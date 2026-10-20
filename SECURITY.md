# Security policy

ModelCompass is a documentation-based advisory skill; it does not need API credentials or shell hooks to recommend models.

- Review any third-party installer before running it and check the target directories.
- Installing user-globally changes files in the current user's agent configuration; it does **not** grant access to remote machines.
- Treat model selection and data transmission as separate decisions. A model might be suitable yet disallowed by privacy restrictions.
- Never provide sensitive repository contents, secrets, or personal data just to test model quality.
- Do not trust recommendations that request secrets or bypass your agent's controls.

Report vulnerabilities privately to a repository maintainer through GitHub's private vulnerability reporting feature once enabled. Do not publish exploitable details in public issues.