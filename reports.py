#! /usr/bin/env python
import functions, MySQLdb, dbconnections, reportQueries

#Obtener datos de DB
def get_db_data(connData, dbQuery):
	dbConn = MySQLdb.connect(connData['hostname'], 
				 connData['username'], 
				 connData['password'],
				 connData['database'])
	dbCursor = dbConn.cursor()
	dbCursor.execute(dbQuery)
	output = dbCursor.fetchall()
	dbCursor.close()
	return output

#Reporte de consumos y sesiones del radius
def radius_report01():
	currentData = get_db_data(dbconnections.connDataRadius, reportQueries.RADIUS_QUERY01)
	userList = []
	downList = []
	upList = []
	connectionTimeList = []
	resultDict = {}

	#making a set of users
	for usr, down, up, sessionTime in currentData:
		userList.append(usr)
		downList.append(down)
		upList.append(up)
		connectionTimeList.append(sessionTime)
	
	userSet = set(userList)
	
	resultDict['avgSessionDownload'] = functions.find_average(downList)
	resultDict['avgSessionUpload'] = functions.find_average(upList)
	resultDict['totalSessions'] = len(currentData)
	resultDict['totalUniqueUsers'] = len(userSet)
	resultDict['avgSessionTime'] = functions.find_average(connectionTimeList)
	resultDict['avgSessionNumber'] = (float(len(currentData)) / len(userSet))

	return resultDict
	
#Reporte de cantidad de dispositivos y tipos de dispositivos 
def device_report01():
	currentData = get_db_data(dbconnections.connDataHotspot, reportQueries.DEVICE_QUERY01)
	resultDict = {}
	userList = []
	devTypeList = []
	platformList = []
	platformVersionList = []
	for user, devType, platform, platformVer in currentData:
		userList.append(user)
		devTypeList.append(devType)
		platformList.append(platform)
		platformVersionList.append(platformVer)
		
	resultDict['totalDeviceQty'] = len(currentData)
	resultDict['devicePlatforms'] = set(platformList)
	resultDict['perPlatformStats'] = functions.find_occurrences(set(platformList), platformList)
	resultDict['avgDevicePerUser'] = float(len(currentData)) / len(set(userList))	
	return resultDict 





	
