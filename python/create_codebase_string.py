from git import Repo

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