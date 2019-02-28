autoscale: true
theme: Sketchnote, 6
footer: Six Feet Up -- AWS APIs with Boto3
slide-dividers: #

# AWS APIs with Boto3
![](https://c2.staticflickr.com/4/3364/3256733589_ae26c15e30_o.jpg)
## Python #vBrownBag

Calvin Hendryx-Parker
CTO, Co-Founder
Six Feet Up
<https://sixfeetup.com>

^ https://www.flickr.com/photos/ashleyrosex/3256733589

[.footer: ]

# [fit] Getting Going
![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Drag_racing_christmas_tree.jpg/2560px-Drag_racing_christmas_tree.jpg)

^ * Install Python
 * Install pipenv
 * Profit

# [fit] First Things First

```python
>>> import this
```

# Python 3
## Batteries Included
![](https://c1.staticflickr.com/5/4719/39646534151_86915b3651_k.jpg)

^ https://www.flickr.com/photos/pmillera4/39646534151

# pipenv
![](https://c2.staticflickr.com/4/3866/14578745869_cb22d2dbb7_k.jpg)

```
$ python3 -m pip install pipenv
```

^ https://www.flickr.com/photos/rexblog/14578745869


# Keeping Creds Safe

* LastPass
* `lpass` CLI
  * `$ brew install lastpass-cli --with-pinentry`
  * <https://github.com/lastpass/lastpass-cli>
* `lpass-env`
  * <ttps://github.com/luketurner/lpass-env>

^ GNU/Linux, Cygwin and Mac OS X

# aws-cli

^ A JMESPath query to use in filtering the response data.


# For a more colorful experience

```console
$ aws ec2 describe-instances | pygmentize -l json -O style=monokai
```

# Advanced JSON Filtering

http://stedolan.github.io/jq/

https://github.com/jmespath/jmespath.py


# aws-shell

<https://github.com/awslabs/aws-shell>

# Automating RDS

^ creating 10 serverless aurora instances with one command

# Automating Shell Commands

^ taking DMS table mappings and dumping structure

# Tracing CloudFront Logs

<https://github.com/sixfeetup/aws-log-tools>

# Resources

* https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
* https://docs.aws.amazon.com/cli/latest/reference/
* http://jmespath.org/

# **Questions?**
![](https://c1.staticflickr.com/1/55/185508448_7f247723f5_o.jpg)

### _<calvin@sixfeetup.com>_
### _[@calvinhp](https://twitter.com/calvinhp)_
