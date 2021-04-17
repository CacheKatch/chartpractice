# chartpractice

The objective of this app is to render a chart with open, high, low and close of a list of stocks.

Although, the process works local, it times out (error H12) when deployed in heroku.

This is the Heroku app link: https://shielded-mesa-08364.herokuapp.com/

## Potential Solution:

Add a worker python file that would run in separate dyno. This is pending to investigate.

## Unexpected Errors on Requirements file:

Several installed packages had a link to folder instead of the version number when performed the command:
```shell 
pip freeze > requirements.txt

```
After investigating potential solutions for this, found that the following command generates the list of packages with version number without links:

```shell
pip list --format=freeze > requirements.txt

```
## To-do list:

- [x] Plot a list of stocks with a line chart in Matplotlib
- [  ] Deploy a chart in Heroku 
- [ ] Plot a candlestick chart 