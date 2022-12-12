from pydantic import BaseModel

class House(BaseModel):
    zpid: int
    id: int
    providerListingId: str
    imgSrc: str
    hasImage: str
    detailUrl: str
    statusType: str
    statusText: str
    countryCurrency: str
    price: float
    unformattedPrice: int
    address: str
    addressStreet: str
    addressCity: str
    addressState: str
    addressZipcode: int
    isUndisclosedAddress: bool
    beds: str
    baths: str
    area: str
    latitude: float
    longitude: float
    isZillowOwned: bool
    variableDataType: str
    variableDataText: str
    variableDataIsFresh: str
    badgeInfo: str
    pgapt: str
    sgapt: str
    zestimate: str
    shouldShowZestimateAsPrice: bool
    has3DModel: bool
    hasVideo: bool
    isHomeRec: str
    info2String: str
    info3String: str
    brokerName: str
    hasAdditionalAttributions: bool
    isFeaturedListing: bool
    list: bool
    relaxed: str
    hasOpenHouse: str
    openHouseStartDate: str
    openHouseEndDate: str
    openHouseDescription: str
    info6String: str
