# myfitnesspal-logs
Made this to print out logs for my nutritionist. Display is still not ideal but getting there. 

For each day in your range display date, totals for the day, then meals for the day, then notes if you had them.


### Example day
![Example day](https://dl.dropboxusercontent.com/u/36376877/mfp.png "Example day")


## Installation

```bash
pip install -r requirements.txt
```

Requires environment variables
```bash
export MFP_USERNAME='<your MFP username>'
export MFP_PASSWORD='<your MFP password>'
```

Also you need to go into script.py and change the start and end date to your own.

## Start project

```bash
python script.py
```

will output log to logs.txt by default. Can take a while.
