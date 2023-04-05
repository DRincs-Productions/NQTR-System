# version beta

```shell
git checkout -b nqtr-tool
git checkout nqtr-tool
git config pull.rebase false
git pull https://github.com/DRincs-Productions/NQTR-System.git tool-only --allow-unrelated-histories

```


## Migrations

Use search and replace of vscode with regex functionality enabled

![image](https://user-images.githubusercontent.com/67595890/224504331-1f546922-5673-4fa9-8cc7-e3fc4e671305.png)

### getTalkLabelName

* `getTalkLabelName\(\)`
* `label_name`

### getButtonIcon

* `getButtonIcon\(\)`
* `button_icon`

### get_hour_name

* `get_hour_name\(\)`
* `hour_name`

### get_day_number

* `get_day_number\(\)`
* `day_number`

### get_hour_number

* `get_hour_number\(\)`
* `hour_number`

### get_weekday_number

* `get_weekday_number\(\)`
* `weekday_number`

### get_weekday_name

* `get_weekday_name\(\)`
* `weekday_name`

# v1.0.3

```shell
git checkout -b nqtr-tool
git checkout nqtr-tool
git config pull.rebase false
git pull https://github.com/DRincs-Productions/NQTR-System.git v1.0.3 --allow-unrelated-histories

```

Now NQTR is a python library, and renpy interacts with it through easy-to-use functions.

What it means:

Pros:

* Performance
* I can now develop directly with python. this makes my life easier since I can use the tools to develop in python
* Can create tests
* From now on future versions will have less complex migration: since now I aim to modify as little as possible renpy functions , but only the library.

Cons:

* Sharing variables with renpy and the library is slightly more difficult because it relies on pointers. (As long as I only share dictionaries, I won't have any big problems).

## Migrations

Use search and replace of vscode with regex functionality enabled

![image](https://user-images.githubusercontent.com/67595890/224504331-1f546922-5673-4fa9-8cc7-e3fc4e671305.png)

### quest_start

* `quests\["(.*)"\].start\(\)`
* `quest_start(id = "$1")`

### quest_nextStage

* `quests\["(.*)"\].nextStage\(\)`
* `quest_nextStage(id = "$1")`

### quest_nextStageOnlyIsCompleted

* `quests\["(.*)"\].nextStageOnlyIsCompleted\(\)`
* `quest_nextStageOnlyIsCompleted(id = "$1")`

### quest_setDayNumberRequiredToStart

* `quests\["(.*)"\].SetDayNumberRequiredToStart\((.*)\)`
* `quest_setDayNumberRequiredToStart(id = "$1",$2)`

### new_day

* `tm.new_day\((.*))\`
* `new_day($1)`

### new_hour

* `tm.new_hour((.*))`
* `new_hour($1)`

### setFlags

* `flags\["(.*)"\] =(.*)`
* `setFlags("$1",$2)`

## What's Changed

* 55 convert pos to align by @DonRP in <https://github.com/DRincs-Productions/NQTR-System/pull/56>
* 57 convert all class in library py by @DonRP in <https://github.com/DRincs-Productions/NQTR-System/pull/58>

**Full Changelog**: <https://github.com/DRincs-Productions/NQTR-System/compare/v1.0.2...v1.0.3>

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
