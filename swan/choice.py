# delivery type

STANDARD = 'STD'
EXPRESS = 'EXP'

DELIVERY_CHOICES = [
    (STANDARD, 'Standard'),
    (EXPRESS, 'Express'),
]


#service type
INTERNATIONAL_MFG_WARRANTY = 'IMW'
NO_WARRANTY = 'NW'
GUARANTEE = 'GN'

WARRANTY_CHOICES = [
    (INTERNATIONAL_MFG_WARRANTY, 'International manufacturer warranty'),
    (NO_WARRANTY, 'No Warranty'),
    (GUARANTEE, 'Guarantee'),
]

#orderstatus
READY_TO_SHIP = 'RTS'
SHIPPED = 'SH'
DELIVERED = 'DL'
CANCELLED = 'CN'
RETURNED_FAILED_DELIVERY = 'RFD'

ORDER_STATUS_CHOICES = [
    (READY_TO_SHIP, 'Ready to ship'),
    (SHIPPED, 'Shipped'),
    (DELIVERED, 'Delivered'),
    (CANCELLED, 'Cancelled'),
    (RETURNED_FAILED_DELIVERY, 'Returned Failed Delivery'),
]

# review - Star choice
ONE_STAR = '1'
TWO_STAR = '2'
THREE_STAR = '3'
FOUR_STAR = '4'
FIVE_STAR = '5'

STAR_CHOICES = [
    (ONE_STAR, '*'),
    (TWO_STAR, '**'),
    (THREE_STAR, '***'),
    (FOUR_STAR, '****'),
    (FIVE_STAR, '*****'),
]
