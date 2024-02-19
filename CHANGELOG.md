# CHANGELOG



## v0.2.1-rc.3 (2024-02-19)

### Fix

* fix(cicd): cancel fail-fast behavior of the github action in ecr management stage ([`96d65ac`](https://github.com/tekeinhor/tag-generator/commit/96d65ac4915411594e85ffa40cacc0e31559cd37))

### Test

* test(ci): add a test job just for ECR creation ([`8bda54a`](https://github.com/tekeinhor/tag-generator/commit/8bda54aac6cf0c44484a0ec62e3c57a9589d36fb))

### Unknown

* Merge branch &#39;main&#39; of https://github.com/tekeinhor/tag-generator ([`57bfb8f`](https://github.com/tekeinhor/tag-generator/commit/57bfb8fc697068c56c6590164e5051bb810fe721))


## v0.2.1-rc.2 (2024-02-19)

### Fix

* fix(ci): change ecr repo naming ([`ce19b75`](https://github.com/tekeinhor/tag-generator/commit/ce19b75de04ada877238c4962bc86b2e62bb5a99))

* fix(build): reformat wheel naming format in release candidate case ([`2edcbc2`](https://github.com/tekeinhor/tag-generator/commit/2edcbc2348080594e639f02ee17b397fcd2d2160))


## v0.2.1-rc.1 (2024-02-16)

### Fix

* fix: allow ci to create ECR repo if it doesn&#39;t exist ([`0186b17`](https://github.com/tekeinhor/tag-generator/commit/0186b17d5c30fbba86dad69fda7bb901d9353a4e))

### Unknown

* Merge pull request #19 from tekeinhor/feature-ecr-to-ci

fix: allow ci to create ECR repo if it doesn&#39;t exist ([`fd17e8c`](https://github.com/tekeinhor/tag-generator/commit/fd17e8cf57af40c7c7d1b9c6adf220ae0890a29a))


## v0.2.0 (2024-02-16)

### Documentation

* docs: add ci workflow documentation and disable ci run for assets/ dir ([`f57ccb0`](https://github.com/tekeinhor/tag-generator/commit/f57ccb0aa1a4378bf1675bc62484b096a100582f))

* docs: update readme with project goal, code structure and tools used ([`dac5cf9`](https://github.com/tekeinhor/tag-generator/commit/dac5cf9fb37f51e2dbd5bea54aa72ade8f14f878))

### Feature

* feat(ui): add dockerfile for UI ([`ea76269`](https://github.com/tekeinhor/tag-generator/commit/ea762691eb4caf70e29a7b615678f3a9871d0ea9))

* feat: update version of image in ecs ([`941c52d`](https://github.com/tekeinhor/tag-generator/commit/941c52dacd3aa3079a38f4f4de4d7019dbc546bf))

### Fix

* fix: run streamlit as a python pkg to avoid import error in docker ([`8c1d103`](https://github.com/tekeinhor/tag-generator/commit/8c1d103f66fd8d60f8b6842b6034765fe8ad1fc8))

* fix(iac): add missing task_role_arn for ECS docker permissions ([`fa281d4`](https://github.com/tekeinhor/tag-generator/commit/fa281d437d8ba1730ff1b3dce77dd87d0dbd4dfa))

### Unknown

* Merge pull request #18 from tekeinhor/feature-ui

feat(ui): add dockerfile for UI ([`827f732`](https://github.com/tekeinhor/tag-generator/commit/827f732824f322c101002cb80539a9178863dbf0))


## v0.1.2 (2024-02-07)

### Fix

* fix: correct typo in ecr repo prefix ([`073f2df`](https://github.com/tekeinhor/tag-generator/commit/073f2dfc067d9dc8978e40301baf92e108cd9018))


## v0.1.1 (2024-02-07)

### Fix

* fix: test checkout in checks with pat ([`c84d51f`](https://github.com/tekeinhor/tag-generator/commit/c84d51f729f9e383d5558d9c61912f1e520c12f0))

### Unknown

* Merge branch &#39;main&#39; of https://github.com/tekeinhor/tag-generator ([`8a573f8`](https://github.com/tekeinhor/tag-generator/commit/8a573f8459d3fa27ad342031c6f27d99d66ea6cf))


## v0.1.1-rc.1 (2024-02-07)

### Fix

* fix: replace semantic-release token with pat ([`ed01c78`](https://github.com/tekeinhor/tag-generator/commit/ed01c784d3b9a641a83d14be044ba670b6125391))

* fix: add permission to docker build job ([`c527312`](https://github.com/tekeinhor/tag-generator/commit/c52731267ab0e47ef8546cbc74b62236498388b0))

* fix: use correct key name for semantic release ([`0ce83f3`](https://github.com/tekeinhor/tag-generator/commit/0ce83f3734ea13ff971d2b48781408a97f5cc04f))


## v0.1.0 (2024-02-07)

### Test

* test: remove token used in checkout and test deploy key with semantic release ([`c18a655`](https://github.com/tekeinhor/tag-generator/commit/c18a655793c1cebbc59493fe339d90a02b97901d))

* test: use PAT as secrets for semantic release ([`45303d3`](https://github.com/tekeinhor/tag-generator/commit/45303d3280c98d613f1e00ceae86986a3ab8a6a7))

* test: use deploy key instead of github token ([`4943961`](https://github.com/tekeinhor/tag-generator/commit/49439611f1b6c077502d5b9b4d69f37f20a73301))


## v0.1.0-rc.1 (2024-02-06)

### Chore

* chore(cicd): change deploy job order and remove provider from child module ([`4ce3772`](https://github.com/tekeinhor/tag-generator/commit/4ce37722f4b086a37ee0a63d31852661411a51e4))

* chore(iac): add ability to use email as primary email in aws ([`0ccc84b`](https://github.com/tekeinhor/tag-generator/commit/0ccc84bfc338a6b1d3505e12158dcd63cfa885a0))

* chore(cicd): change workflow name et remove run-name ([`b28fcb2`](https://github.com/tekeinhor/tag-generator/commit/b28fcb27141dbe953259fd3a29fa52a4d8189e6d))

* chore(iac): apply terraform fmt and remove role ([`ccfeddf`](https://github.com/tekeinhor/tag-generator/commit/ccfeddf39b322e9fe2328843dac1c2aaffc573a9))

* chore(tag_generator): apply linter and fmt ([`35f8739`](https://github.com/tekeinhor/tag-generator/commit/35f8739200e0f614721b3bcc3c3c7e04f189db8c))

* chore: update gitignore ([`25ff3c3`](https://github.com/tekeinhor/tag-generator/commit/25ff3c3fd8fd4140664d913f3dd21f587741eccc))

* chore: apply linter to ui ([`6a723bb`](https://github.com/tekeinhor/tag-generator/commit/6a723bb9af78563d7f3769ee0dbce7efcdd08e2c))

* chore: add pylint and isort pkg to code audit tool and apply audit to code ([`8ea9224`](https://github.com/tekeinhor/tag-generator/commit/8ea92243b58b6d91dddabfe634b19caf629fb5ea))

* chore: use code_audit tool in core ([`e9cd61c`](https://github.com/tekeinhor/tag-generator/commit/e9cd61cb729cb2a6f4b2099f64d5562d981aa665))

### Ci

* ci(badge): add/update test-cov badge ([`9493955`](https://github.com/tekeinhor/tag-generator/commit/9493955872d25307bb35e72b4eaecf1007f42191))

* ci(badge): add/update test-cov badge ([`7348652`](https://github.com/tekeinhor/tag-generator/commit/7348652628df9d1fc316ad376dfce1701878116e))

* ci(badge): add/update test-cov badge ([`ef0db35`](https://github.com/tekeinhor/tag-generator/commit/ef0db35fcd488d3ad9e5d70c7c5bc3b59f167939))

* ci(badge): add test-cov badge ([`8f13c28`](https://github.com/tekeinhor/tag-generator/commit/8f13c28bf2f35dcd9047336ac30972c9e89e352e))

### Feature

* feat(cicd): add semantic release ([`72b5caa`](https://github.com/tekeinhor/tag-generator/commit/72b5caaf9953e0a4ac23a670631c55b889134e4a))

* feat(iac): create log group and update naming to reflect dev env (#9) ([`3533977`](https://github.com/tekeinhor/tag-generator/commit/3533977ae4b065cf4f0842c08a2532eef869a2fd))

* feat(iac): add logs config and fix task definition port mapping (#8) ([`7018214`](https://github.com/tekeinhor/tag-generator/commit/7018214308ad82689947629ddb62dac50cbac48c))

* feat(iac): add load balancer to ecs in order to have a url for the api (#7) ([`97b40ec`](https://github.com/tekeinhor/tag-generator/commit/97b40ec01ffe580cefd352c0ef8703d9257c38e2))

* feat(iac): add api deployment in ecs in dev env (#6) ([`b0de26d`](https://github.com/tekeinhor/tag-generator/commit/b0de26d8d65a04a7b98d087a1fc2239724aeb1df))

* feat(iac): create ecr and rename main to iam to reflect its content (#5) ([`9a1dbdb`](https://github.com/tekeinhor/tag-generator/commit/9a1dbdb89589a67481186d69d7d5abad8a3dcaba))

* feat(cicd): create build job ([`c989d82`](https://github.com/tekeinhor/tag-generator/commit/c989d8280b05167f49792520cd4d80a48d2d6945))

* feat(scripts): automate pkg build scripts ([`93f75a2`](https://github.com/tekeinhor/tag-generator/commit/93f75a20a84750cc4c268f11786cc1641266f0ee))

* feat(api): add s3 model retrieval and add lifespan to api ([`c3b3c08`](https://github.com/tekeinhor/tag-generator/commit/c3b3c089791a38c54809adb04c90937e7bbd4cf8))

* feat(cicd): trigger deploy (tf plan and apply) through pull request (#1)

* feat: create a specific state file for global and dev

* feat(cicd): trigger tf plan only on PR and tf apply only on pr merged to main

* fix(cicd): fix plan formatting output in comment

* fix(cicd): format s3 file in dev and add fancy smileys to tf plan output ([`d6d04cf`](https://github.com/tekeinhor/tag-generator/commit/d6d04cf0d0421bc18b72bd045013f53fcd9b7bd8))

* feat: create a specific state file for global and dev ([`0004a74`](https://github.com/tekeinhor/tag-generator/commit/0004a742e9cd574c28d11cd61cd5b2bab1efb072))

* feat(iac): create users and give access ([`0ba64f7`](https://github.com/tekeinhor/tag-generator/commit/0ba64f7821cd6d3a1847bcd238e19f5c66f7e78e))

* feat(cicd): create deploy template et use it for iac resource deployment ([`ae0bcb9`](https://github.com/tekeinhor/tag-generator/commit/ae0bcb9a1594721e68032f22cbd7a904b702ad1c))

* feat(cicd): create terraform s3 modules and add its deployment to github workflow ([`44f7f9c`](https://github.com/tekeinhor/tag-generator/commit/44f7f9cde1b371080a266869f3f990b067b7b761))

* feat(cicd): create badge for test coverage ([`e1ae0f8`](https://github.com/tekeinhor/tag-generator/commit/e1ae0f8dbb389600b3441122e99b7975ea282a4d))

* feat(ci): create a demo github action demo ([`54447e8`](https://github.com/tekeinhor/tag-generator/commit/54447e811c1695b98722b4cea7cc38d7288c26d4))

* feat(scripts): create script for auto build of sub repos ([`5eb543a`](https://github.com/tekeinhor/tag-generator/commit/5eb543a49da583395b086eafb390cd8985f5f266))

* feat(core): add settings, add download_dir for nltk ([`148d35b`](https://github.com/tekeinhor/tag-generator/commit/148d35bc429bb25d522017e579df5958d99d9b6e))

* feat(api): apply linter and fmt ([`30eaa81`](https://github.com/tekeinhor/tag-generator/commit/30eaa819a517a7dd580c1b434a64f3abb1f0b542))

* feat(api): create docker and docker compose for api ([`ff8a5bc`](https://github.com/tekeinhor/tag-generator/commit/ff8a5bcb96ede52594ddc88744041b4813287f17))

* feat(api): remove singleton and use global var for model ([`f26acaa`](https://github.com/tekeinhor/tag-generator/commit/f26acaaa756aa13c7e8c8e58e9e18458a06f5c42))

* feat(tools): add mypy back to linter ([`96dd1a5`](https://github.com/tekeinhor/tag-generator/commit/96dd1a5cb63fb3c24afa79b2c08e02d86da1b328))

* feat(ui): use api in ui for tag generation ([`b309e68`](https://github.com/tekeinhor/tag-generator/commit/b309e682d9f6b1292521b43304db91a255cd3514))

* feat(api): add prediciton endpoints using local model ([`d7034d2`](https://github.com/tekeinhor/tag-generator/commit/d7034d2dedee94018afb579137ccd83a6d5a74a4))

* feat(core): add exploration and model notebook ([`2551d28`](https://github.com/tekeinhor/tag-generator/commit/2551d2814c0a41f1edf14b84249a86df9b73241c))

* feat: create empty API ([`d447a92`](https://github.com/tekeinhor/tag-generator/commit/d447a92e0a56682fc1ce6bc82356660a6eb6d6a2))

* feat: add text preprocessing for tag generator ([`b5a7e3b`](https://github.com/tekeinhor/tag-generator/commit/b5a7e3b3dedd7dd850a581df5d354ae52495025c))

* feat: add logger and update audit spinner ([`5639204`](https://github.com/tekeinhor/tag-generator/commit/563920418a5e9be1a376ccfb90d7b566d206055c))

* feat: create first proto of UI using streamlit ([`f95b035`](https://github.com/tekeinhor/tag-generator/commit/f95b03568c439ed4a15a5c96b45a30ce954d9ed5))

* feat: update code audit and add toml config file handling ([`e0aa95c`](https://github.com/tekeinhor/tag-generator/commit/e0aa95c3b41486bc258c12a6f57f2022b4935904))

* feat: create dev tools (for code audit) in libs ([`d9fec09`](https://github.com/tekeinhor/tag-generator/commit/d9fec09873bc6b01fd83237e8b172d9b076ff085))

* feat: init repo with poetry, readme and basic pipeline ([`ed16de3`](https://github.com/tekeinhor/tag-generator/commit/ed16de3e98ef0cf9f97dbe0b0a4a155f16889763))

### Fix

* fix(cicd): add concurrency and depth to release step ([`06630fe`](https://github.com/tekeinhor/tag-generator/commit/06630fe2a70850893ec8d9e33d84e580407e5a5d))

* fix(cicd): add safety option to git config to avoid repository ownership error ([`e048c15`](https://github.com/tekeinhor/tag-generator/commit/e048c152212884b4767e151b71428a762876ac7d))

* fix(cicd): add job permissions for semantic-release ([`bfdba47`](https://github.com/tekeinhor/tag-generator/commit/bfdba47a58b8c6b4426fdd346806f452befd8c7c))

* fix(cicd): update event that triggers release ([`7ba2276`](https://github.com/tekeinhor/tag-generator/commit/7ba22768a056977c5845a5a41d95eb2d4f981085))

* fix(cicd): update semantic-release pkg name in ci ([`eae6f74`](https://github.com/tekeinhor/tag-generator/commit/eae6f74ad59cdea13bb42e5df0862baa2882577a))

* fix(api): add option to use profile or not with boto3 ([`47deed7`](https://github.com/tekeinhor/tag-generator/commit/47deed70ea82ac39616fde0c2fa716ca6782fc7d))

* fix(cicd): change trigger condition for plan (#3) ([`a106484`](https://github.com/tekeinhor/tag-generator/commit/a106484a5818d8f1700164800b0f8504f2270647))

* fix(cicd): update template name in deploy file after renaming ([`626c49b`](https://github.com/tekeinhor/tag-generator/commit/626c49b50e9e09f1e6514142cf053575b1815bf7))

* fix(iac): change ssoadmin_instances resource name and apply lint and fmt ([`4ef4b25`](https://github.com/tekeinhor/tag-generator/commit/4ef4b25abbce2d8be7105b65ffb365877cf7ea05))

* fix(cicd): change terraform-version input type to match tf actions&#39; ([`1c19dad`](https://github.com/tekeinhor/tag-generator/commit/1c19dade38d63372ab570b5578668c6bb0d380c0))

* fix(cicd): fix ill indentation of steps in deploy template ([`4911195`](https://github.com/tekeinhor/tag-generator/commit/4911195407131e6dc2cc6011a5778a1133f2c097))

* fix(cicd): fix ill indentation in deploy template ([`8a5e4d9`](https://github.com/tekeinhor/tag-generator/commit/8a5e4d9067ee58fe3981d26bc2449fe99642f2db))

* fix(cicd): change script indentation under uses.with ([`7418f1b`](https://github.com/tekeinhor/tag-generator/commit/7418f1b868c1d4f7130f9e951896e74aa0b06b12))

* fix(cicd): replace tab with double space ([`4efbc50`](https://github.com/tekeinhor/tag-generator/commit/4efbc50fbda9e2b1fb622ea8f85f594f5de11408))

* fix(cicd): surrend paths and paths-ignore with quotes ([`8053209`](https://github.com/tekeinhor/tag-generator/commit/8053209aefb30730d2939288b36b53ac22300912))

* fix(ci): update workflow name in ci and badge link in readme ([`fce9a09`](https://github.com/tekeinhor/tag-generator/commit/fce9a0940087d86a7d48e39bdf8e73bb16bb7218))

* fix(cicd): commit generated report badge ([`f2f0a30`](https://github.com/tekeinhor/tag-generator/commit/f2f0a30f2da0e922986158cfcb64f162fec3b3a3))

* fix(cicd): activate poetry env for each run ([`e112216`](https://github.com/tekeinhor/tag-generator/commit/e1122169afda25b13c6f2d1900d3bd481f7dd1bf))

* fix(cicd): add pytest to test-cov workflow ([`3b78199`](https://github.com/tekeinhor/tag-generator/commit/3b781993876e14176f9722de2e98950b8d269053))

* fix: try to install coverage directly ([`5c13038`](https://github.com/tekeinhor/tag-generator/commit/5c13038fb5e4e3c968f574519567250ee5f92dec))

* fix(tools): exit scripts when there is an error ([`33fd501`](https://github.com/tekeinhor/tag-generator/commit/33fd5010da8f6ffcc581278219be3ec929cae029))

* fix(cicd): move the comment line that breaks the workflow ([`8a395de`](https://github.com/tekeinhor/tag-generator/commit/8a395de99c3e04a0b69a01b6973d925635d7b771))

* fix(cicd): replace command for activating poetry in gitlab ci runer ([`5e3c084`](https://github.com/tekeinhor/tag-generator/commit/5e3c084648de0a1a4ab7ad06ad285b1905b43d95))

* fix(ui): force a git mv to change filename case ([`af0b0ac`](https://github.com/tekeinhor/tag-generator/commit/af0b0acb56a5985a433d2952aaea70aa6dc80d4a))

* fix(ui): change readme file name case causing an error in the cicd install of the pkg ([`0c10a27`](https://github.com/tekeinhor/tag-generator/commit/0c10a273ae8b9654012ba257e9f37250926d6a90))

* fix(core): add timer to pipe creation function and fix tag list creation bug ([`2cb6b91`](https://github.com/tekeinhor/tag-generator/commit/2cb6b915c089e90187cf8bc0e2206f464fa77f4e))

### Refactor

* refactor(cicd): use python-semantic-release action ([`690024c`](https://github.com/tekeinhor/tag-generator/commit/690024c80821792035b57cef864da9cd264ff69e))

* refactor(cicd): correct typo in build step (#4)

* refactor(cicd): correct typo in build step

* fix(cicd): install python and poetry

* refactor(iac): rename file to represent its content

* feat(ecr): create ECR for api

* fix(cicd): fix indention inconsistency in docker workflow ([`593d00f`](https://github.com/tekeinhor/tag-generator/commit/593d00fd239f0a45e2a7c74a977c707ddddd4501))

* refactor(cicd): rename build workflow to checks ([`c5a37c9`](https://github.com/tekeinhor/tag-generator/commit/c5a37c971ac1aaec046fa1a4a195053f6b1ed4b3))

* refactor(cicd): trigger ci when pull request has been closed (#2) ([`bb759a9`](https://github.com/tekeinhor/tag-generator/commit/bb759a9f0ce413e6caeb0ad540569cc6819a9c1b))

* refactor(cicd): disable ci build when no python has been changed ([`a56514f`](https://github.com/tekeinhor/tag-generator/commit/a56514fc52cab4b262dfb3491ac2e8dfdddc44b9))

* refactor(iac): remove output from s3 module ([`5fc359f`](https://github.com/tekeinhor/tag-generator/commit/5fc359fe2f1b624cad5d65d497f4c1d2a1349499))

* refactor(cicd): change terraform working dir to dev env ([`8d8ce0a`](https://github.com/tekeinhor/tag-generator/commit/8d8ce0af935b8c3526f70d2062c8a231dc316c3a))

* refactor: set working-directory to terraform dir ([`f96cef4`](https://github.com/tekeinhor/tag-generator/commit/f96cef49e3eab2907c9636ac764facc4970c4b1f))

* refactor(ci): only push badge when the coverage has changed ([`19bcda4`](https://github.com/tekeinhor/tag-generator/commit/19bcda4b312f519a26b962986743268c5243f03f))

* refactor(core): restructure core folder ([`2e237c1`](https://github.com/tekeinhor/tag-generator/commit/2e237c15ba39e99a615b0df447c14a04c318d5d5))

### Test

* test(api): remove engine as a global var making the api testable ([`4d669ea`](https://github.com/tekeinhor/tag-generator/commit/4d669ea89306ecc985b8eeee58e98300ed3c129d))

* test(cicd): update workflow to build python ([`36cff45`](https://github.com/tekeinhor/tag-generator/commit/36cff45b8c6d3c06eac4e9e20aa072f55867c488))

* test(api): add tests ([`9919d0f`](https://github.com/tekeinhor/tag-generator/commit/9919d0f8699ac8b3bdafcdad6b3d8271ce62caab))

* test(core): add one unit test ([`984fcfb`](https://github.com/tekeinhor/tag-generator/commit/984fcfbba034b43bec4474e180baa6ff76fae8bc))

### Unknown

* Merge branch &#39;main&#39; of https://github.com/tekeinhor/tag-generator ([`a6431a5`](https://github.com/tekeinhor/tag-generator/commit/a6431a56bd36ffd162b52e133d0130df86cf1612))

* refactor(): rename pkg to taggenerator to avoid confusing between dash and underscore ([`ad1dd7d`](https://github.com/tekeinhor/tag-generator/commit/ad1dd7dcd80776d70eaf0a9392a9467278affb8a))

* Merge branch &#39;main&#39; of https://github.com/tekeinhor/tag-generator ([`920a735`](https://github.com/tekeinhor/tag-generator/commit/920a7352068e48e9805461415a9e7172671cefde))

* Merge branch &#39;main&#39; of https://github.com/tekeinhor/tag-generator ([`c8d0685`](https://github.com/tekeinhor/tag-generator/commit/c8d068563a766b59c611bfbf0884b4b548bf644f))

* test(): add more tests and create scripting test in bash ([`b4a63a1`](https://github.com/tekeinhor/tag-generator/commit/b4a63a13eb91d6c07aa847673e6062870be325eb))

* Merge branch &#39;main&#39; of https://github.com/tekeinhor/tag-generator ([`f660a8b`](https://github.com/tekeinhor/tag-generator/commit/f660a8baf8fa9e277ec164fd62c2136ed1ec3fd7))

* feat(): add coverage pkg ([`aa73c64`](https://github.com/tekeinhor/tag-generator/commit/aa73c6439e93b40bc033bb0a368e65c151c82f9f))

* doc(): add demo build badge ([`6b59ee2`](https://github.com/tekeinhor/tag-generator/commit/6b59ee2f95377b0e96e85ca68d5a69244953cda9))

* chore(): install semantic-release ([`75c73ab`](https://github.com/tekeinhor/tag-generator/commit/75c73abc0729af1204afff4f48be240a95df8c60))

* chore(): update ignore list for pylama ([`a2df940`](https://github.com/tekeinhor/tag-generator/commit/a2df9408660cb08ad7cebd960287c48af8728ad2))
