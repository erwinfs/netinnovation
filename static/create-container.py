#One off Python script to create object store container
import swiftclient

auth_url = "https://lon-identity.open.softlayer.com"
project = "object_storage_1b885008_464c_43d5_9dc1_fbe603a79525"
project_id =  "4a9ca921887640639289c818531bd517"
region= "london"
user_id= "e1a1ab03073d4fa3ba8ee2d68be42f5a"
username= "admin_5127cf3f164c4012f377599cb658584de59aca5c"
password= "I!=dt-BPf3.^6fCg"
domainId= "6543fe3416ae4d13b26c96ac415e0535"
domainName= "1390751"
role= "admin"


conn = swiftclient.Connection(key=password,
	authurl=auth_url,
	auth_version='3',
	os_options={"project_id= project_id,
				"user_id= user_id,
				"region_name= region_name})

cont_name = "works"
conn.put_container(cont_name)
