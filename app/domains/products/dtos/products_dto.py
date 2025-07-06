class ProductsDTO:
    def __init__(
        self,
        product_id=None,
        brand_id=None,
        name=None,
        description=None,
        image=None,
        weight=None,
        volume=None,
        units=None,
        length=None,
        model=None
    ):
        if model is not None:
            product_id = model.id
            brand_id = model.brand_id
            name = model.name
            description = model.description
            image = model.image
            weight = model.weight
            volume = model.volume
            units = model.units
            length = model.length

        self.id = product_id
        self.brand_id = brand_id
        self.name = name
        self.description = description
        self.image = image
        self.weight = weight
        self.volume = volume
        self.units = units
        self.length = length

    def toDict(self):
        return {
            "product_id":  self.id,
            "brand_id":    self.brand_id,
            "name":        self.name,
            "description": self.description,
            "image":       self.image,
            "weight":      self.weight,
            "volume":      self.volume,
            "units":       self.units,
            "length":      self.length
        }