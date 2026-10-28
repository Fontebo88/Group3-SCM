TASK 9: SECURITY AND MAINTENANCE REPORT
Repository: redis/redis | Group 3
Date: 28 October 2026
1. Introduction
This report looks at the security and maintenance of the Redis GitHub repository. It uses the screenshots provided to check the .gitignore file, supported versions, security reporting, security alerts, and recent project activity.
2. Evidence from GitHub
The figures below show the main evidence used in this report.
 
Fig 9.1: The .gitignore file excludes build files and binaries.
 
Fig 9.2: Redis lists the versions that still receive support.
 
Fig 9.3: Redis explains how to report security problems.
 
Fig 9.4: The repository lists security advisories, including serious issues.
 
Fig 9.5: GitHub Pulse shows active development during 21–28 October 2026.
3. Findings
This table summarises the evidence, what could not be confirmed, the possible risk, and what should be done.
Area	Evidence	Gap	Risk	Recommendation
.gitignore	The file ignores build files, logs, and Redis binaries.	It does not prove that passwords or other secrets were never uploaded.	Low for the files shown.	Keep the file updated and use secret scanning.
Secret handling	The screenshots do not show secret-scanning settings.	We could not confirm whether leaked passwords or keys are checked automatically.	Unknown; exposed secrets can be misused.	Enable secret scanning where available. Store passwords and keys safely, and change them if exposed.
Dependencies	The screenshots do not show dependency checks.	We could not confirm whether dependency alerts and automatic updates are enabled.	Unknown; old packages may contain weaknesses.	Check dependency alerts and update packages when needed.
Repository settings	A CodeQL workflow is listed. The Security and quality tab shows 47 alerts.	The number 47 does not tell us how many alerts are still open. Access and branch settings were not checked.	Some security issues may need attention.	Check each alert and CodeQL results. Protect important branches and limit access.
4. Supported Versions and Reporting Security Problems
Redis lists which versions are still supported. Users should check their version and upgrade when needed, because older versions may no longer receive security fixes.
The security page tells people to report problems through the Redis Vulnerability Disclosure Program. It also provides security@redis.com as a contact. This gives researchers a clear way to report security problems.
The advisory list includes serious issues, some of which may allow remote code execution. We must check which versions are affected before saying that a particular installation is vulnerable.
5. Maintenance Activity
The Pulse screenshot covers 21–28 October 2026. It shows 71 active pull requests, 32 merged pull requests, 39 open pull requests, 11 active issues, and seven releases. It also shows commits from several contributors. This suggests that the project was actively maintained during that week.
6. Licensing Risk
Redis licensing changed across versions. Redis 7.2 and earlier use the BSD-3-Clause licence. Redis 7.4–7.8 has different licence options, and Redis 8.0 and later offers RSALv2, SSPLv1, or AGPLv3. These licences do not all have the same rules.
The legal risk can be high if a team uses Redis without checking the licence for its exact version. Users should read the licence before using Redis in a product or service. This does not mean that all use of Redis is illegal.
7. Conclusion
Based on the screenshots, Redis appears to be actively maintained. It has a .gitignore file, a supported-version list, a way to report security problems, security advisories, and a CodeQL workflow.
Maintenance rating: 5/5 based on the visible activity and information.
Abandonment risk: Very low, because the screenshots show recent commits, pull requests, and releases.
Legal risk: High if the licence is not checked before use, especially for Redis 8.0 and later. The screenshots alone are not enough to confirm that the repository has no security problems.
8. References
•	Redis security page: https://github.com/redis/redis/security
•	Redis CodeQL workflow: https://github.com/redis/redis/actions/workflows/codeql-analysis.yml
•	Redis licence file: https://github.com/redis/redis/blob/unstable/LICENSE.txt
•	Redis licensing information: https://redis.io/legal/licenses/
•	Redis GitHub repository: https://github.com/redis/redis
