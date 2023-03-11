# v1.0.3

( developing )

## Migrations

Use search and replace of vscode with regex functionality enabled

### quest_start

* `quests["quest_id"].start()`
* `quest_start(id = "quest_id")`

### quest_nextStage

* `quests["quest_id"].nextStage()`
* `quest_nextStage(id = "quest_id")`

### quest_nextStageOnlyIsCompleted

* `quests["quest_id"].nextStageOnlyIsCompleted()`
* `quest_nextStageOnlyIsCompleted(id = "quest_id")`

### quest_setDayNumberRequiredToStart

* `quests["quest_id"].SetDayNumberRequiredToStart(day = 2)`
* `quest_setDayNumberRequiredToStart(id = "quest_id", day = 2)`

### new_day

* `tm.new_day()`
* `new_day()`

### new_hour

* `tm.new_hour(3)`
* `new_hour(3)`

### setFlags

* `flags["flag_id"] = True`
* `setFlags("flag_id", True)`

# v1.0.2

```shell
git checkout -b NQTR-toolkit
git checkout NQTR-toolkit
git config pull.rebase false
git pull https://github.com/DRincs-Productions/NQTR-toolkit.git v1.0.2 --allow-unrelated-histories

```

## What's Changed

* fix and improve by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/53>
* 20 add notifications and improve log by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/54>
![image](https://user-images.githubusercontent.com/67595890/198825289-292df3da-8143-4fbf-a686-24e42c744d8c.png)
![image](https://user-images.githubusercontent.com/67595890/198825291-1cf9be09-a074-49dd-9c40-8741f93dbeda.png)

**Full Changelog**: <https://github.com/DRincs-Productions/NQTR-toolkit/compare/v1.0.1...v1.0.2>

# v1.0.1

## What's Changed

* Create LICENSE by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/1>
* Ren'Py 8.0.0 by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/8>
* 9 typify python by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/10>
* 14 code snippets by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/27>
* 11 improving the quest system by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/33>
* 12 pass by object reference by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/34>
* 16 after closing a label it should not be mandatory to close with call screen room navigation by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/37>
* Update time_label.rpy by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/38>
* fix by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/41>
* align cash label by @01010100010100100100100101000111 in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/44>
* Fixes for #42 and #43 by @01010100010100100100100101000111 in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/45>
* clean by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/49>
* 15 create a button class to be extended by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/50>  (**IMPORTANT**: Some property names have been changed: So it gives errors when inserted in an old version. But it does not create any problems in saves.   )
* 4 map navigation possibility to use multiple maps by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/51>

## New Contributors

* @DonRP made their first contribution in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/1>
* @01010100010100100100100101000111 made their first contribution in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/44>

**Full Changelog**: <https://github.com/DRincs-Productions/NQTR-toolkit/commits/v1.0.1>

# v1.0.0

```shell
git checkout -b NQTR-toolkit
git checkout NQTR-toolkit
git pull https://github.com/DRincs-Productions/NQTR-toolkit.git v1.0.0 --allow-unrelated-histories

```

## What's Changed

* Create LICENSE by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/1>
* Ren'Py 8.0.0 by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/8>
* 9 typify python by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/10>
* 14 code snippets by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/27>
* 11 improving the quest system by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/33>
* 12 pass by object reference by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/34>
* 16 after closing a label it should not be mandatory to close with call screen room navigation by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/37>
* Update time_label.rpy by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/38>

## New Contributors

* @DonRP made their first contribution in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/1>

**Full Changelog**: <https://github.com/DRincs-Productions/NQTR-toolkit/commits/v1.0.0>
