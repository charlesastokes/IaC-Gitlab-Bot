# Documentation for Terraform IAM Changes

## Summary

This document outlines the recent changes made to the IAM configuration in our Terraform codebase. The core change involves altering IAM role policy assignments which can have significant security implications.

## Change Details

### Changed IAM Role Policy Attachment
- **File:** `iam.tf`
- **Resource Changed:** `aws_iam_role_policy_attachment.ec2_read_only`
- **Original Policy Attachment:**
  - **Policy ARN:** `arn:aws:iam::aws:policy/ReadOnlyAccess`
  - **Description:** This policy allowed the associated EC2 instance role (`ec2_role`) to perform read-only operations, such as listing S3 buckets and describing EC2 instances, thereby limiting its permission scope to non-destructive actions.
- **Updated Policy Attachment:**
  - **Policy ARN:** `arn:aws:iam::aws:policy/AdministratorAccess`
  - **Description:** This policy grants full administrative rights, giving the EC2 instance role (`ec2_role`) comprehensive permissions over the AWS account.

## Security Implications

Switching from `ReadOnlyAccess` to `AdministratorAccess` dramatically broadens the scope of permissions granted to the EC2 instance running with this IAM role. This change poses considerable security risks, including:

- **Increased Attack Surface:** The instance now has permissions to modify, delete, or create AWS resources across the account, potentially leading to unintentional or malicious actions.
- **Potential for Privilege Escalation:** If the instance or its associated applications get compromised, an attacker could leverage these administrative privileges to further access resources within the AWS environment.
- **Lack of Principle of Least Privilege:** By granting `AdministratorAccess`, we violate the best practice of least privilege, which insists that entities should only have access to the permissions necessary for their function.

## Recommendations

1. **Evaluate Requirement:** Ensure that the EC2 instance genuinely requires full administrative access. If not, revert to a more restrictive policy or customize a policy that grants only the necessary permissions.

2. **Consider Custom Policies:** If specific permissions beyond read-only access are needed, consider creating a custom IAM policy that defines only those necessary actions.

3. **Audit and Monitoring:** Implement monitoring for any unusual activities performed by this role using AWS CloudTrail and set up alarms for critical actions indicative of potential security breaches.

4. **Documentation and Justification:** If retaining `AdministratorAccess` is necessary, document the justification thoroughly and ensure all team members understand the responsibilities and risks associated with this level of access.

## Conclusion

The change to `AdministratorAccess` significantly escalates the privileges of the IAM role associated with the EC2 instance. It's crucial to deliberate on this change, considering the potential security impacts and ensuring proper monitoring and documentation are in place to mitigate associated risks.
