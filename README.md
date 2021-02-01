
# Irelia·py

A library made to communicate with League of Legends Client API with **python** 🐍.

# Usage

```request(method,  path, data='', query='')```

##
>  Creating Solo/Duo ranked lobby

```request("post",  "/lol-lobby/v2/lobby",  "","{"queueId":420}")```
###
>Getting the summoner's name.

```request("get",  "/lol-chat/v1/me")```

### Example:
> Changing summoner icon.
###

```python from ireliapy import  *

def  LCU():

	data =  {'profileIconId':  29}
	response =  request('put',  '/lol-summoner/v1/current-summoner/icon', data)

	print(response.status_code)
	print(response.json())

LCU()
```
##
**Irelia·py** isn’t endorsed by Riot Games and doesn’t reflect the views or opinions of Riot Games or anyone officially involved in producing or managing League of Legends. League of Legends and Riot Games are trademarks or registered trademarks of Riot Games, Inc. League of Legends © Riot Games, Inc.
