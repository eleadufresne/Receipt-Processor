receipt_schema = {
    "type": "object",
    "required": [
        "retailer",
        "purchaseDate",
        "purchaseTime",
        "items",
        "total"
    ],
    "properties": {
        "retailer": {
            "description": "The name of the retailer or store the receipt is from.",
            "type": "string",
            "pattern": "^[\\w\\s\\-&]+$",
            "example": "M&M Corner Market"
        },
        "purchaseDate": {
            "description": "The date of the purchase printed on the receipt.",
            "type": "string",
            "format": "date",
            "example": "2022-01-01"
        },
        "purchaseTime": {
            "description": "The time of the purchase printed on the receipt. 24-hour time expected.",
            "type": "string",
            "format": "time",
            "example": "13:01"
        },
        "items": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "required": [
                    "shortDescription",
                    "price"
                ],
                "properties": {
                    "shortDescription": {
                        "description": "The Short Product Description for the item.",
                        "type": "string",
                        "pattern": "^[\\w\\s\\-]+$",
                        "example": "Mountain Dew 12PK"
                    },
                    "price": {
                        "description": "The total price payed for this item.",
                        "type": "string",
                        "pattern": "^\\d+\\.\\d{2}$",
                        "example": "6.49"
                    }
                }
            }
        },
        "total": {
            "description": "The total amount paid on the receipt.",
            "type": "string",
            "pattern": "^\\d+\\.\\d{2}$",
            "example": "6.49"
        }
    }
}