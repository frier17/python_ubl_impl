"""
Business process package defines routine services provided by a business.
The listed processes are used to manage the activities associated with a
given business service.
The design implemented of all processes are derived from the definition of
business service by Aniefiok Friday:
"Every business service consists of activities performed at a cost and
requires a feedback (proof of transaction) to participants or parties involved"

Implement the business processes such as procurement, call to tender etc.
defined in the UBL 2.1
Section 2.3, “Tendering”
Section 2.4, “Catalogue”
Section 2.5, “Quotation”
Section 2.6, “Ordering”
Section 2.7, “Fulfilment”
Section 2.8, “Billing”
Section 2.9, “Freight Billing”
Section 2.10, “Utility Billing”
Section 2.11, “Payment Notification”
Section 2.13, “Collaborative Planning, Forecasting, and Replenishment”
Section 2.14, “Vendor Managed Inventory”
Section 2.15, “International Freight Management”
Section 2.18, “Intermodal Freight Management”
Section 2.16, “Freight Status Reporting”
Section 2.17, “Certification of Origin of Goods”
adopted from http://docs.oasis-open.org/ubl/os-UBL-2.1/UBL-2.1.html
The named business operations are provided as corresponding service module
mixins. These mixins would define the features available in defined services.

Mixins to include:
1	TenderingMixin
2	CatalogueMixin
3	QuotationMixin
4	OrderingMixin
5	FulfilmentMixin
6	BillingMixin
7	FreightBillingMixin
8	UtilityBillingMixin
9	PaymentNotificationMixin
10	CollaborativePlanningForecastingandReplenishmentMixin
11	VendorManagedInventoryMixin
12	InternationalFreightManagementMixin
13	IntermodalFreightManagementMixin
14	FreightStatusReportingMixin
15	CertificationofOriginofGoodsMixin

The derived services can have methods which takes in tasks as a keyword
argument. The task are callable object provided by the developer to meet
requirements of target processes. Example, the BillingService may provide a
method: BillingService.receive_statement(*args, **kwargs) which is used to
store an account statement to a database. The actual implementation is not
defined in the derived BillingService but can be passed as a parameter to
the method, receive_statement and then executed from the wrapper method.

Hence we obtain:

# Process account statement for client

 BillingService.receive_statement(task=(pre_process_statement,
 post_process),documents, conditions, flags)

 Which internally runs thus:

 for task in tasks:
    task(*args, **kwargs)

Where arguments could be documents, conditions, flags, and other passed in
parameters via decorators, global variables etc.

can be executed by process
"""
from enum import IntFlag, unique, Enum
from collections import namedtuple


@unique
class ProcessRegistry(IntFlag):
    ANY_COLLABORATION = 2
    BILLING = 3
    CATALOGUE = 5
    CERTIFICATE_OF_ORIGIN_OF_GOODS = 7
    CHANGES_TO_THE_ARTICLE_CATALOGUE = 11
    CHANGES_TO_THE_ITEM_CATALOGUE = 13
    COLLABORATIVE_PLANNING = 17
    CREATE_CATALOGUE = 19
    CYCLIC_REPLENISHMENT_PROGRAM = 23
    DELETE_CATALOGUE = 29
    FORECASTING = 31
    FREIGHT_BILLING = 37
    FREIGHT_MANAGEMENT = 41
    FREIGHT_STATUS_REPORTING = 43
    FULFILLMENT = 47
    FULFILMENT_WITH_DESPATCH_ADVICE = 53
    FULFILMENT_WITH_RECEIPT_ADVICE = 59
    INITIAL_STOCKING_OF_THE_AREA_BY_PRODUCER = 61
    INTERMODAL_FREIGHT_MANAGEMENT = 67
    ORDERING = 71
    PAYMENT_NOTIFICATION = 73
    PERMANENT_REPLENISHMENT = 79
    PRICE_ADJUSTMENTS = 83
    QUOTATION = 89
    REPLENISHMENT = 97
    TENDERING = 101
    TRANSFER_OF_BASE_ITEM_CATALOGUE = 103
    UPDATE_CATALOGUE_ITEM_SPECIFICATION = 107
    UPDATE_CATALOGUE_PRICING = 109
    UTILITY_BILLING = 113
    VENDOR_INVENTORY = 127
    INITIAL_STOCKING_OF_THE_AREA_BY_RETAILER = 131
    PUNCHOUT_SOURCING = 137

bp = namedtuple('BusinessProcessEnum', ('process', 'id', 'rank'))


class ContractingInformation(Enum):
    PREPARE_PRIOR_NOTICE = bp(ProcessRegistry.TENDERING, 2, 3)
    PUBLISH_IN_BUYER_PROFILE = bp(ProcessRegistry.TENDERING, 3, 9)
    PREPARE_SIMPLIFIED_NOTICE = bp(ProcessRegistry.TENDERING, 5, 15)
    PUBLISH_SIMPLIFIED_NOTICE = bp(ProcessRegistry.TENDERING, 7, 21)
    PUBLISH_PRIOR_INFORMATION_NOTICE = bp(ProcessRegistry.TENDERING, 11, 33)
    VALIDATE_PRIOR_INFORMATION_NOTICE = bp(ProcessRegistry.TENDERING, 13, 39)


class ContractingInformationNotification(Enum):
    PREPARE_CONTRACT_NOTICE = bp(ProcessRegistry.TENDERING, 17, 51)
    PUBLISH_IN_BUYER_PROFILE = bp(ProcessRegistry.TENDERING, 19, 57)
    PUBLISH_CONTRACT_NOTICE = bp(ProcessRegistry.TENDERING, 23, 69)
    VALIDATE_CONTRACT_NOTICE = bp(ProcessRegistry.TENDERING, 29, 87)


class InvitationToTender(Enum):
    PREPARE_CALL_FOR_TENDERS = bp(ProcessRegistry.TENDERING, 31, 93)
    SUBMIT_INVITATION_TO_TENDER_ = bp(ProcessRegistry.TENDERING, 37, 111)
    RECEIVE_INVITATION_TO_TENDER = bp(ProcessRegistry.TENDERING, 41, 123)
    PROCESS_CALL_FOR_TENDER = bp(ProcessRegistry.TENDERING, 43, 129)


class SubmissionOfQualification(Enum):
    PREPARE_QUALIFICATION_DOCUMENT = bp(ProcessRegistry.TENDERING, 47, 141)
    SUBMIT_QUALIFICATION_DOCUMENT = bp(ProcessRegistry.TENDERING, 53, 159)
    RECEIVE_RESULT = bp(ProcessRegistry.TENDERING, 59, 177)
    EVALUATE_QUALIFICATION_DOCUMENT = bp(ProcessRegistry.TENDERING, 61, 183)
    SUBMIT_QUALIFICATION_RESULT = bp(ProcessRegistry.TENDERING, 67, 201)


class SubmissionOfTender(Enum):
    PREPARE_TENDER_DOCUMENTS = bp(ProcessRegistry.TENDERING, 71, 213)
    SUBMIT_TENDER_DOCUMENTS = bp(ProcessRegistry.TENDERING, 73, 219)
    RECEIVE_RECEIPT = bp(ProcessRegistry.TENDERING, 79, 237)
    SUBMIT_TENDER_RECEIPT = bp(ProcessRegistry.TENDERING, 83, 249)
    RECEIVE_TENDER_DOCUMENTS = bp(ProcessRegistry.TENDERING, 89, 267)


class AwardPublication(Enum):
    PREPARE_CONTRACT_AWARD_AND_NOTICE = bp(ProcessRegistry.TENDERING, 97, 291)
    SUBMIT_CONTRACT_AWARD_NOTICE = bp(ProcessRegistry.TENDERING, 101, 303)
    VALIDATE_CONTRACT_AWARD_NOTICE = bp(ProcessRegistry.TENDERING, 103, 309)
    PUBLISH_CONTRACT_AWARD_NOTICE = bp(ProcessRegistry.TENDERING, 107, 321)


class GuaranteeDeposit(Enum):
    GET_GUARANTEE_FROM_FINANCIAL_INSTITUTION = bp(ProcessRegistry.TENDERING,
                                                  109, 327)
    SUBMIT_CERTIFICATE = bp(ProcessRegistry.TENDERING, 113, 339)
    RECEIVE_GUARANTEE_CERTIFICATE = bp(ProcessRegistry.TENDERING, 127, 381)


class CreateCatalogue(Enum):
    REQUEST_CATALOGUE = bp(ProcessRegistry.CATALOGUE, 131, 393)
    RESPOND_TO_REQUEST = bp(ProcessRegistry.CATALOGUE, 137, 411)
    SEND_REJECTION = bp(ProcessRegistry.CATALOGUE, 139, 417)
    PREPARE_CATALOGUE_INFORMATION = bp(ProcessRegistry.CATALOGUE, 149, 447)
    SEND_ACCEPTANCE_RESPONSE = bp(ProcessRegistry.CATALOGUE, 151, 453)
    PRODUCE_CATALOGUE = bp(ProcessRegistry.CATALOGUE, 157, 471)
    DISTRIBUTE_CATALOGUE = bp(ProcessRegistry.CATALOGUE, 163, 489)
    RECEIVE_CATALOGUE = bp(ProcessRegistry.CATALOGUE, 167, 501)
    ACKNOWLEDGE_ACCEPTANCE = bp(ProcessRegistry.CATALOGUE, 173, 519)
    ACCEPT_CATALOGUE = bp(ProcessRegistry.CATALOGUE, 179, 537)


class UpdateItemSpecification(Enum):
    REQUEST_CATALOGUE_UPDATE = bp(ProcessRegistry.CATALOGUE, 181, 543)
    SEND_REJECTION = bp(ProcessRegistry.CATALOGUE, 191, 573)
    SEND_ACCEPTANCE_RESPONSE = bp(ProcessRegistry.CATALOGUE, 193, 579)
    PREPARE_CATALOGUE_ITEM_UPDATE_INFORMATION = bp(ProcessRegistry.CATALOGUE,
                                                   197, 591)
    DISTRIBUTE_ITEM_NOTIFICATIONS = bp(ProcessRegistry.CATALOGUE, 199, 597)
    RECEIVE_ITEM_UPDATE = bp(ProcessRegistry.CATALOGUE, 211, 633)
    ACKNOWLEDGE_ACCEPTANCE = bp(ProcessRegistry.CATALOGUE, 223, 669)
    ACTIVATE_CHANGES = bp(ProcessRegistry.CATALOGUE, 227, 681)
    APPLY_CHANGES = bp(ProcessRegistry.CATALOGUE, 229, 687)


class UpdateCataloguePrice(Enum):
    REQUEST_CATALOGUE_UPDATE = bp(ProcessRegistry.CATALOGUE, 233, 699)
    SEND_REJECTION = bp(ProcessRegistry.CATALOGUE, 239, 717)
    SEND_ACCEPTANCE_RESPONSE = bp(ProcessRegistry.CATALOGUE, 241, 723)
    PREPARE_CATALOGUE_PRICING_UPDATE_INFORMATION = bp(
        ProcessRegistry.CATALOGUE, 251, 753)
    DISTRIBUTE_PRICING_MODIFICATIONS = bp(ProcessRegistry.CATALOGUE, 257, 771)
    RECEIVE_PRICING_UPDATE = bp(ProcessRegistry.CATALOGUE, 263, 789)
    ACKNOWLEDGE_ACCEPTANCE = bp(ProcessRegistry.CATALOGUE, 269, 807)
    ACTIVATE_CHANGES = bp(ProcessRegistry.CATALOGUE, 271, 813)
    APPLY_CHANGES = bp(ProcessRegistry.CATALOGUE, 277, 831)


class DeleteCatalogue(Enum):
    IDENTIFY_CATALOGUE = bp(ProcessRegistry.CATALOGUE, 281, 843)
    NOTIFY_OF_CATALOGUE_DELETION = bp(ProcessRegistry.CATALOGUE, 283, 849)
    CANCEL_CATALOGUE = bp(ProcessRegistry.CATALOGUE, 293, 879)
    ACKNOWLEDGE_CANCELLATION = bp(ProcessRegistry.CATALOGUE, 307, 921)
    DELETE_CATALOGUE = bp(ProcessRegistry.CATALOGUE, 311, 933)


class PunchoutSourcing(Enum):
    INITIATE_A_PUNCHOUT_SESSION = bp(ProcessRegistry.PUNCHOUT_SOURCING, 313,
                                     939)
    BUILD_SHOPPING_BASKET = bp(ProcessRegistry.PUNCHOUT_SOURCING, 317, 951)
    SEND_SHOPPING_BASKET = bp(ProcessRegistry.PUNCHOUT_SOURCING, 331, 993)
    RECEIVE_QUOTATION = bp(ProcessRegistry.PUNCHOUT_SOURCING, 337, 1011)


class QuotationProcess(Enum):
    SEND_REQUEST_FOR_QUOTATION = bp(ProcessRegistry.QUOTATION, 347, 1041)
    RECEIVE_REQUEST_FOR_QUOTATION = bp(ProcessRegistry.QUOTATION, 349, 1047)
    SEND_QUOTATION = bp(ProcessRegistry.QUOTATION, 353, 1059)
    RECEIVE_QUOTATION = bp(ProcessRegistry.QUOTATION, 359, 1077)


class OrderingProcess(Enum):
    PLACE_ORDER = bp(ProcessRegistry.ORDERING, 367, 1101)
    RECEIVE_ORDER = bp(ProcessRegistry.ORDERING, 373, 1119)
    REJECT_ORDER = bp(ProcessRegistry.ORDERING, 379, 1137)
    ADD_DETAIL = bp(ProcessRegistry.ORDERING, 383, 1149)
    ACCEPT_ORDER = bp(ProcessRegistry.ORDERING, 389, 1167)
    RECEIVE_RESPONSE = bp(ProcessRegistry.ORDERING, 397, 1191)
    CANCEL_ORDER = bp(ProcessRegistry.ORDERING, 401, 1203)
    CHANGE_ORDER = bp(ProcessRegistry.ORDERING, 409, 1227)


class FulfilmentWithDespatchAdvice(Enum):
    ACCEPT_ORDER = bp(ProcessRegistry.FULFILLMENT, 421, 1263)
    ACCEPT_ITEMS = bp(ProcessRegistry.FULFILLMENT, 431, 1293)
    SEND_RECEIPT_ADVICE = bp(ProcessRegistry.FULFILLMENT, 433, 1299)
    RECEIVE_RECEIPT_ADVICE = bp(ProcessRegistry.FULFILLMENT, 439, 1317)
    ADJUST_SUPPLY_STATUS = bp(ProcessRegistry.FULFILLMENT, 443, 1329)
    CANCEL_DESPATCH = bp(ProcessRegistry.FULFILLMENT, 449, 1347)
    RECEIVE_FULFILLMENT_CANCELLATION = bp(ProcessRegistry.FULFILLMENT, 457,
                                          1371)
    CHECK_STATUS_OF_ITEMS = bp(ProcessRegistry.FULFILLMENT, 461, 1383)
    RECEIVE_ORDER_ITEMS = bp(ProcessRegistry.FULFILLMENT, 463, 1389)
    SEND_DESPATCH_ADVICE = bp(ProcessRegistry.FULFILLMENT, 467, 1401)
    RECEIVE_DESPATCH_ADVICE = bp(ProcessRegistry.FULFILLMENT, 479, 1437)


class FulillmentWithReceipt(Enum):
    ACCEPT_ITEMS = bp(ProcessRegistry.FULFILLMENT, 487, 1461)
    ADJUST_ORDER = bp(ProcessRegistry.FULFILLMENT, 491, 1473)
    SEND_ORDER_CANCELLATION = bp(ProcessRegistry.FULFILLMENT, 499, 1497)
    ADVISE_BUYER_OF_STATUS = bp(ProcessRegistry.FULFILLMENT, 503, 1509)
    CHECK_STATUS_OF_ITEMS = bp(ProcessRegistry.FULFILLMENT, 509, 1527)
    RECEIVE_ORDER_ITEMS = bp(ProcessRegistry.FULFILLMENT, 521, 1563)
    SEND_RECEIPT_ADVICE = bp(ProcessRegistry.FULFILLMENT, 523, 1569)
    CANCEL_RECEIPT_NOTIFICATION = bp(ProcessRegistry.FULFILLMENT, 541, 1623)
    RECEIVE_RECEIPT_ADVICE = bp(ProcessRegistry.FULFILLMENT, 547, 1641)
    RECEIVE_FULFILLMENT_CANCELLATION = bp(ProcessRegistry.FULFILLMENT, 557,
                                          1671)
    ADJUST_SUPPLY_STATUS = bp(ProcessRegistry.FULFILLMENT, 563, 1689)
    CANCEL_ORDER = bp(ProcessRegistry.FULFILLMENT, 569, 1707)
    CHANGE_ORDER = bp(ProcessRegistry.FULFILLMENT, 571, 1713)
    

class BillingWithCreditNote(Enum):
    RECEIVE_INVOICE = bp(ProcessRegistry.BILLING, 577, 1731)
    SEND_ACCOUNT_RESPONSE = bp(ProcessRegistry.BILLING, 587, 1761)
    RECEIVE_CREDIT_NOTE = bp(ProcessRegistry.BILLING, 593, 1779)
    RECEIVE_ACCOUNT_RESPONSE = bp(ProcessRegistry.BILLING, 599, 1797)
    RAISE_CREDIT_NOTE = bp(ProcessRegistry.BILLING, 601, 1803)
    RAISE_INVOICE = bp(ProcessRegistry.BILLING, 607, 1821)
    

class BillingWithDebitNote(Enum):
    RECEIVE_INVOICE = bp(ProcessRegistry.BILLING, 613, 1839)
    RAISE_INVOICE = bp(ProcessRegistry.BILLING, 617, 1851)
    SEND_ACCOUNT_RESPONSE = bp(ProcessRegistry.BILLING, 619, 1857)
    RAISE_DEBIT_NOTE = bp(ProcessRegistry.BILLING, 631, 1893)
    RECEIVE_DEBIT_NOTE = bp(ProcessRegistry.BILLING, 641, 1923)
    RECEIVE_ACCOUNT_RESPONSE = bp(ProcessRegistry.BILLING, 643, 1929)
    

class SelfBillingWithCreditNote(Enum):
    RAISE_SELF_BILLED_INVOICE = bp(ProcessRegistry.BILLING, 647, 1941)
    RECEIVE_ACCOUNT_RESPONSE = bp(ProcessRegistry.BILLING, 653, 1959)
    RECEIVE_CREDIT_NOTE = bp(ProcessRegistry.BILLING, 659, 1977)
    RAISE_CREDIT_NOTE = bp(ProcessRegistry.BILLING, 661, 1983)
    SEND_ACCOUNT_RESPONSE = bp(ProcessRegistry.BILLING, 673, 2019)
    RECEIVE_SELF_BILLED_INVOICE = bp(ProcessRegistry.BILLING, 677, 2031)
    
    
class SelfBillingWithSelfCredit(Enum):
    RAISE_SELF_BILLED_INVOICE = bp(ProcessRegistry.BILLING, 683, 2049)
    RECEIVE_ACCOUNT_RESPONSE = bp(ProcessRegistry.BILLING, 691, 2073)
    RAISE_SELF_BILLED_CREDIT_NOTE = bp(ProcessRegistry.BILLING, 701, 2103)
    RECEIVE_SELF_BILLED_CREDIT_NOTE = bp(ProcessRegistry.BILLING, 709, 2127)
    SEND_ACCOUNT_RESPONSE = bp(ProcessRegistry.BILLING, 719, 2157)
    RECEIVE_SELF_BILLED_INVOICE = bp(ProcessRegistry.BILLING, 727, 2181)
    

class ReminderForPayment(Enum):
    RECEIVE_REMINDER = bp(ProcessRegistry.PAYMENT_NOTIFICATION, 733, 2199)
    REQUEST_PAYMENT_OF_ACCOUNT = bp(ProcessRegistry.PAYMENT_NOTIFICATION,
                                    739, 2217)
    

class FreightBilling(Enum):
    RECEIVE_FREIGHT_INVOICE = bp(ProcessRegistry.FREIGHT_BILLING, 743, 2229)
    SEND_FREIGHT_INVOICE_TO_COSIGNOR = bp(ProcessRegistry.FREIGHT_BILLING,
                                          751, 2253)
    

class UtilityBilling(Enum):
    RECEIVE_INVOICE = bp(ProcessRegistry.UTILITY_BILLING, 757, 2271)
    RECEIVE_UTILITY_STATEMENT = bp(ProcessRegistry.UTILITY_BILLING, 761, 2283)
    SEND_ACCOUNT_RESPONSE = bp(ProcessRegistry.UTILITY_BILLING, 769, 2307)
    RECEIVE_ACCOUNT_RESPONSE = bp(ProcessRegistry.UTILITY_BILLING, 773, 2319)
    REPORT_USAGE = bp(ProcessRegistry.UTILITY_BILLING, 787, 2361)
    RAISE_INVOICE = bp(ProcessRegistry.UTILITY_BILLING, 797, 2391)


class PaymentNotification(Enum):
    AUTHORIZE_PAYMENT = bp(ProcessRegistry.PAYMENT_NOTIFICATION, 809, 2427)
    NOTIFY_OF_PAYMENT = bp(ProcessRegistry.PAYMENT_NOTIFICATION, 811, 2433)
    RECEIVE_ADVICE = bp(ProcessRegistry.PAYMENT_NOTIFICATION, 821, 2463)
    NOTIFY_PAYEE = bp(ProcessRegistry.PAYMENT_NOTIFICATION, 823, 2469)
    

class PaymentStatement(Enum):
    RECEIVE_STATEMENT = bp(ProcessRegistry.BILLING, 827, 2481)
    GUARANTEE_STATEMENT = bp(ProcessRegistry.BILLING, 829, 2487)
    

class CollaborativeRelationship(Enum):
    RECEIVE_EXCEPTION_CRITERIA = bp(ProcessRegistry.COLLABORATIVE_PLANNING,
                                    839, 2517)
    REVISE_EXCEPTION = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 853, 2559)
    SEND_REVISION = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 857, 2571)
    SEND_EXCEPTION_CRITERIA = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 859,
                                 2577)
    RECEIVE_EXCEPTION = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 863, 2589)
    REVIEW_AND_RESEND_REVISION = bp(ProcessRegistry.COLLABORATIVE_PLANNING,
                                    877, 2631)
    RECEIVE_REVISION = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 881, 2643)
    

class CollaborativeBusinessPlan(Enum):
    CREATE_RETAIL_EVENT = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 883, 2649)
    SEND_RETAIL_EVENT = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 887, 2661)
    RECEIVE_RETAIL_EVENT_REVISION = bp(
        ProcessRegistry.COLLABORATIVE_PLANNING, 907, 2721)
    RECEIVE_TRADE_ITEM_LOCATION_PROFILE = bp(
        ProcessRegistry.COLLABORATIVE_PLANNING, 911, 2733)
    REVISE_TILP = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 919, 2757)
    SEND_TILP_REVISION = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 929, 2787)
    RECEIVE_TILP = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 937, 2811)
    SEND_TILP = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 941, 2823)
    CREATE_TILP = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 947, 2841)
    RECEIVE_RETAIL_EVENT = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 953, 2859)
    REVISE_RETAIL_EVENT = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 967, 2901)
    SEND_REVISION = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 971, 2913)
    

class CreateSalesForecast(Enum):
    CREATE_PRODUCT_ACTIVITY_POS = bp(ProcessRegistry.FORECASTING, 983, 2949)
    CREATE_PRODUCT_ACTIVITY_DC_DATA = bp(ProcessRegistry.FORECASTING, 991, 2973)
    SEND_PRODUCT_ACTIVITY = bp(ProcessRegistry.FORECASTING, 997, 2991)
    CREATE_ITEM_INFORMATION_REQUEST = bp(ProcessRegistry.FORECASTING, 1009,
                                         3027)
    RECEIVE_PRODUCT_ACTIVITY = bp(ProcessRegistry.FORECASTING, 1013, 3039)
    CREATE_SALES_FORECAST = bp(ProcessRegistry.FORECASTING, 1019, 3057)
    SEND_SALES_FORECAST = bp(ProcessRegistry.FORECASTING, 1021, 3063)
    RECEIVE_SALES_FORECAST = bp(ProcessRegistry.FORECASTING, 1031, 3093)
    REUSE_SALES_FORECAST = bp(ProcessRegistry.FORECASTING, 1033, 3099)
    REVISE_SALES_FORECAST = bp(ProcessRegistry.FORECASTING, 1039, 3117)
    SEND_REVISION = bp(ProcessRegistry.FORECASTING, 1049, 3147)
    RECEIVE_SALES_FORECAST_REVISION = bp(ProcessRegistry.FORECASTING, 1051,
                                         3153)
    

class ExceptionHandling(Enum):
    RECEIVE_SALES_FORECAST = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 1061,
                                3183)
    WAIT_FOR_SALES_FORECAST_EXCEPTION_NOTIFICATION = bp(
        ProcessRegistry.COLLABORATIVE_PLANNING, 1063, 3189)
    SEND_EXCEPTION = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 1069, 3207)
    RECEIVE_EXCEPTION = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 1087, 3261)
    RESOLVE_EXCEPTION = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 1091, 3273)
    

class CreateOrderForecast(Enum):
    SEND_PRODUCT_ACTIVITY = bp(ProcessRegistry.FORECASTING, 1093, 3279)
    SEND_RETAIL_EVENT = bp(ProcessRegistry.FORECASTING, 1097, 3291)
    RECEIVE_RETAIL_AND_PRODUCT_ACTIVITY = bp(ProcessRegistry.FORECASTING,
                                             1103, 3309)
    SEND_ORDER_FORECAST = bp(ProcessRegistry.FORECASTING, 1109, 3327)
    RECEIVE_ORDER_FORECAST = bp(ProcessRegistry.FORECASTING, 1117, 3351)
    REVISE_ORDER_FORECAST = bp(ProcessRegistry.FORECASTING, 1123, 3369)
    SEND_ORDER_FORECAST_REVISION = bp(ProcessRegistry.FORECASTING, 1129, 3387)
    

class ExceptionMonitor(Enum):
    ORDERING = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 1151, 3453)
    WAIT_FOR_EXCEPTION_NOTIFICATION = bp(
        ProcessRegistry.COLLABORATIVE_PLANNING, 1153, 3459)
    SEND_EXCEPTION = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 1163, 3489)
    RECEIVE_EXCEPTION = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 1171, 3513)
    RESOLVE_EXCEPTION = bp(ProcessRegistry.COLLABORATIVE_PLANNING, 1181, 3543)
    
    
class InitialStockingByProducer(Enum):
    CALCULATE_THE_INITIAL_DELIVERY = bp(ProcessRegistry.VENDOR_INVENTORY,
                                        1187, 3561)
    SEND_CATALOGUE = bp(ProcessRegistry.VENDOR_INVENTORY, 1193, 3579)
    SEND_DESPATCH_ADVICE = bp(ProcessRegistry.VENDOR_INVENTORY, 1201, 3603)
    DESPATCH_ITEM = bp(ProcessRegistry.VENDOR_INVENTORY, 1213, 3639)
    RECEIVE_CATALOGUE = bp(ProcessRegistry.VENDOR_INVENTORY, 1217, 3651)
    RECEIVE_DESPATCH_ADVICE = bp(ProcessRegistry.VENDOR_INVENTORY, 1223, 3669)
    UPDATE_PRODUCTS_DATABASE = bp(ProcessRegistry.VENDOR_INVENTORY, 1229, 3687)
    RECEIVE_ITEM = bp(ProcessRegistry.VENDOR_INVENTORY, 1231, 3693)
    CHECK_STATUS_OF_ITEMS = bp(ProcessRegistry.VENDOR_INVENTORY, 1237, 3711)
    SEND_RECEIPT_ADVICE = bp(ProcessRegistry.VENDOR_INVENTORY, 1249, 3747)
    RECEIVE_RECEIPT_ADVICE = bp(ProcessRegistry.VENDOR_INVENTORY, 1259, 3777)
    ADJUST_SUPPLY_STATUS = bp(ProcessRegistry.VENDOR_INVENTORY, 1277, 3831)
    
    
class ReportSalesInventoryMovement(Enum):
    SEND_A_REPORT_ABOUT_SALES = bp(ProcessRegistry.VENDOR_INVENTORY, 1279, 3837)
    SEND_A_REPORT_ABOUT_MOVEMENT_OF_GOODS = bp(
        ProcessRegistry.VENDOR_INVENTORY, 1283, 3849)
    RECEIVE_A_REPORT_ABOUT_SALES = bp(ProcessRegistry.VENDOR_INVENTORY, 1289,
                                      3867)
    RECEIVE_A_REPORT_ABOUT_MOVEMENT_OF_GOODS = bp(
        ProcessRegistry.VENDOR_INVENTORY, 1291, 3873)
    

class PermanentReplenishment(Enum):
    SEND_CATALOGUE = bp(ProcessRegistry.PERMANENT_REPLENISHMENT, 1297, 3891)
    SEND_DESPATCH_ADVICE = bp(ProcessRegistry.PERMANENT_REPLENISHMENT, 1301,
                              3903)
    DESPATCH_ITEM = bp(ProcessRegistry.PERMANENT_REPLENISHMENT, 1303, 3909)
    RECEIVE_RECEIPT_ADVICE = bp(ProcessRegistry.PERMANENT_REPLENISHMENT,
                                1307, 3921)
    ADJUST_SUPPLY_STATUS = bp(ProcessRegistry.PERMANENT_REPLENISHMENT, 1319,
                              3957)
    SEND_RECEIPT_ADVICE = bp(ProcessRegistry.PERMANENT_REPLENISHMENT, 1321,
                             3963)
    CHECK_STATUS_OF_ITEMS = bp(ProcessRegistry.PERMANENT_REPLENISHMENT, 1327,
                               3981)
    RECEIVE_ITEM = bp(ProcessRegistry.PERMANENT_REPLENISHMENT, 1361, 4083)
    RECEIVE_DESPATCH_ADVICE = bp(ProcessRegistry.PERMANENT_REPLENISHMENT,
                                 1367, 4101)
    RECEIVE_CATALOGUE = bp(ProcessRegistry.PERMANENT_REPLENISHMENT, 1373, 4119)
    UPDATE_PRODUCTS_DATABASE = bp(ProcessRegistry.PERMANENT_REPLENISHMENT,
                                  1381, 4143)
    

class InvoicingVendorInventory(Enum):
    RAISE_INVOICE = bp(ProcessRegistry.VENDOR_INVENTORY, 1399, 4197)
    RECEIVE_INVOICE = bp(ProcessRegistry.VENDOR_INVENTORY, 1409, 4227)
    

class ReturnsInitiatedByProducer(Enum):
    SEND_INSTRUCTION_FOR_RETURNS = bp(ProcessRegistry.VENDOR_INVENTORY, 1423,
                                      4269)
    RECEIVE_THE_ADVICE = bp(ProcessRegistry.VENDOR_INVENTORY, 1427, 4281)
    CHECK_STATUS_OF_ITEMS = bp(ProcessRegistry.VENDOR_INVENTORY, 1429, 4287)
    SEND_RECEIPT_ADVICE = bp(ProcessRegistry.VENDOR_INVENTORY, 1433, 4299)
    RECEIVE_RECEIPT_ADVICE = bp(ProcessRegistry.VENDOR_INVENTORY, 1439, 4317)
    SEND_ITEM = bp(ProcessRegistry.VENDOR_INVENTORY, 1447, 4341)
    SEND_ADVICE_TO_NOTIFY_RETURN = bp(ProcessRegistry.VENDOR_INVENTORY, 1451,
                                      4353)
    RECEIVE_INSTRUCTION_FOR_RETURNS = bp(ProcessRegistry.VENDOR_INVENTORY,
                                         1453, 4359)
    

class PriceAdjustments(Enum):
    RECEIVE_ORDER = bp(ProcessRegistry.PRICE_ADJUSTMENTS, 1459, 4377)
    SEND_DESPATCH_ADVICE = bp(ProcessRegistry.PRICE_ADJUSTMENTS, 1471, 4413)


class InitialStockingByRetailer(Enum):
    RECEIVE_ORDER = bp(
        ProcessRegistry.INITIAL_STOCKING_OF_THE_AREA_BY_RETAILER, 1481, 4443)
    SEND_DESPATCH_ADVICE = bp(
        ProcessRegistry.INITIAL_STOCKING_OF_THE_AREA_BY_RETAILER, 1483, 4449)
    DESPATCH_ORDER_ITEMS = bp(
        ProcessRegistry.INITIAL_STOCKING_OF_THE_AREA_BY_RETAILER, 1487, 4461)
    RECEIVE_RECEIPT_ADVICE = bp(
        ProcessRegistry.INITIAL_STOCKING_OF_THE_AREA_BY_RETAILER, 1489, 4467)
    SEND_RECEIPT_ADVICE = bp(
        ProcessRegistry.INITIAL_STOCKING_OF_THE_AREA_BY_RETAILER, 1493, 4479)
    CHECK_STATUS_OF_ITEMS = bp(
        ProcessRegistry.INITIAL_STOCKING_OF_THE_AREA_BY_RETAILER, 1499, 4497)
    RECEIVE_ORDER_ITEMS = bp(
        ProcessRegistry.INITIAL_STOCKING_OF_THE_AREA_BY_RETAILER, 1511, 4533)
    RECEIVE_DESPATCH_ADVICE = bp(
        ProcessRegistry.INITIAL_STOCKING_OF_THE_AREA_BY_RETAILER, 1523, 4569)
    SEND_ORDER = bp(ProcessRegistry.INITIAL_STOCKING_OF_THE_AREA_BY_RETAILER,
                    1531, 4593)
    ADJUST_SUPPLY_STATUS = bp(
        ProcessRegistry.INITIAL_STOCKING_OF_THE_AREA_BY_RETAILER, 1543, 4629)

    
class SynchronizingStockInformation(Enum):
    SYNCHRONIZE_STOCK_INFORMATION = bp(ProcessRegistry.VENDOR_INVENTORY,
                                       1549, 4647)
    SEND_INFORMATION_ABOUT_STOCK = bp(ProcessRegistry.VENDOR_INVENTORY, 1553,
                                      4659)
    

class ItemChangeCatalogue(Enum):
    INFORM_ABOUT_CHANGES_INSIDE_THE_CATALOGUE = bp(
        ProcessRegistry.VENDOR_INVENTORY, 1559, 4677)
    RECEIVE_INFORMATION = bp(ProcessRegistry.VENDOR_INVENTORY, 1567, 4701)
    UPDATE_PRODUCTS_DATABASE = bp(ProcessRegistry.VENDOR_INVENTORY, 1571, 4713)
    

class PeriodicAvailabilityInformation(Enum):
    SEND_STOCK_AVAILABILITY_REPORT = bp(ProcessRegistry.VENDOR_INVENTORY,
                                        1579, 4737)
    RECEIVE_STOCK_AVAILABILITY_REPORT = bp(ProcessRegistry.VENDOR_INVENTORY,
                                           1583, 4749)
    
    
class InitiateFreight(Enum):
    REQUEST_LOGISTIC_SERVICE = bp(ProcessRegistry.FREIGHT_MANAGEMENT, 1597,
                                  4791)
    RECEIVE_BILL_OF_LANDING = bp(ProcessRegistry.FREIGHT_MANAGEMENT, 1601, 4803)
    RECEIVE_WAYBILL = bp(ProcessRegistry.FREIGHT_MANAGEMENT, 1607, 4821)
    RECEIVE_STATUS_REPORT = bp(ProcessRegistry.FREIGHT_MANAGEMENT, 1609, 4827)
    REQUEST_TRANSPORT_SERVICE = bp(ProcessRegistry.FREIGHT_MANAGEMENT, 1613,
                                   4839)
    SEND_BILL_OF_LANDING = bp(ProcessRegistry.FREIGHT_MANAGEMENT, 1619, 4857)
    SEND_WAYBILL_TO_COSIGNOR = bp(ProcessRegistry.FREIGHT_MANAGEMENT, 1621,
                                  4863)
    REPORT_STATUS = bp(ProcessRegistry.FREIGHT_MANAGEMENT, 1627, 4881)
    RECEIVE_TRANSPORT_SERVICE_REQUEST = bp(
        ProcessRegistry.FREIGHT_MANAGEMENT, 1637, 4911)
    TRANSPORT_GOODS_ITEMS_TO_DELIVERY_PARTY = bp(
        ProcessRegistry.FREIGHT_MANAGEMENT, 1657, 4971)
    

class FreightStatusReporting(Enum):
    REQUEST_STATUS = bp(ProcessRegistry.FREIGHT_MANAGEMENT, 1663, 4989)
    RECEIVE_STATUS_REPORT = bp(ProcessRegistry.FREIGHT_MANAGEMENT, 1667, 5001)
    RECEIVE_STATUS_REQUEST = bp(ProcessRegistry.FREIGHT_MANAGEMENT, 1669, 5007)
    REPORT_STATUS = bp(ProcessRegistry.FREIGHT_MANAGEMENT, 1693, 5079)
    

class CertificateOfOrigin(Enum):
    APPLY_FOR_COO = bp(ProcessRegistry.CERTIFICATE_OF_ORIGIN_OF_GOODS, 1697,
                       5091)
    REQUEST_STATUS = bp(ProcessRegistry.CERTIFICATE_OF_ORIGIN_OF_GOODS, 1699,
                        5097)
    RECEIVE_RESPONSE = bp(ProcessRegistry.CERTIFICATE_OF_ORIGIN_OF_GOODS,
                          1709, 5127)
    APPLY_FOR_ENDORSEMENT = bp(
        ProcessRegistry.CERTIFICATE_OF_ORIGIN_OF_GOODS, 1721, 5163)
    SEND_COO = bp(ProcessRegistry.CERTIFICATE_OF_ORIGIN_OF_GOODS, 1723, 5169)
    RECEIVE_COO = bp(ProcessRegistry.CERTIFICATE_OF_ORIGIN_OF_GOODS, 1733, 5199)
    REJECT_COO = bp(ProcessRegistry.CERTIFICATE_OF_ORIGIN_OF_GOODS, 1741, 5223)
    QUERY_COO = bp(ProcessRegistry.CERTIFICATE_OF_ORIGIN_OF_GOODS, 1747, 5241)
    ENDORSE_COO = bp(ProcessRegistry.CERTIFICATE_OF_ORIGIN_OF_GOODS, 1753, 5259)
    

class IntermodalFreightManagement(Enum):
    DEFINE_TRANSPORT_DEMAND = bp(
        ProcessRegistry.INTERMODAL_FREIGHT_MANAGEMENT, 1759, 5277)
    PERFORM_BOOKING_MANAGEMENT = bp(
        ProcessRegistry.INTERMODAL_FREIGHT_MANAGEMENT, 1777, 5331)
    PERFORM__ORDER_MANAGEMENT = bp(
        ProcessRegistry.INTERMODAL_FREIGHT_MANAGEMENT, 1783, 5349)
    ANNOUNCE_TRANSPORT_SERVICE = bp(
        ProcessRegistry.INTERMODAL_FREIGHT_MANAGEMENT, 1787, 5361)
    PLAN_TRANSPORT_SERVICE = bp(
        ProcessRegistry.INTERMODAL_FREIGHT_MANAGEMENT, 1789, 5367)
    MONITOR_AND_CONTROL_TRANSPORT_SERVICES = bp(
        ProcessRegistry.INTERMODAL_FREIGHT_MANAGEMENT, 1801, 5403)
    EXECUTE_TRANSPORT_SERVICES = bp(
        ProcessRegistry.INTERMODAL_FREIGHT_MANAGEMENT, 1811, 5433)
    PERFORM_COMPLIANCE_MANAGEMENT = bp(
        ProcessRegistry.INTERMODAL_FREIGHT_MANAGEMENT, 1823, 5469)
    PROVIDE_TRANSPORTATION_NETWORK_INFORMATION = bp(
        ProcessRegistry.INTERMODAL_FREIGHT_MANAGEMENT, 1831, 5493)
    FINALIZE_TRANSPORT_SERVICE = bp(
        ProcessRegistry.INTERMODAL_FREIGHT_MANAGEMENT, 1847, 5541)
    MANAGE_COMPLETION = bp(ProcessRegistry.INTERMODAL_FREIGHT_MANAGEMENT,
                           1861, 5583)
    
    
class TransportServiceDescription(Enum):
    REQUEST_TRANSPORT_SERVICE_DESCRIPTION = bp(
        ProcessRegistry.FREIGHT_MANAGEMENT, 1867, 5601)
    RECEIVE_TRANSPORT_SERVICE_DESCRIPTION = bp(
        ProcessRegistry.FREIGHT_MANAGEMENT, 1871, 5613)
    SEND_TRANSPORT_SERVICE_DESCRIPTION = bp(
        ProcessRegistry.FREIGHT_MANAGEMENT, 1873, 5619)
    RECEIVE_TRANSPORT_SERVICE_DESCRIPTION_REQUEST = bp(
        ProcessRegistry.FREIGHT_MANAGEMENT, 1877, 5631)
    
    
class TransportExecutionPlan(Enum):
    CREATE_UPDATE_TRANSPORT_EXECUTION_PLAN_REQUEST = bp(
        ProcessRegistry.FREIGHT_MANAGEMENT, 1879, 5637)
    REQUEST_TRANSPORT_SERVICE = bp(ProcessRegistry.FREIGHT_MANAGEMENT, 1889,
                                   5667)
    RECEIVE_REJECTED_TRANSPORT_EXECUTION_PLAN = bp(
        ProcessRegistry.FREIGHT_MANAGEMENT, 1901, 5703)
    RECEIVE_PROPOSED_TRANSPORT_EXECUTION_PLAN = bp(
        ProcessRegistry.FREIGHT_MANAGEMENT, 1907, 5721)
    EVALUATE_TRANSPORT_EXECUTION_PLAN = bp(
        ProcessRegistry.FREIGHT_MANAGEMENT, 1913, 5739)
    CONFIRM_EXECUTION_PLAN = bp(ProcessRegistry.FREIGHT_MANAGEMENT, 1931, 5793)
    REJECT_TRANSPORT_EXCECUTION_PLAN = bp(ProcessRegistry.FREIGHT_MANAGEMENT,
                                          1933, 5799)
    RECEIVE_CONFIRMED_TRANSPORT_EXECUTION_PLAN = bp(
        ProcessRegistry.FREIGHT_MANAGEMENT, 1949, 5847)
    RECEIVE_TRANSPORT_SERVICE_REQUEST = bp(
        ProcessRegistry.FREIGHT_MANAGEMENT, 1973, 5919)
    REJECT_TRANSPORT_SERVICE_REQUEST = bp(ProcessRegistry.FREIGHT_MANAGEMENT,
                                          1979, 5937)
    CONFIRM_TRANSPORT_SERVICE_REQUEST = bp(
        ProcessRegistry.FREIGHT_MANAGEMENT, 1987, 5961)
    EVALUATE_TRANSPORT_EXECUTION_PLAN_REQUEST = bp(
        ProcessRegistry.FREIGHT_MANAGEMENT, 1993, 5979)
    

class GoodsItemItinery(Enum):
    RECEIVE_GOODS_ITEM_ITINERARY = bp(ProcessRegistry.FREIGHT_MANAGEMENT,
                                      1997, 5991)
    SEND_GOODS_ITEM_ITINERARY = bp(ProcessRegistry.FREIGHT_MANAGEMENT, 1999,
                                   5997)
    

class TransportProgressStatus(Enum):
    REQUEST_TRANSPORT_PROGESS_STATUS = bp(ProcessRegistry.FREIGHT_MANAGEMENT,
                                          2003, 6009)
    RECEIVE_TRANSPORT_PROGRESS_STATUS = bp(
        ProcessRegistry.FREIGHT_MANAGEMENT, 2011, 6033)
    SEND_TRANSPORT_PROGRESS_STATUS = bp(ProcessRegistry.FREIGHT_MANAGEMENT,
                                        2017, 6051)
    RECEIVE_TRANSPORT_PROGRESS_STATUS_REQUEST = bp(
        ProcessRegistry.FREIGHT_MANAGEMENT, 2027, 6081)
