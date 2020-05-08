# BBCS-X-NoSQL

[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/<username>/BBCS-X-NoSQL)


[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/joelleoqiyi/BBCS-X-NoSQL)


Hello! Welcome to BuildingBloCS 2020 NoSQL Workshop!

For this workshop, we would be using:
- [MongoDB](https://www.mongodb.com) as a remote server database for storing our data
- [Gitpod](https://www.gitpod.io) as a online environment to run our code (as gitpod allows for some usage of terminal commands which we will be using later for importing our json file to the MongoDB server)

Before we begin, we would need to download MongoDB. In order to do this in Gitpod, we would need to configure  `.gitpod.dockerfile ` and `.gitpod.yml` files to use the dedicated MongoDB image built on top of gitpod/workspace-full.

Simply add the following line to .gitpod.dockerfile:

```
FROM gitpod/workspace-mongodb
```

Add the following line to .gitpod.yml:

```image:
  file: .gitpod.dockerfile
```
  
Then start the MongoDB server by running this in a Terminal or in a .gitpod.yml command:
mkdir -p /workspace/data && mongod --dbpath /workspace/data
Note: Storing MongoDB’s data inside /workspace ensures that it will get backed up and restored properly when you stop and restart a workspace, or share a snapshot.

Note: if you are doing this locally you can [download the MongoDB Community Edition here](https://docs.mongodb.com/manual/administration/install-community/)


---
