# IdentityServer4_Token_Access_by_Python 

There are several ways for many programming languages like C# and Java to access a vaild token when request a server using IDS4.
However, few information could be found by using Python to get an access_token.

For this reason,
this git gives an solution to whom wanna using Python to do webscrape on those servers.



Before begining,
you should know something essential for the request.
## The things are:


* 'client_id'
* 'client_secret'
* 'token_url'
* '{'grant_type': 
*  'username': 
*  'password': 
*  'scope':  }'




## How get those information above
You should find the target website like https://ids.xxx.com/connect/authorize by yourself, open the website and you will find some information contains 'token_url' which your need to request directly. e.g. https://ids.xxx.com/connect/token; "grant_types_supported" as many choices for 'grand_type', normally we choose 'password', then we enter our 'username' and 'password' ;After, "scopes_supported" as 'scope', 'webapi' is the answer. 

The remaining 4 inputs as I know(id, secret, username, password), might need the server host provides to you. The host has the full right to give your the access account.

However, I known that in most situations, the Python user was not working in the same environment with the server host. So they could not get the these information. This git only provides the solution for those who known the information.

An optional solution might be applying to be a developer like Google Developers. Once you finished to be a developer, you will achieve the cliend_id and client_secret for getting the access_token. The target website would regconize you as an app for connecting.


## How to use
Once you got all the information you need, input the information in '(def___init___)', and then you could just import the pyfile to use. The file would check for you every time your use. The refresh time can be defined by yourself if you know the token validation time.


