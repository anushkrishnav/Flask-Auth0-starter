# Flask + API + Auth0 The Complete Starter

## Please refer to get a better idea of the inner working of the app
- [Flask](https://auth0.com/docs/quickstart/webapp/python/01-login#display-user-information)
- [Flask API: Authorization](https://auth0.com/docs/quickstart/backend/python)



## What is Auth0?

Auth0 helps you to easily:

- implement authentication with multiple identity providers, including social (e.g., Google, Facebook, Microsoft, LinkedIn, GitHub, Twitter, etc), or enterprise (e.g., Windows Azure AD, Google Apps, Active Directory, ADFS, SAML, etc.)
- log in users with username/password databases, passwordless, or multi-factor authentication
- link multiple user accounts together
- generate signed JSON Web Tokens to authorize your API calls and flow the user identity securely
- access demographics and analytics detailing how, when, and where users are logging in
- enrich user profiles from other data sources using customizable JavaScript rules

[Why Auth0?](https://auth0.com/why-auth0)

## Create a free account in Auth0

1. Go to [Auth0](https://auth0.com) and click Sign Up.
2. Use Google, GitHub or Microsoft Account to login.

## Getting the app started

In order to run the example you need to have python and pip installed.

You also need to set your Auth0 Domain and the API's audience as environment variables with the following names respectively: AUTH0_DOMAIN and API_IDENTIFIER, which is the audience of your API. You can find an example in the env.example file.

For that, if you just create a file named .env in the directory and set the values like the following, the app will just work 


Once you've set those 2 environment variables:

1. Install the needed dependencies with `pip install -r requirements.txt`
2. Start the server with ``
3. Try calling [http://localhost:5000/api/public](http://localhost:5000/api/public)

## Testing the API
You can then try to do a GET to http://localhost:5000/api/private 
- which will will take you to Signup if you don't send an access token signed with RS256 with the appropriate issuer and audience in the Authorization header.
- if you have log in / logged in then you can see the message


You can also try to do a GET to http://localhost:5000/api/private-scoped which will throw an error if you don't send an access token with the scope read:messages signed with RS256 with the appropriate issuer and audience in the Authorization header.


## Issue Reporting

If you have found a bug or if you have a feature request, please report them at this repository issues section. Please do not report security vulnerabilities on the public GitHub issue tracker. The [Responsible Disclosure Program](https://auth0.com/whitehat) details the procedure for disclosing security issues.


## License

This project is licensed under the MIT license. See the [LICENSE](LICENSE) file for more info.
