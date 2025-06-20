from git import Repo

#TODO - lot of hack in this file, I'm tired :)
# Add in the OpenTofu binary to interrogate each directory with TF files to see if it's a valid module to better understand mono-repos when present
# Add in an in-memory graph representation of the TF files to suppliment the model input
# Use better naming conventions and more effecient string concatenation

def lazy_concatenate_tf_files(pygit_codebase):
    return terraform_blobs_to_string(pygit_codebase)


def terraform_blobs_to_string(pygit_codebase) -> str:
    """
    Build one string that contains every *.tf and *.tf.json file at HEAD.

    Format:
        ##### <relative/path>.tf #####
        <file contents>

        ##### <relative/path>.tf.json #####
        <file contents>
    """
    parts = []

    for blob in pygit_codebase.tree.traverse():     # walk the entire tree
        # skip directories and blobs that aren’t Terraform sources
        if blob.type != "blob":
            continue
        if not (blob.path.endswith(".tf") or blob.path.endswith(".tf.json")):
            continue

        try:
            text = blob.data_stream.read().decode("utf-8", "replace")
        except Exception:
            # Binary or bad encoding: drop it (usually won’t happen for .tf files)
            continue

        parts.append(f"##### {blob.path} #####\n{text}")

    return "\n\n".join(parts)