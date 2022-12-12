from fastapi import FastAPI, status
import pandas as pd
import json
from models import House
import csv

app = FastAPI()
MEDIA_ROOT = "us-cities-real-estate-sample-zenrows.csv"


@app.get("/")
async def test_1():
    return "Welcome to the real state App"


@app.get("/real_state/")
async def real_state():
    df = pd.read_csv(MEDIA_ROOT)
    data = df.to_json(orient = "index")
    data = json.loads(data)
    return data


@app.post("/insertData",status_code = 201)
async def insertData(item: House):
    with open(MEDIA_ROOT, "a", newline="") as csvfile:
        fielnames = [
            'zpid',
            'id',
            'providerListingId',
            'imgSrc',
            'hasImage',
            'detailUrl',
            'statusType',
            'statusText',
            'countryCurrency',
            'price',
            'unformattedPrice',
            'address',
            'addressStreet',
            'addressCity',
            'addressState',
            'addressZipcode',
            'isUndisclosedAddress',
            'beds',
            'baths',
            'area',
            'latitude',
            'longitude',
            'isZillowOwned',
            'variableDataType',
            'variableDataText',
            'variableDataIsFresh',
            'badgeInfo',
            'pgapt',
            'sgapt',
            'zestimate',
            'shouldShowZestimateAsPrice',
            'has3DModel',
            'hasVideo',
            'isHomeRec',
            'info2String',
            'info3String',
            'brokerName',
            'hasAdditionalAttributions',
            'isFeaturedListing',
            'list',
            'relaxed',
            'hasOpenHouse',
            'openHouseStartDate',
            'openHouseEndDate',
            'openHouseDescription',
            'info6String' 
        ]

        writer = csv.DictWriter(csvfile, fieldnames=fielnames)
        writer.writerow({
            'zpid':item.zpid,
            'id':item.id,
            'providerListingId':item.providerListingId,
            'imgSrc':item.imgSrc,
            'hasImage':item.hasImage,
            'detailUrl':item.detailUrl,
            'statusType':item.statusType,
            'statusText':item.statusText,
            'countryCurrency':item.countryCurrency,
            'price':item.price,
            'unformattedPrice':item.unformattedPrice,
            'address':item.address,
            'addressStreet':item.addressStreet,
            'addressCity':item.addressCity,
            'addressState':item.addressState,
            'addressZipcode':item.addressZipcode,
            'isUndisclosedAddress':item.isUndisclosedAddress,
            'beds':item.beds,
            'baths':item.baths,
            'area':item.area,
            'latitude':item.latitude,
            'longitude':item.longitude,
            'isZillowOwned':item.isZillowOwned,
            'variableDataType':item.variableDataType,
            'variableDataText':item.variableDataText,
            'variableDataIsFresh':item.variableDataIsFresh,
            'badgeInfo':item.badgeInfo,
            'pgapt':item.pgapt,
            'sgapt':item.sgapt,
            'zestimate':item.zestimate,
            'shouldShowZestimateAsPrice':item.shouldShowZestimateAsPrice,
            'has3DModel':item.has3DModel,
            'hasVideo':item.hasVideo,
            'isHomeRec':item.isHomeRec,
            'info2String':item.info2String,
            'info3String':item.info3String,
            'brokerName':item.brokerName,
            'hasAdditionalAttributions':item.hasAdditionalAttributions,
            'isFeaturedListing':item.isFeaturedListing,
            'list':item.list,
            'relaxed':item.relaxed,
            'hasOpenHouse':item.hasOpenHouse,
            'openHouseStartDate':item.openHouseStartDate,
            'openHouseEndDate':item.openHouseEndDate,
            'openHouseDescription':item.openHouseDescription,
            'info6String':item.info6String
        })
    return item


@app.put("/updateData/{item_id}", status_code= 200)
async def updateData(item_id: int, item: House):
    df = pd.read_csv(MEDIA_ROOT)
    df.loc[df.index[-1], "zpid"] = item.zpid
    df.loc[df.index[-1], "id"] = item.id
    df.loc[df.index[-1], "providerListingId"] = item.providerListingId
    df.loc[df.index[-1], "imgSrc"] = item.imgSrc
    df.loc[df.index[-1], "hasImage"] = item.hasImage
    df.loc[df.index[-1], "detailUrl"] = item.detailUrl
    df.loc[df.index[-1], "statusType"] = item.statusType
    df.loc[df.index[-1], "statusText"] = item.statusText
    df.loc[df.index[-1], "countryCurrency"] = item.countryCurrency
    df.loc[df.index[-1], "unformattedPrice"] = item.unformattedPrice
    df.loc[df.index[-1], "address"] = item.address
    df.loc[df.index[-1], "addressStreet"] = item.addressStreet
    df.loc[df.index[-1], "addressCity"] = item.addressCity
    df.loc[df.index[-1], "addressState"] = item.addressState
    df.loc[df.index[-1], "addressZipcode"] = item.addressZipcode
    df.loc[df.index[-1], "isUndisclosedAddress"] = item.isUndisclosedAddress
    df.loc[df.index[-1], "latitude"] = item.latitude
    df.loc[df.index[-1], "longitude"] = item.longitude
    df.loc[df.index[-1], "isZillowOwned"] = item.isZillowOwned
    df.loc[df.index[-1], "variableDataType"] = item.variableDataType
    df.loc[df.index[-1], "variableDataText"] = item.variableDataText
    df.loc[df.index[-1], "variableDataIsFresh"] = item.variableDataIsFresh
    df.loc[df.index[-1], "badgeInfo"] = item.badgeInfo
    df.loc[df.index[-1], "pgapt"] = item.pgapt
    df.loc[df.index[-1], "sgapt"] = item.sgapt
    df.loc[df.index[-1], "zestimate"] = item.zestimate
    df.loc[df.index[-1], "shouldShowZestimateAsPrice"] = item.shouldShowZestimateAsPrice
    df.loc[df.index[-1], "has3DModel"] = item.has3DModel
    df.loc[df.index[-1], "hasVideo"] = item.hasVideo
    df.loc[df.index[-1], "isHomeRec"] = item.isHomeRec
    df.loc[df.index[-1], "info2String"] = item.info2String
    df.loc[df.index[-1], "info3String"] = item.info3String
    df.loc[df.index[-1], "brokerName"] = item.brokerName
    df.loc[df.index[-1], "hasAdditionalAttributions"] = item.hasAdditionalAttributions
    df.loc[df.index[-1], "isFeaturedListing"] = item.isFeaturedListing
    df.loc[df.index[-1], "relaxed"] = item.relaxed
    df.loc[df.index[-1], "hasOpenHouse"] = item.hasOpenHouse
    df.loc[df.index[-1], "openHouseStartDate"] = item.openHouseStartDate
    df.loc[df.index[-1], "openHouseEndDate"] = item.openHouseEndDate
    df.loc[df.index[-1], "openHouseDescription"] = item.openHouseDescription
    df.loc[df.index[-1], "info6String"] = item.info6String
    df.to_csv(MEDIA_ROOT, index = False)
    return {"item_id": item_id, **item.dict()}


@app.delete("/deleteData/{item_id}", status_code = 204)
async def deleteData(item_id: int):
    df = pd.read_csv(MEDIA_ROOT)
    df.drop(df.index[-1], inplace=True)
    df.to_csv(MEDIA_ROOT, index= False)
    return {"item_id": item_id, "msg": "Deleted"}

















