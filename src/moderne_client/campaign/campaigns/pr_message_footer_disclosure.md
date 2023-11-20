# :arrow_right: Vulnerability Disclosure :arrow_left:

:wave: Vulnerability disclosure is a super important part of the vulnerability handling process and should not be skipped! This may be completely new to you, and that's okay, I'm here to assist!

First question, do we need to perform vulnerability disclosure? It depends!

1. Is the vulnerable code only in tests or example code? No disclosure required!
2. Is the vulnerable code in code shipped to your end users? Vulnerability disclosure is probably required!

## Vulnerability Disclosure How-To

You have a few options to perform vulnerability disclosure. However, I'd like to suggest the following 2 options:

1. Request a CVE number from GitHub by creating a repository-level [GitHub Security Advisory](https://docs.github.com/en/code-security/repository-security-advisories/creating-a-repository-security-advisory).
   This has the advantage that, if you provide sufficient information, GitHub will automatically generate Dependabot alerts for your downstream consumers, resolving this vulnerability more quickly.
2. Reach out to the team at Snyk to assist with CVE issuance.
   They can be reached at the [Snyk's Disclosure Email](mailto:report@snyk.io).
   Note: Please include `Jonathan Leitschuh` in the subject of your email, so it is not missed.

## Why didn't you disclose privately (ie. coordinated disclosure)?

This pull request (PR) was automatically generated.

This is technically what is called "Full Disclosure" in vulnerability disclosure terminology, and I agree it's less than ideal. Currently, GitHub, GitLab, and BitBucket do not have support for private pull requests that can be opened by security researchers via an API, therefore, this is a stop gap process until the functionality is available.

As an open source security researcher, or even as a maintainer, there is limited time in the day. A single vulnerability could impact hundreds, or even thousands of open source projects. With tools like GitHub Code Search and CodeQL, this simplifies the identification and detection process, however, it is based on knowledge of vulnerabilities. This does not scale well.

There are several known challenges to open source security research, such as it's a long and tedious process that must be performed with time and care. Tracking individuals via email, JIRA, and bat signals also takes time, research, and isn't an automate-able process. As we study and design ways to automate at scale, individual reporting is also an issue, where security researchers do not wish to spam emails or issues, nor overwhelm already overly tax maintainers. This is not our goal.

Additionally, if we just spam out emails or issues, we’ll just overwhelm already over-taxed maintainers. We don't want to do this either.

By creating a pull request, we aim to provide maintainers a highly actionable way to fix the identified vulnerability, quickly, via a pull request.

There's a larger discussion on this topic that can be found here: https://github.com/JLLeitschuh/security-research/discussions/12
