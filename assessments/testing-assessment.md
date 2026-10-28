# Redis Automated Testing Assessment

## 1. Introduction

The purpose of this assessment is to evaluate the automated testing capability of the Redis software repository. The assessment examines the test directory, testing instructions, GitHub Actions workflows, and the results of selected automated test jobs.

Repository: https://github.com/redis/redis

## 2. Existing Testing Structure

The Redis repository contains a `tests` directory with several categories, including unit tests, integration tests, module tests, and Sentinel tests.

The repository's README recommends running `make test` after building Redis. It also documents additional TLS testing instructions.

These findings show that Redis has an organized testing structure and documented procedures for running tests.

## 3. Automated Testing

The repository contains GitHub Actions workflow files, including `ci.yml` and `daily.yml`. These workflows automate checks and tests across different configurations.

Two jobs from the Daily workflow were examined.

### 3.1 Successful Test Job

Job: `test-ubuntu-tls`

Result: Passed.

The job completed successfully on October 27, 2026, in approximately 44 minutes and 27 seconds.

This provides evidence that the selected Ubuntu TLS testing job completed successfully. It does not prove that every test or configuration passes.

Evidence: https://github.com/redis/redis/actions/runs/40496677011/job/122163778894

### 3.2 Failed Test Job

Job: `test-centos-jemalloc`

Result: Failed.

The `module api test` step exited with code 1. Two tests failed in `tests/unit/moduleapi/testrdb.tcl`.

**Test 1: Module variable during diskless loading**

The test expected the replica's module variable to equal `value1_master`, but the reported value was `value1_replica`.

**Test 2: Module variable after loading was aborted**

The test expected the replica database size to be 200, but the reported size was 1010.

Both failures concern module state and diskless loading or replication behaviour. The available evidence does not establish their root cause.

Evidence: https://github.com/redis/redis/actions/runs/40496677011/job/122163778925

## 4. Strengths Identified

- Redis has a dedicated test directory with multiple test categories.
- Testing instructions are documented.
- GitHub Actions automates testing across different configurations.
- The inspected Ubuntu TLS job passed.
- Automated testing detected unexpected results in the inspected CentOS/Jemalloc job.

## 5. Risks and Limitations

- Two tests failed in the inspected CentOS/Jemalloc job.
- The root cause of those failures has not been confirmed.
- Only selected workflow results were examined; the assessment does not establish the status of every test.
- The presence of a Codecov workflow configuration does not, by itself, establish the current test coverage percentage.

## 6. Recommendations

1. Review the complete logs for both failed tests.
2. Reproduce the failures to determine whether they are consistent.

## 7. Conclusion

The Redis repository demonstrates an established automated testing process through its test directory, documented commands, and GitHub Actions workflows. The successful Ubuntu TLS job provides positive evidence, while the two failures in the CentOS/Jemalloc job identify an area requiring further investigation. Additional testing and root-cause analysis are necessary before drawing conclusions about the overall reliability of the test suite.