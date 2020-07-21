class Company:
    def __init__(self, name, region, status, type):
        self.name = name
        self.region = region
        self.status = status
        self.type = type

    def addExtraData(self, data):
        self.isExistsData = 1
        self.shortDescription = data['short_description']
        self.homepageURL = data['homepage_url']
        self.profileImageURL = data['profile_image_url']
        self.city = data['city_name']

    def notFound(self):
        self.isExistsData = 0
        self.shortDescription = ''
        self.homepageURL = ''
        self.profileImageURL = ''
        self.city = ''

    def getData(self):
        return [
            self.name, self.region, self.status, self.type, self.isExistsData,
            self.shortDescription, self.homepageURL, self.profileImageURL, self.city
        ]