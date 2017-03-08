#!/usr/bin/python3


class BaseElement(object):
    def __init__(self, required=False):
        self.required = required


class Tag(BaseElement):
    def __init__(self, value=None, required=False):
        BaseElement.__init__(self, required=required)
        self.value = value


class Component(BaseElement):
    def __init__(self, required=False):
        BaseElement.__init__(self, required=required)


class Group(Component):
    def __init__(self, required=False):
        Component.__init__(self, required=required)


class RepeatingGroup(Component):
    def __init__(self, required=False):
        Component.__init__(self, required=required)
        self.groups = []


class Message(object):
    def __init__(self):
        pass


class AppMessage(Message):
    def __init__(self):
        Message.__init__(self)


class FIX50SP2:
    class Tags:
        class Account(Tag):
            Tag = 1
            Type = "STRING"

        class AdvId(Tag):
            Tag = 2
            Type = "STRING"

        class AdvRefID(Tag):
            Tag = 3
            Type = "STRING"

        class AdvSide(Tag):
            Tag = 4
            Type = "CHAR"
            class Values:
                BUY = "B"
                SELL = "S"
                TRADE = "T"
                CROSS = "X"

        class AdvTransType(Tag):
            Tag = 5
            Type = "STRING"
            class Values:
                NEW = "N"
                CANCEL = "C"
                REPLACE = "R"

        class AvgPx(Tag):
            Tag = 6
            Type = "PRICE"

        class BeginSeqNo(Tag):
            Tag = 7
            Type = "SEQNUM"

        class BeginString(Tag):
            Tag = 8
            Type = "STRING"

        class BodyLength(Tag):
            Tag = 9
            Type = "LENGTH"

        class CheckSum(Tag):
            Tag = 10
            Type = "STRING"

        class ClOrdID(Tag):
            Tag = 11
            Type = "STRING"

        class Commission(Tag):
            Tag = 12
            Type = "AMT"

        class CommType(Tag):
            Tag = 13
            Type = "CHAR"
            class Values:
                PER_UNIT = "1"
                PERCENT = "2"
                ABSOLUTE = "3"
                PERCENTAGE_WAIVED_4 = "4"
                PERCENTAGE_WAIVED_5 = "5"
                POINTS_PER_BOND_OR_CONTRACT = "6"

        class CumQty(Tag):
            Tag = 14
            Type = "QTY"

        class Currency(Tag):
            Tag = 15
            Type = "CURRENCY"

        class EndSeqNo(Tag):
            Tag = 16
            Type = "SEQNUM"

        class ExecID(Tag):
            Tag = 17
            Type = "STRING"

        class ExecInst(Tag):
            Tag = 18
            Type = "MULTIPLECHARVALUE"
            class Values:
                STAY_ON_OFFER_SIDE = "0"
                NOT_HELD = "1"
                WORK = "2"
                GO_ALONG = "3"
                OVER_THE_DAY = "4"
                HELD = "5"
                PARTICIPATE_DONT_INITIATE = "6"
                STRICT_SCALE = "7"
                TRY_TO_SCALE = "8"
                STAY_ON_BID_SIDE = "9"
                NO_CROSS = "A"
                OK_TO_CROSS = "B"
                CALL_FIRST = "C"
                PERCENT_OF_VOLUME = "D"
                DO_NOT_INCREASE = "E"
                DO_NOT_REDUCE = "F"
                ALL_OR_NONE = "G"
                REINSTATE_ON_SYSTEM_FAILURE = "H"
                INSTITUTIONS_ONLY = "I"
                REINSTATE_ON_TRADING_HALT = "J"
                CANCEL_ON_TRADING_HALT = "K"
                LAST_PEG = "L"
                MID_PRICE_PEG = "M"
                NON_NEGOTIABLE = "N"
                OPENING_PEG = "O"
                MARKET_PEG = "P"
                CANCEL_ON_SYSTEM_FAILURE = "Q"
                PRIMARY_PEG = "R"
                SUSPEND = "S"
                FIXED_PEG_TO_LOCAL_BEST_BID_OR_OFFER_AT_TIME_OF_ORDER = "T"
                CUSTOMER_DISPLAY_INSTRUCTION = "U"
                NETTING = "V"
                PEG_TO_VWAP = "W"
                TRADE_ALONG = "X"
                TRY_TO_STOP = "Y"
                CANCEL_IF_NOT_BEST = "Z"
                TRAILING_STOP_PEG = "a"
                STRICT_LIMIT = "b"
                IGNORE_PRICE_VALIDITY_CHECKS = "c"
                PEG_TO_LIMIT_PRICE = "d"
                WORK_TO_TARGET_STRATEGY = "e"
                INTERMARKET_SWEEP = "f"
                EXTERNAL_ROUTING_ALLOWED = "g"
                EXTERNAL_ROUTING_NOT_ALLOWED = "h"
                IMBALANCE_ONLY = "i"
                SINGLE_EXECUTION_REQUESTED_FOR_BLOCK_TRADE = "j"
                BEST_EXECUTION = "k"
                SUSPEND_ON_SYSTEM_FAILURE = "l"
                SUSPEND_ON_TRADING_HALT = "m"
                REINSTATE_ON_CONNECTION_LOSS = "n"
                CANCEL_ON_CONNECTION_LOSS = "o"
                SUSPEND_ON_CONNECTION_LOSS = "p"
                RELEASE_FROM_SUSPENSION = "q"
                EXECUTE_AS_DELTA_NEUTRAL_USING_VOLATILITY_PROVIDED = "r"
                EXECUTE_AS_DURATION_NEUTRAL = "s"
                EXECUTE_AS_FX_NEUTRAL = "t"

        class ExecRefID(Tag):
            Tag = 19
            Type = "STRING"

        class HandlInst(Tag):
            Tag = 21
            Type = "CHAR"
            class Values:
                AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION = "1"
                AUTOMATED_EXECUTION_ORDER_PUBLIC_BROKER_INTERVENTION_OK = "2"
                MANUAL_ORDER_BEST_EXECUTION = "3"

        class SecurityIDSource(Tag):
            Tag = 22
            Type = "STRING"
            class Values:
                CUSIP = "1"
                SEDOL = "2"
                QUIK = "3"
                ISIN_NUMBER = "4"
                RIC_CODE = "5"
                ISO_CURRENCY_CODE = "6"
                ISO_COUNTRY_CODE = "7"
                EXCHANGE_SYMBOL = "8"
                CONSOLIDATED_TAPE_ASSOCIATION = "9"
                BLOOMBERG_SYMBOL = "A"
                WERTPAPIER = "B"
                DUTCH = "C"
                VALOREN = "D"
                SICOVAM = "E"
                BELGIAN = "F"
                COMMON = "G"
                CLEARING_HOUSE = "H"
                ISDA_FPML_PRODUCT_SPECIFICATION = "I"
                OPTION_PRICE_REPORTING_AUTHORITY = "J"
                ISDA_FPML_PRODUCT_URL = "K"
                LETTER_OF_CREDIT = "L"
                MARKETPLACE_ASSIGNED_IDENTIFIER = "M"

        class IOIID(Tag):
            Tag = 23
            Type = "STRING"

        class IOIQltyInd(Tag):
            Tag = 25
            Type = "CHAR"
            class Values:
                HIGH = "H"
                LOW = "L"
                MEDIUM = "M"

        class IOIRefID(Tag):
            Tag = 26
            Type = "STRING"

        class IOIQty(Tag):
            Tag = 27
            Type = "STRING"
            class Values:
                SMALL = "S"
                MEDIUM = "M"
                LARGE = "L"
                UNDISCLOSED_QUANTITY = "U"

        class IOITransType(Tag):
            Tag = 28
            Type = "CHAR"
            class Values:
                NEW = "N"
                CANCEL = "C"
                REPLACE = "R"

        class LastCapacity(Tag):
            Tag = 29
            Type = "CHAR"
            class Values:
                AGENT = "1"
                CROSS_AS_AGENT = "2"
                CROSS_AS_PRINCIPAL = "3"
                PRINCIPAL = "4"

        class LastMkt(Tag):
            Tag = 30
            Type = "EXCHANGE"

        class LastPx(Tag):
            Tag = 31
            Type = "PRICE"

        class LastQty(Tag):
            Tag = 32
            Type = "QTY"

        class NoLinesOfText(Tag):
            Tag = 33
            Type = "NUMINGROUP"

        class MsgSeqNum(Tag):
            Tag = 34
            Type = "SEQNUM"

        class MsgType(Tag):
            Tag = 35
            Type = "STRING"
            class Values:
                HEARTBEAT = "0"
                TESTREQUEST = "1"
                RESENDREQUEST = "2"
                REJECT = "3"
                SEQUENCERESET = "4"
                LOGOUT = "5"
                IOI = "6"
                ADVERTISEMENT = "7"
                EXECUTIONREPORT = "8"
                ORDERCANCELREJECT = "9"
                LOGON = "A"
                DERIVATIVESECURITYLIST = "AA"
                NEWORDERMULTILEG = "AB"
                MULTILEGORDERCANCELREPLACE = "AC"
                TRADECAPTUREREPORTREQUEST = "AD"
                TRADECAPTUREREPORT = "AE"
                ORDERMASSSTATUSREQUEST = "AF"
                QUOTEREQUESTREJECT = "AG"
                RFQREQUEST = "AH"
                QUOTESTATUSREPORT = "AI"
                QUOTERESPONSE = "AJ"
                CONFIRMATION = "AK"
                POSITIONMAINTENANCEREQUEST = "AL"
                POSITIONMAINTENANCEREPORT = "AM"
                REQUESTFORPOSITIONS = "AN"
                REQUESTFORPOSITIONSACK = "AO"
                POSITIONREPORT = "AP"
                TRADECAPTUREREPORTREQUESTACK = "AQ"
                TRADECAPTUREREPORTACK = "AR"
                ALLOCATIONREPORT = "AS"
                ALLOCATIONREPORTACK = "AT"
                CONFIRMATIONACK = "AU"
                SETTLEMENTINSTRUCTIONREQUEST = "AV"
                ASSIGNMENTREPORT = "AW"
                COLLATERALREQUEST = "AX"
                COLLATERALASSIGNMENT = "AY"
                COLLATERALRESPONSE = "AZ"
                NEWS = "B"
                COLLATERALREPORT = "BA"
                COLLATERALINQUIRY = "BB"
                NETWORKCOUNTERPARTYSYSTEMSTATUSREQUEST = "BC"
                NETWORKCOUNTERPARTYSYSTEMSTATUSRESPONSE = "BD"
                USERREQUEST = "BE"
                USERRESPONSE = "BF"
                COLLATERALINQUIRYACK = "BG"
                CONFIRMATIONREQUEST = "BH"
                TRADINGSESSIONLISTREQUEST = "BI"
                TRADINGSESSIONLIST = "BJ"
                SECURITYLISTUPDATEREPORT = "BK"
                ADJUSTEDPOSITIONREPORT = "BL"
                ALLOCATIONINSTRUCTIONALERT = "BM"
                EXECUTIONACKNOWLEDGEMENT = "BN"
                CONTRARYINTENTIONREPORT = "BO"
                SECURITYDEFINITIONUPDATEREPORT = "BP"
                SETTLEMENTOBLIGATIONREPORT = "BQ"
                DERIVATIVESECURITYLISTUPDATEREPORT = "BR"
                TRADINGSESSIONLISTUPDATEREPORT = "BS"
                MARKETDEFINITIONREQUEST = "BT"
                MARKETDEFINITION = "BU"
                MARKETDEFINITIONUPDATEREPORT = "BV"
                APPLICATIONMESSAGEREQUEST = "BW"
                APPLICATIONMESSAGEREQUESTACK = "BX"
                APPLICATIONMESSAGEREPORT = "BY"
                ORDERMASSACTIONREPORT = "BZ"
                EMAIL = "C"
                ORDERMASSACTIONREQUEST = "CA"
                USERNOTIFICATION = "CB"
                STREAMASSIGNMENTREQUEST = "CC"
                STREAMASSIGNMENTREPORT = "CD"
                STREAMASSIGNMENTREPORTACK = "CE"
                NEWORDERSINGLE = "D"
                NEWORDERLIST = "E"
                ORDERCANCELREQUEST = "F"
                ORDERCANCELREPLACEREQUEST = "G"
                ORDERSTATUSREQUEST = "H"
                ALLOCATIONINSTRUCTION = "J"
                LISTCANCELREQUEST = "K"
                LISTEXECUTE = "L"
                LISTSTATUSREQUEST = "M"
                LISTSTATUS = "N"
                ALLOCATIONINSTRUCTIONACK = "P"
                DONTKNOWTRADE = "Q"
                QUOTEREQUEST = "R"
                QUOTE = "S"
                SETTLEMENTINSTRUCTIONS = "T"
                MARKETDATAREQUEST = "V"
                MARKETDATASNAPSHOTFULLREFRESH = "W"
                MARKETDATAINCREMENTALREFRESH = "X"
                MARKETDATAREQUESTREJECT = "Y"
                QUOTECANCEL = "Z"
                QUOTESTATUSREQUEST = "a"
                MASSQUOTEACKNOWLEDGEMENT = "b"
                SECURITYDEFINITIONREQUEST = "c"
                SECURITYDEFINITION = "d"
                SECURITYSTATUSREQUEST = "e"
                SECURITYSTATUS = "f"
                TRADINGSESSIONSTATUSREQUEST = "g"
                TRADINGSESSIONSTATUS = "h"
                MASSQUOTE = "i"
                BUSINESSMESSAGEREJECT = "j"
                BIDREQUEST = "k"
                BIDRESPONSE = "l"
                LISTSTRIKEPRICE = "m"
                XMLNONFIX = "n"
                REGISTRATIONINSTRUCTIONS = "o"
                REGISTRATIONINSTRUCTIONSRESPONSE = "p"
                ORDERMASSCANCELREQUEST = "q"
                ORDERMASSCANCELREPORT = "r"
                NEWORDERCROSS = "s"
                CROSSORDERCANCELREPLACEREQUEST = "t"
                CROSSORDERCANCELREQUEST = "u"
                SECURITYTYPEREQUEST = "v"
                SECURITYTYPES = "w"
                SECURITYLISTREQUEST = "x"
                SECURITYLIST = "y"
                DERIVATIVESECURITYLISTREQUEST = "z"

        class NewSeqNo(Tag):
            Tag = 36
            Type = "SEQNUM"

        class OrderID(Tag):
            Tag = 37
            Type = "STRING"

        class OrderQty(Tag):
            Tag = 38
            Type = "QTY"

        class OrdStatus(Tag):
            Tag = 39
            Type = "CHAR"
            class Values:
                NEW = "0"
                PARTIALLY_FILLED = "1"
                FILLED = "2"
                DONE_FOR_DAY = "3"
                CANCELED = "4"
                REPLACED = "5"
                PENDING_CANCEL = "6"
                STOPPED = "7"
                REJECTED = "8"
                SUSPENDED = "9"
                PENDING_NEW = "A"
                CALCULATED = "B"
                EXPIRED = "C"
                ACCEPTED_FOR_BIDDING = "D"
                PENDING_REPLACE = "E"

        class OrdType(Tag):
            Tag = 40
            Type = "CHAR"
            class Values:
                MARKET = "1"
                LIMIT = "2"
                STOP = "3"
                STOP_LIMIT = "4"
                MARKET_ON_CLOSE = "5"
                WITH_OR_WITHOUT = "6"
                LIMIT_OR_BETTER = "7"
                LIMIT_WITH_OR_WITHOUT = "8"
                ON_BASIS = "9"
                ON_CLOSE = "A"
                LIMIT_ON_CLOSE = "B"
                FOREX_MARKET = "C"
                PREVIOUSLY_QUOTED = "D"
                PREVIOUSLY_INDICATED = "E"
                FOREX_LIMIT = "F"
                FOREX_SWAP = "G"
                FOREX_PREVIOUSLY_QUOTED = "H"
                FUNARI = "I"
                MARKET_IF_TOUCHED = "J"
                MARKET_WITH_LEFT_OVER_AS_LIMIT = "K"
                PREVIOUS_FUND_VALUATION_POINT = "L"
                NEXT_FUND_VALUATION_POINT = "M"
                PEGGED = "P"
                COUNTER_ORDER_SELECTION = "Q"

        class OrigClOrdID(Tag):
            Tag = 41
            Type = "STRING"

        class OrigTime(Tag):
            Tag = 42
            Type = "UTCTIMESTAMP"

        class PossDupFlag(Tag):
            Tag = 43
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class Price(Tag):
            Tag = 44
            Type = "PRICE"

        class RefSeqNum(Tag):
            Tag = 45
            Type = "SEQNUM"

        class SecurityID(Tag):
            Tag = 48
            Type = "STRING"

        class SenderCompID(Tag):
            Tag = 49
            Type = "STRING"

        class SenderSubID(Tag):
            Tag = 50
            Type = "STRING"

        class SendingTime(Tag):
            Tag = 52
            Type = "UTCTIMESTAMP"

        class Quantity(Tag):
            Tag = 53
            Type = "QTY"

        class Side(Tag):
            Tag = 54
            Type = "CHAR"
            class Values:
                BUY = "1"
                SELL = "2"
                BUY_MINUS = "3"
                SELL_PLUS = "4"
                SELL_SHORT = "5"
                SELL_SHORT_EXEMPT = "6"
                UNDISCLOSED = "7"
                CROSS = "8"
                CROSS_SHORT = "9"
                CROSS_SHORT_EXEMPT = "A"
                AS_DEFINED = "B"
                OPPOSITE = "C"
                SUBSCRIBE = "D"
                REDEEM = "E"
                LEND = "F"
                BORROW = "G"

        class Symbol(Tag):
            Tag = 55
            Type = "STRING"

        class TargetCompID(Tag):
            Tag = 56
            Type = "STRING"

        class TargetSubID(Tag):
            Tag = 57
            Type = "STRING"

        class Text(Tag):
            Tag = 58
            Type = "STRING"

        class TimeInForce(Tag):
            Tag = 59
            Type = "CHAR"
            class Values:
                DAY = "0"
                GOOD_TILL_CANCEL = "1"
                AT_THE_OPENING = "2"
                IMMEDIATE_OR_CANCEL = "3"
                FILL_OR_KILL = "4"
                GOOD_TILL_CROSSING = "5"
                GOOD_TILL_DATE = "6"
                AT_THE_CLOSE = "7"
                GOOD_THROUGH_CROSSING = "8"
                AT_CROSSING = "9"

        class TransactTime(Tag):
            Tag = 60
            Type = "UTCTIMESTAMP"

        class Urgency(Tag):
            Tag = 61
            Type = "CHAR"
            class Values:
                NORMAL = "0"
                FLASH = "1"
                BACKGROUND = "2"

        class ValidUntilTime(Tag):
            Tag = 62
            Type = "UTCTIMESTAMP"

        class SettlType(Tag):
            Tag = 63
            Type = "STRING"
            class Values:
                REGULAR = "0"
                CASH = "1"
                NEXT_DAY = "2"
                T_PLUS_2 = "3"
                T_PLUS_3 = "4"
                T_PLUS_4 = "5"
                FUTURE = "6"
                WHEN_AND_IF_ISSUED = "7"
                SELLERS_OPTION = "8"
                T_PLUS_5 = "9"
                BROKEN_DATE = "B"
                FX_SPOT_NEXT_SETTLEMENT = "C"

        class SettlDate(Tag):
            Tag = 64
            Type = "LOCALMKTDATE"

        class SymbolSfx(Tag):
            Tag = 65
            Type = "STRING"
            class Values:
                EUCP_WITH_LUMP_SUM_INTEREST_RATHER_THAN_DISCOUNT_PRICE = "CD"
                WHEN_ISSUED_FOR_A_SECURITY_TO_BE_REISSUED_UNDER_AN_OLD_CUSIP_OR_ISIN = "WI"

        class ListID(Tag):
            Tag = 66
            Type = "STRING"

        class ListSeqNo(Tag):
            Tag = 67
            Type = "INT"

        class TotNoOrders(Tag):
            Tag = 68
            Type = "INT"

        class ListExecInst(Tag):
            Tag = 69
            Type = "STRING"

        class AllocID(Tag):
            Tag = 70
            Type = "STRING"

        class AllocTransType(Tag):
            Tag = 71
            Type = "CHAR"
            class Values:
                NEW = "0"
                REPLACE = "1"
                CANCEL = "2"
                PRELIMINARY = "3"
                CALCULATED = "4"
                CALCULATED_WITHOUT_PRELIMINARY = "5"
                REVERSAL = "6"

        class RefAllocID(Tag):
            Tag = 72
            Type = "STRING"

        class NoOrders(Tag):
            Tag = 73
            Type = "NUMINGROUP"

        class AvgPxPrecision(Tag):
            Tag = 74
            Type = "INT"

        class TradeDate(Tag):
            Tag = 75
            Type = "LOCALMKTDATE"

        class PositionEffect(Tag):
            Tag = 77
            Type = "CHAR"
            class Values:
                CLOSE = "C"
                FIFO = "F"
                OPEN = "O"
                ROLLED = "R"
                CLOSE_BUT_NOTIFY_ON_OPEN = "N"
                DEFAULT = "D"

        class NoAllocs(Tag):
            Tag = 78
            Type = "NUMINGROUP"

        class AllocAccount(Tag):
            Tag = 79
            Type = "STRING"

        class AllocQty(Tag):
            Tag = 80
            Type = "QTY"

        class ProcessCode(Tag):
            Tag = 81
            Type = "CHAR"
            class Values:
                REGULAR = "0"
                SOFT_DOLLAR = "1"
                STEP_IN = "2"
                STEP_OUT = "3"
                SOFT_DOLLAR_STEP_IN = "4"
                SOFT_DOLLAR_STEP_OUT = "5"
                PLAN_SPONSOR = "6"

        class NoRpts(Tag):
            Tag = 82
            Type = "INT"

        class RptSeq(Tag):
            Tag = 83
            Type = "INT"

        class CxlQty(Tag):
            Tag = 84
            Type = "QTY"

        class NoDlvyInst(Tag):
            Tag = 85
            Type = "NUMINGROUP"

        class AllocStatus(Tag):
            Tag = 87
            Type = "INT"
            class Values:
                ACCEPTED = 0
                BLOCK_LEVEL_REJECT = 1
                ACCOUNT_LEVEL_REJECT = 2
                RECEIVED = 3
                INCOMPLETE = 4
                REJECTED_BY_INTERMEDIARY = 5
                ALLOCATION_PENDING = 6
                REVERSED = 7

        class AllocRejCode(Tag):
            Tag = 88
            Type = "INT"
            class Values:
                UNKNOWN_ACCOUNT = 0
                INCORRECT_QUANTITY = 1
                INCORRECT_AVERAGEG_PRICE = 2
                UNKNOWN_EXECUTING_BROKER_MNEMONIC = 3
                COMMISSION_DIFFERENCE = 4
                UNKNOWN_ORDERID = 5
                UNKNOWN_LISTID = 6
                OTHER_7 = 7
                INCORRECT_ALLOCATED_QUANTITY = 8
                CALCULATION_DIFFERENCE = 9
                UNKNOWN_OR_STALE_EXECID = 10
                MISMATCHED_DATA = 11
                UNKNOWN_CLORDID = 12
                WAREHOUSE_REQUEST_REJECTED = 13
                OTHER_99 = 99

        class Signature(Tag):
            Tag = 89
            Type = "DATA"

        class SecureDataLen(Tag):
            Tag = 90
            Type = "LENGTH"

        class SecureData(Tag):
            Tag = 91
            Type = "DATA"

        class SignatureLength(Tag):
            Tag = 93
            Type = "LENGTH"

        class EmailType(Tag):
            Tag = 94
            Type = "CHAR"
            class Values:
                NEW = "0"
                REPLY = "1"
                ADMIN_REPLY = "2"

        class RawDataLength(Tag):
            Tag = 95
            Type = "LENGTH"

        class RawData(Tag):
            Tag = 96
            Type = "DATA"

        class PossResend(Tag):
            Tag = 97
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class EncryptMethod(Tag):
            Tag = 98
            Type = "INT"
            class Values:
                NONE = 0
                PKCS_1 = 1
                DES = 2
                PKCS_3 = 3
                PGP_4 = 4
                PGP_5 = 5
                PEM = 6

        class StopPx(Tag):
            Tag = 99
            Type = "PRICE"

        class ExDestination(Tag):
            Tag = 100
            Type = "EXCHANGE"

        class CxlRejReason(Tag):
            Tag = 102
            Type = "INT"
            class Values:
                TOO_LATE_TO_CANCEL = 0
                UNKNOWN_ORDER = 1
                BROKER = 2
                ORDER_ALREADY_IN_PENDING_CANCEL_OR_PENDING_REPLACE_STATUS = 3
                UNABLE_TO_PROCESS_ORDER_MASS_CANCEL_REQUEST = 4
                ORIGORDMODTIME = 5
                DUPLICATE_CLORDID = 6
                PRICE_EXCEEDS_CURRENT_PRICE = 7
                PRICE_EXCEEDS_CURRENT_PRICE_BAND = 8
                INVALID_PRICE_INCREMENT = 18
                OTHER = 99

        class OrdRejReason(Tag):
            Tag = 103
            Type = "INT"
            class Values:
                BROKER = 0
                UNKNOWN_SYMBOL = 1
                EXCHANGE_CLOSED = 2
                ORDER_EXCEEDS_LIMIT = 3
                TOO_LATE_TO_ENTER = 4
                UNKNOWN_ORDER = 5
                DUPLICATE_ORDER = 6
                DUPLICATE_OF_A_VERBALLY_COMMUNICATED_ORDER = 7
                STALE_ORDER = 8
                TRADE_ALONG_REQUIRED = 9
                INVALID_INVESTOR_ID = 10
                UNSUPPORTED_ORDER_CHARACTERISTIC = 11
                SURVEILLENCE_OPTION = 12
                INCORRECT_QUANTITY = 13
                INCORRECT_ALLOCATED_QUANTITY = 14
                UNKNOWN_ACCOUNT = 15
                PRICE_EXCEEDS_CURRENT_PRICE_BAND = 16
                INVALID_PRICE_INCREMENT = 18
                OTHER = 99

        class IOIQualifier(Tag):
            Tag = 104
            Type = "CHAR"
            class Values:
                ALL_OR_NONE = "A"
                MARKET_ON_CLOSE = "B"
                AT_THE_CLOSE = "C"
                VWAP = "D"
                IN_TOUCH_WITH = "I"
                LIMIT = "L"
                MORE_BEHIND = "M"
                AT_THE_OPEN = "O"
                TAKING_A_POSITION = "P"
                AT_THE_MARKET = "Q"
                READY_TO_TRADE = "R"
                PORTFOLIO_SHOWN = "S"
                THROUGH_THE_DAY = "T"
                VERSUS = "V"
                INDICATION = "W"
                CROSSING_OPPORTUNITY = "X"
                AT_THE_MIDPOINT = "Y"
                PRE_OPEN = "Z"

        class Issuer(Tag):
            Tag = 106
            Type = "STRING"

        class SecurityDesc(Tag):
            Tag = 107
            Type = "STRING"

        class HeartBtInt(Tag):
            Tag = 108
            Type = "INT"

        class MinQty(Tag):
            Tag = 110
            Type = "QTY"

        class MaxFloor(Tag):
            Tag = 111
            Type = "QTY"

        class TestReqID(Tag):
            Tag = 112
            Type = "STRING"

        class ReportToExch(Tag):
            Tag = 113
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class LocateReqd(Tag):
            Tag = 114
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class OnBehalfOfCompID(Tag):
            Tag = 115
            Type = "STRING"

        class OnBehalfOfSubID(Tag):
            Tag = 116
            Type = "STRING"

        class QuoteID(Tag):
            Tag = 117
            Type = "STRING"

        class NetMoney(Tag):
            Tag = 118
            Type = "AMT"

        class SettlCurrAmt(Tag):
            Tag = 119
            Type = "AMT"

        class SettlCurrency(Tag):
            Tag = 120
            Type = "CURRENCY"

        class ForexReq(Tag):
            Tag = 121
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class OrigSendingTime(Tag):
            Tag = 122
            Type = "UTCTIMESTAMP"

        class GapFillFlag(Tag):
            Tag = 123
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class NoExecs(Tag):
            Tag = 124
            Type = "NUMINGROUP"

        class ExpireTime(Tag):
            Tag = 126
            Type = "UTCTIMESTAMP"

        class DKReason(Tag):
            Tag = 127
            Type = "CHAR"
            class Values:
                UNKNOWN_SYMBOL = "A"
                WRONG_SIDE = "B"
                QUANTITY_EXCEEDS_ORDER = "C"
                NO_MATCHING_ORDER = "D"
                PRICE_EXCEEDS_LIMIT = "E"
                CALCULATION_DIFFERENCE = "F"
                OTHER = "Z"

        class DeliverToCompID(Tag):
            Tag = 128
            Type = "STRING"

        class DeliverToSubID(Tag):
            Tag = 129
            Type = "STRING"

        class IOINaturalFlag(Tag):
            Tag = 130
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class QuoteReqID(Tag):
            Tag = 131
            Type = "STRING"

        class BidPx(Tag):
            Tag = 132
            Type = "PRICE"

        class OfferPx(Tag):
            Tag = 133
            Type = "PRICE"

        class BidSize(Tag):
            Tag = 134
            Type = "QTY"

        class OfferSize(Tag):
            Tag = 135
            Type = "QTY"

        class NoMiscFees(Tag):
            Tag = 136
            Type = "NUMINGROUP"

        class MiscFeeAmt(Tag):
            Tag = 137
            Type = "AMT"

        class MiscFeeCurr(Tag):
            Tag = 138
            Type = "CURRENCY"

        class MiscFeeType(Tag):
            Tag = 139
            Type = "STRING"
            class Values:
                REGULATORY = "1"
                TAX = "2"
                LOCAL_COMMISSION = "3"
                EXCHANGE_FEES = "4"
                STAMP = "5"
                LEVY = "6"
                OTHER = "7"
                MARKUP = "8"
                CONSUMPTION_TAX = "9"
                PER_TRANSACTION = "10"
                CONVERSION = "11"
                AGENT = "12"
                TRANSFER_FEE = "13"
                SECURITY_LENDING = "14"

        class PrevClosePx(Tag):
            Tag = 140
            Type = "PRICE"

        class ResetSeqNumFlag(Tag):
            Tag = 141
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class SenderLocationID(Tag):
            Tag = 142
            Type = "STRING"

        class TargetLocationID(Tag):
            Tag = 143
            Type = "STRING"

        class OnBehalfOfLocationID(Tag):
            Tag = 144
            Type = "STRING"

        class DeliverToLocationID(Tag):
            Tag = 145
            Type = "STRING"

        class NoRelatedSym(Tag):
            Tag = 146
            Type = "NUMINGROUP"

        class Subject(Tag):
            Tag = 147
            Type = "STRING"

        class Headline(Tag):
            Tag = 148
            Type = "STRING"

        class URLLink(Tag):
            Tag = 149
            Type = "STRING"

        class ExecType(Tag):
            Tag = 150
            Type = "CHAR"
            class Values:
                NEW = "0"
                DONE_FOR_DAY = "3"
                CANCELED = "4"
                REPLACED = "5"
                PENDING_CANCEL = "6"
                STOPPED = "7"
                REJECTED = "8"
                SUSPENDED = "9"
                PENDING_NEW = "A"
                CALCULATED = "B"
                EXPIRED = "C"
                RESTATED = "D"
                PENDING_REPLACE = "E"
                TRADE = "F"
                TRADE_CORRECT = "G"
                TRADE_CANCEL = "H"
                ORDER_STATUS = "I"
                TRADE_IN_A_CLEARING_HOLD = "J"
                TRADE_HAS_BEEN_RELEASED_TO_CLEARING = "K"
                TRIGGERED_OR_ACTIVATED_BY_SYSTEM = "L"

        class LeavesQty(Tag):
            Tag = 151
            Type = "QTY"

        class CashOrderQty(Tag):
            Tag = 152
            Type = "QTY"

        class AllocAvgPx(Tag):
            Tag = 153
            Type = "PRICE"

        class AllocNetMoney(Tag):
            Tag = 154
            Type = "AMT"

        class SettlCurrFxRate(Tag):
            Tag = 155
            Type = "FLOAT"

        class SettlCurrFxRateCalc(Tag):
            Tag = 156
            Type = "CHAR"
            class Values:
                MULTIPLY = "M"
                DIVIDE = "D"

        class NumDaysInterest(Tag):
            Tag = 157
            Type = "INT"

        class AccruedInterestRate(Tag):
            Tag = 158
            Type = "PERCENTAGE"

        class AccruedInterestAmt(Tag):
            Tag = 159
            Type = "AMT"

        class SettlInstMode(Tag):
            Tag = 160
            Type = "CHAR"
            class Values:
                DEFAULT = "0"
                STANDING_INSTRUCTIONS_PROVIDED = "1"
                SPECIFIC_ALLOCATION_ACCOUNT_OVERRIDING = "2"
                SPECIFIC_ALLOCATION_ACCOUNT_STANDING = "3"
                SPECIFIC_ORDER_FOR_A_SINGLE_ACCOUNT = "4"
                REQUEST_REJECT = "5"

        class AllocText(Tag):
            Tag = 161
            Type = "STRING"

        class SettlInstID(Tag):
            Tag = 162
            Type = "STRING"

        class SettlInstTransType(Tag):
            Tag = 163
            Type = "CHAR"
            class Values:
                NEW = "N"
                CANCEL = "C"
                REPLACE = "R"
                RESTATE = "T"

        class EmailThreadID(Tag):
            Tag = 164
            Type = "STRING"

        class SettlInstSource(Tag):
            Tag = 165
            Type = "CHAR"
            class Values:
                BROKERS_INSTRUCTIONS = "1"
                INSTITUTIONS_INSTRUCTIONS = "2"
                INVESTOR = "3"

        class SecurityType(Tag):
            Tag = 167
            Type = "STRING"
            class Values:
                US_TREASURY_NOTE_UST = "UST"
                US_TREASURY_BILL_USTB = "USTB"
                EURO_SUPRANATIONAL_COUPONS = "EUSUPRA"
                FEDERAL_AGENCY_COUPON = "FAC"
                FEDERAL_AGENCY_DISCOUNT_NOTE = "FADN"
                PRIVATE_EXPORT_FUNDING = "PEF"
                USD_SUPRANATIONAL_COUPONS = "SUPRA"
                CORPORATE_BOND = "CORP"
                CORPORATE_PRIVATE_PLACEMENT = "CPP"
                CONVERTIBLE_BOND = "CB"
                DUAL_CURRENCY = "DUAL"
                EURO_CORPORATE_BOND = "EUCORP"
                EURO_CORPORATE_FLOATING_RATE_NOTES = "EUFRN"
                US_CORPORATE_FLOATING_RATE_NOTES = "FRN"
                INDEXED_LINKED = "XLINKD"
                STRUCTURED_NOTES = "STRUCT"
                YANKEE_CORPORATE_BOND = "YANK"
                FOREIGN_EXCHANGE_CONTRACT = "FOR"
                CREDIT_DEFAULT_SWAP = "CDS"
                FUTURE = "FUT"
                OPTION = "OPT"
                OPTIONS_ON_FUTURES = "OOF"
                OPTIONS_ON_PHYSICAL = "OOP"
                INTEREST_RATE_SWAP = "IRS"
                OPTIONS_ON_COMBO = "OOC"
                COMMON_STOCK = "CS"
                PREFERRED_STOCK = "PS"
                REPURCHASE = "REPO"
                FORWARD = "FORWARD"
                BUY_SELLBACK = "BUYSELL"
                SECURITIES_LOAN = "SECLOAN"
                SECURITIES_PLEDGE = "SECPLEDGE"
                BRADY_BOND = "BRADY"
                CANADIAN_TREASURY_NOTES = "CAN"
                CANADIAN_TREASURY_BILLS = "CTB"
                EURO_SOVEREIGNS = "EUSOV"
                CANADIAN_PROVINCIAL_BONDS = "PROV"
                TREASURY_BILL = "TB"
                US_TREASURY_BOND = "TBOND"
                INTEREST_STRIP_FROM_ANY_BOND_OR_NOTE = "TINT"
                US_TREASURY_BILL_TBILL = "TBILL"
                TREASURY_INFLATION_PROTECTED_SECURITIES = "TIPS"
                PRINCIPAL_STRIP_OF_A_CALLABLE_BOND_OR_NOTE = "TCAL"
                PRINCIPAL_STRIP_FROM_A_NON_CALLABLE_BOND_OR_NOTE = "TPRN"
                US_TREASURY_NOTE_TNOTE = "TNOTE"
                TERM_LOAN = "TERM"
                REVOLVER_LOAN = "RVLV"
                REVOLVER_TERM_LOAN = "RVLVTRM"
                BRIDGE_LOAN = "BRIDGE"
                LETTER_OF_CREDIT = "LOFC"
                SWING_LINE_FACILITY = "SWING"
                DEBTOR_IN_POSSESSION = "DINP"
                DEFAULTED = "DEFLTED"
                WITHDRAWN = "WITHDRN"
                REPLACED = "REPLACD"
                MATURED = "MATURED"
                AMENDED_RESTATED = "AMENDED"
                RETIRED = "RETIRED"
                BANKERS_ACCEPTANCE = "BA"
                BANK_DEPOSITORY_NOTE = "BDN"
                BANK_NOTES = "BN"
                BILL_OF_EXCHANGES = "BOX"
                CANADIAN_MONEY_MARKETS = "CAMM"
                CERTIFICATE_OF_DEPOSIT = "CD"
                CALL_LOANS = "CL"
                COMMERCIAL_PAPER = "CP"
                DEPOSIT_NOTES = "DN"
                EURO_CERTIFICATE_OF_DEPOSIT = "EUCD"
                EURO_COMMERCIAL_PAPER = "EUCP"
                LIQUIDITY_NOTE = "LQN"
                MEDIUM_TERM_NOTES = "MTN"
                OVERNIGHT = "ONITE"
                PROMISSORY_NOTE = "PN"
                SHORT_TERM_LOAN_NOTE = "STN"
                PLAZOS_FIJOS = "PZFJ"
                SECURED_LIQUIDITY_NOTE = "SLQN"
                TIME_DEPOSIT = "TD"
                TERM_LIQUIDITY_NOTE = "TLQN"
                EXTENDED_COMM_NOTE = "XCN"
                YANKEE_CERTIFICATE_OF_DEPOSIT = "YCD"
                ASSET_BACKED_SECURITIES = "ABS"
                CANADIAN_MORTGAGE_BONDS = "CMB"
                CORP_MORTGAGE_BACKED_SECURITIES = "CMBS"
                COLLATERALIZED_MORTGAGE_OBLIGATION = "CMO"
                IOETTE_MORTGAGE = "IET"
                MORTGAGE_BACKED_SECURITIES = "MBS"
                MORTGAGE_INTEREST_ONLY = "MIO"
                MORTGAGE_PRINCIPAL_ONLY = "MPO"
                MORTGAGE_PRIVATE_PLACEMENT = "MPP"
                MISCELLANEOUS_PASS_THROUGH = "MPT"
                PFANDBRIEFE = "PFAND"
                TO_BE_ANNOUNCED = "TBA"
                OTHER_ANTICIPATION_NOTES = "AN"
                CERTIFICATE_OF_OBLIGATION = "COFO"
                CERTIFICATE_OF_PARTICIPATION = "COFP"
                GENERAL_OBLIGATION_BONDS = "GO"
                MANDATORY_TENDER = "MT"
                REVENUE_ANTICIPATION_NOTE = "RAN"
                REVENUE_BONDS = "REV"
                SPECIAL_ASSESSMENT = "SPCLA"
                SPECIAL_OBLIGATION = "SPCLO"
                SPECIAL_TAX = "SPCLT"
                TAX_ANTICIPATION_NOTE = "TAN"
                TAX_ALLOCATION = "TAXA"
                TAX_EXEMPT_COMMERCIAL_PAPER = "TECP"
                TAXABLE_MUNICIPAL_CP = "TMCP"
                TAX_REVENUE_ANTICIPATION_NOTE = "TRAN"
                VARIABLE_RATE_DEMAND_NOTE = "VRDN"
                WARRANT = "WAR"
                MUTUAL_FUND = "MF"
                MULTILEG_INSTRUMENT = "MLEG"
                NO_SECURITY_TYPE = "NONE"
                WILDCARD_ENTRY_FOR_USE_ON_SECURITY_DEFINITION_REQUEST = "?"
                CASH = "CASH"
                NON_DELIVERABLE_FORWARD = "FXNDF"
                FX_SPOT = "FXSPOT"
                FX_FORWARD = "FXFWD"
                FX_SWAP = "FXSWAP"

        class EffectiveTime(Tag):
            Tag = 168
            Type = "UTCTIMESTAMP"

        class StandInstDbType(Tag):
            Tag = 169
            Type = "INT"
            class Values:
                OTHER = 0
                DTC_SID = 1
                THOMSON_ALERT = 2
                A_GLOBAL_CUSTODIAN = 3
                ACCOUNTNET = 4

        class StandInstDbName(Tag):
            Tag = 170
            Type = "STRING"

        class StandInstDbID(Tag):
            Tag = 171
            Type = "STRING"

        class SettlDeliveryType(Tag):
            Tag = 172
            Type = "INT"
            class Values:
                VERSUS_PAYMENT_DELIVER = 0
                FREE_DELIVER = 1
                TRI_PARTY = 2
                HOLD_IN_CUSTODY = 3

        class BidSpotRate(Tag):
            Tag = 188
            Type = "PRICE"

        class BidForwardPoints(Tag):
            Tag = 189
            Type = "PRICEOFFSET"

        class OfferSpotRate(Tag):
            Tag = 190
            Type = "PRICE"

        class OfferForwardPoints(Tag):
            Tag = 191
            Type = "PRICEOFFSET"

        class OrderQty2(Tag):
            Tag = 192
            Type = "QTY"

        class SettlDate2(Tag):
            Tag = 193
            Type = "LOCALMKTDATE"

        class LastSpotRate(Tag):
            Tag = 194
            Type = "PRICE"

        class LastForwardPoints(Tag):
            Tag = 195
            Type = "PRICEOFFSET"

        class AllocLinkID(Tag):
            Tag = 196
            Type = "STRING"

        class AllocLinkType(Tag):
            Tag = 197
            Type = "INT"
            class Values:
                FX_NETTING = 0
                FX_SWAP = 1

        class SecondaryOrderID(Tag):
            Tag = 198
            Type = "STRING"

        class NoIOIQualifiers(Tag):
            Tag = 199
            Type = "NUMINGROUP"

        class MaturityMonthYear(Tag):
            Tag = 200
            Type = "MONTHYEAR"

        class PutOrCall(Tag):
            Tag = 201
            Type = "INT"
            class Values:
                PUT = 0
                CALL = 1

        class StrikePrice(Tag):
            Tag = 202
            Type = "PRICE"

        class CoveredOrUncovered(Tag):
            Tag = 203
            Type = "INT"
            class Values:
                COVERED = 0
                UNCOVERED = 1

        class OptAttribute(Tag):
            Tag = 206
            Type = "CHAR"

        class SecurityExchange(Tag):
            Tag = 207
            Type = "EXCHANGE"

        class NotifyBrokerOfCredit(Tag):
            Tag = 208
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class AllocHandlInst(Tag):
            Tag = 209
            Type = "INT"
            class Values:
                MATCH = 1
                FORWARD = 2
                FORWARD_AND_MATCH = 3

        class MaxShow(Tag):
            Tag = 210
            Type = "QTY"

        class PegOffsetValue(Tag):
            Tag = 211
            Type = "FLOAT"

        class XmlDataLen(Tag):
            Tag = 212
            Type = "LENGTH"

        class XmlData(Tag):
            Tag = 213
            Type = "DATA"

        class SettlInstRefID(Tag):
            Tag = 214
            Type = "STRING"

        class NoRoutingIDs(Tag):
            Tag = 215
            Type = "NUMINGROUP"

        class RoutingType(Tag):
            Tag = 216
            Type = "INT"
            class Values:
                TARGET_FIRM = 1
                TARGET_LIST = 2
                BLOCK_FIRM = 3
                BLOCK_LIST = 4

        class RoutingID(Tag):
            Tag = 217
            Type = "STRING"

        class Spread(Tag):
            Tag = 218
            Type = "PRICEOFFSET"

        class BenchmarkCurveCurrency(Tag):
            Tag = 220
            Type = "CURRENCY"

        class BenchmarkCurveName(Tag):
            Tag = 221
            Type = "STRING"
            class Values:
                EONIA = "EONIA"
                EUREPO = "EUREPO"
                EURIBOR = "Euribor"
                FUTURESWAP = "FutureSWAP"
                LIBID = "LIBID"
                LIBOR = "LIBOR"
                MUNIAAA = "MuniAAA"
                OTHER = "OTHER"
                PFANDBRIEFE = "Pfandbriefe"
                SONIA = "SONIA"
                SWAP = "SWAP"
                TREASURY = "Treasury"

        class BenchmarkCurvePoint(Tag):
            Tag = 222
            Type = "STRING"

        class CouponRate(Tag):
            Tag = 223
            Type = "PERCENTAGE"

        class CouponPaymentDate(Tag):
            Tag = 224
            Type = "LOCALMKTDATE"

        class IssueDate(Tag):
            Tag = 225
            Type = "LOCALMKTDATE"

        class RepurchaseTerm(Tag):
            Tag = 226
            Type = "INT"

        class RepurchaseRate(Tag):
            Tag = 227
            Type = "PERCENTAGE"

        class Factor(Tag):
            Tag = 228
            Type = "FLOAT"

        class TradeOriginationDate(Tag):
            Tag = 229
            Type = "LOCALMKTDATE"

        class ExDate(Tag):
            Tag = 230
            Type = "LOCALMKTDATE"

        class ContractMultiplier(Tag):
            Tag = 231
            Type = "FLOAT"

        class NoStipulations(Tag):
            Tag = 232
            Type = "NUMINGROUP"

        class StipulationType(Tag):
            Tag = 233
            Type = "STRING"
            class Values:
                ALTERNATIVE_MINIMUM_TAX = "AMT"
                AUTO_REINVESTMENT_AT_RATE_OR_BETTER = "AUTOREINV"
                BANK_QUALIFIED = "BANKQUAL"
                BARGAIN_CONDITIONS = "BGNCON"
                COUPON_RANGE = "COUPON"
                ISO_CURRENCY_CODE = "CURRENCY"
                CUSTOM_START_END_DATE = "CUSTOMDATE"
                GEOGRAPHICS_AND_RANGE = "GEOG"
                VALUATION_DISCOUNT = "HAIRCUT"
                INSURED = "INSURED"
                YEAR_OR_YEAR_MONTH_OF_ISSUE = "ISSUE"
                ISSUERS_TICKER = "ISSUER"
                ISSUE_SIZE_RANGE = "ISSUESIZE"
                LOOKBACK_DAYS = "LOOKBACK"
                EXPLICIT_LOT_IDENTIFIER = "LOT"
                LOT_VARIANCE = "LOTVAR"
                MATURITY_YEAR_AND_MONTH = "MAT"
                MATURITY_RANGE = "MATURITY"
                MAXIMUM_SUBSTITUTIONS = "MAXSUBS"
                MINIMUM_DENOMINATION = "MINDNOM"
                MINIMUM_INCREMENT = "MININCR"
                MINIMUM_QUANTITY = "MINQTY"
                PAYMENT_FREQUENCY_CALENDAR = "PAYFREQ"
                NUMBER_OF_PIECES = "PIECES"
                POOLS_MAXIMUM = "PMAX"
                POOLS_PER_LOT = "PPL"
                POOLS_PER_MILLION = "PPM"
                POOLS_PER_TRADE = "PPT"
                PRICE_RANGE = "PRICE"
                PRICING_FREQUENCY = "PRICEFREQ"
                PRODUCTION_YEAR = "PROD"
                CALL_PROTECTION = "PROTECT"
                PURPOSE = "PURPOSE"
                BENCHMARK_PRICE_SOURCE = "PXSOURCE"
                RATING_SOURCE_AND_RANGE = "RATING"
                TYPE_OF_REDEMPTION = "REDEMPTION"
                RESTRICTED = "RESTRICTED"
                MARKET_SECTOR = "SECTOR"
                SECURITY_TYPE_INCLUDED_OR_EXCLUDED = "SECTYPE"
                STRUCTURE = "STRUCT"
                SUBSTITUTIONS_FREQUENCY = "SUBSFREQ"
                SUBSTITUTIONS_LEFT = "SUBSLEFT"
                FREEFORM_TEXT = "TEXT"
                TRADE_VARIANCE = "TRDVAR"
                WEIGHTED_AVERAGE_COUPON = "WAC"
                WEIGHTED_AVERAGE_LIFE_COUPON = "WAL"
                WEIGHTED_AVERAGE_LOAN_AGE = "WALA"
                WEIGHTED_AVERAGE_MATURITY = "WAM"
                WHOLE_POOL = "WHOLE"
                YIELD_RANGE = "YIELD"
                AVERAGE_FICO_SCORE = "AVFICO"
                AVERAGE_LOAN_SIZE = "AVSIZE"
                MAXIMUM_LOAN_BALANCE = "MAXBAL"
                POOL_IDENTIFIER = "POOL"
                TYPE_OF_ROLL_TRADE = "ROLLTYPE"
                REFERENCE_TO_ROLLING_OR_CLOSING_TRADE = "REFTRADE"
                PRINCIPAL_OF_ROLLING_OR_CLOSING_TRADE = "REFPRIN"
                INTEREST_OF_ROLLING_OR_CLOSING_TRADE = "REFINT"
                AVAILABLE_OFFER_QUANTITY_TO_BE_SHOWN_TO_THE_STREET = "AVAILQTY"
                BROKERS_SALES_CREDIT = "BROKERCREDIT"
                OFFER_PRICE_TO_BE_SHOWN_TO_INTERNAL_BROKERS = "INTERNALPX"
                OFFER_QUANTITY_TO_BE_SHOWN_TO_INTERNAL_BROKERS = "INTERNALQTY"
                THE_MINIMUM_RESIDUAL_OFFER_QUANTITY = "LEAVEQTY"
                MAXIMUM_ORDER_SIZE = "MAXORDQTY"
                ORDER_QUANTITY_INCREMENT = "ORDRINCR"
                PRIMARY_OR_SECONDARY_MARKET_INDICATOR = "PRIMARY"
                BROKER_SALES_CREDIT_OVERRIDE = "SALESCREDITOVR"
                TRADERS_CREDIT = "TRADERCREDIT"
                DISCOUNT_RATE = "DISCOUNT"
                YIELD_TO_MATURITY = "YTM"
                ABSOLUTE_PREPAYMENT_SPEED = "ABS"
                CONSTANT_PREPAYMENT_PENALTY = "CPP"
                CONSTANT_PREPAYMENT_RATE = "CPR"
                CONSTANT_PREPAYMENT_YIELD = "CPY"
                FINAL_CPR_OF_HOME_EQUITY_PREPAYMENT_CURVE = "HEP"
                PERCENT_OF_MANUFACTURED_HOUSING_PREPAYMENT_CURVE = "MHP"
                MONTHLY_PREPAYMENT_RATE = "MPR"
                PERCENT_OF_PROSPECTUS_PREPAYMENT_CURVE = "PPC"
                PERCENT_OF_BMA_PREPAYMENT_CURVE = "PSA"
                SINGLE_MONTHLY_MORTALITY = "SMM"

        class StipulationValue(Tag):
            Tag = 234
            Type = "STRING"

        class YieldType(Tag):
            Tag = 235
            Type = "STRING"
            class Values:
                AFTER_TAX_YIELD = "AFTERTAX"
                ANNUAL_YIELD = "ANNUAL"
                YIELD_AT_ISSUE = "ATISSUE"
                YIELD_TO_AVG_MATURITY = "AVGMATURITY"
                BOOK_YIELD = "BOOK"
                YIELD_TO_NEXT_CALL = "CALL"
                YIELD_CHANGE_SINCE_CLOSE = "CHANGE"
                CLOSING_YIELD = "CLOSE"
                COMPOUND_YIELD = "COMPOUND"
                CURRENT_YIELD = "CURRENT"
                GVNT_EQUIVALENT_YIELD = "GOVTEQUIV"
                TRUE_GROSS_YIELD = "GROSS"
                YIELD_WITH_INFLATION_ASSUMPTION = "INFLATION"
                INVERSE_FLOATER_BOND_YIELD = "INVERSEFLOATER"
                MOST_RECENT_CLOSING_YIELD = "LASTCLOSE"
                CLOSING_YIELD_MOST_RECENT_MONTH = "LASTMONTH"
                CLOSING_YIELD_MOST_RECENT_QUARTER = "LASTQUARTER"
                CLOSING_YIELD_MOST_RECENT_YEAR = "LASTYEAR"
                YIELD_TO_LONGEST_AVERAGE_LIFE = "LONGAVGLIFE"
                MARK_TO_MARKET_YIELD = "MARK"
                YIELD_TO_MATURITY = "MATURITY"
                YIELD_TO_NEXT_REFUND = "NEXTREFUND"
                OPEN_AVERAGE_YIELD = "OPENAVG"
                PREVIOUS_CLOSE_YIELD = "PREVCLOSE"
                PROCEEDS_YIELD = "PROCEEDS"
                YIELD_TO_NEXT_PUT = "PUT"
                SEMI_ANNUAL_YIELD = "SEMIANNUAL"
                YIELD_TO_SHORTEST_AVERAGE_LIFE = "SHORTAVGLIFE"
                SIMPLE_YIELD = "SIMPLE"
                TAX_EQUIVALENT_YIELD = "TAXEQUIV"
                YIELD_TO_TENDER_DATE = "TENDER"
                TRUE_YIELD = "TRUE"
                YIELD_VALUE_OF_1_32 = "VALUE1_32"
                YIELD_TO_WORST = "WORST"

        class Yield(Tag):
            Tag = 236
            Type = "PERCENTAGE"

        class TotalTakedown(Tag):
            Tag = 237
            Type = "AMT"

        class Concession(Tag):
            Tag = 238
            Type = "AMT"

        class RepoCollateralSecurityType(Tag):
            Tag = 239
            Type = "STRING"

        class RedemptionDate(Tag):
            Tag = 240
            Type = "LOCALMKTDATE"

        class UnderlyingCouponPaymentDate(Tag):
            Tag = 241
            Type = "LOCALMKTDATE"

        class UnderlyingIssueDate(Tag):
            Tag = 242
            Type = "LOCALMKTDATE"

        class UnderlyingRepoCollateralSecurityType(Tag):
            Tag = 243
            Type = "STRING"

        class UnderlyingRepurchaseTerm(Tag):
            Tag = 244
            Type = "INT"

        class UnderlyingRepurchaseRate(Tag):
            Tag = 245
            Type = "PERCENTAGE"

        class UnderlyingFactor(Tag):
            Tag = 246
            Type = "FLOAT"

        class UnderlyingRedemptionDate(Tag):
            Tag = 247
            Type = "LOCALMKTDATE"

        class LegCouponPaymentDate(Tag):
            Tag = 248
            Type = "LOCALMKTDATE"

        class LegIssueDate(Tag):
            Tag = 249
            Type = "LOCALMKTDATE"

        class LegRepoCollateralSecurityType(Tag):
            Tag = 250
            Type = "STRING"

        class LegRepurchaseTerm(Tag):
            Tag = 251
            Type = "INT"

        class LegRepurchaseRate(Tag):
            Tag = 252
            Type = "PERCENTAGE"

        class LegFactor(Tag):
            Tag = 253
            Type = "FLOAT"

        class LegRedemptionDate(Tag):
            Tag = 254
            Type = "LOCALMKTDATE"

        class CreditRating(Tag):
            Tag = 255
            Type = "STRING"

        class UnderlyingCreditRating(Tag):
            Tag = 256
            Type = "STRING"

        class LegCreditRating(Tag):
            Tag = 257
            Type = "STRING"

        class TradedFlatSwitch(Tag):
            Tag = 258
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class BasisFeatureDate(Tag):
            Tag = 259
            Type = "LOCALMKTDATE"

        class BasisFeaturePrice(Tag):
            Tag = 260
            Type = "PRICE"

        class MDReqID(Tag):
            Tag = 262
            Type = "STRING"

        class SubscriptionRequestType(Tag):
            Tag = 263
            Type = "CHAR"
            class Values:
                SNAPSHOT = "0"
                SNAPSHOT_PLUS_UPDATES = "1"
                DISABLE_PREVIOUS_SNAPSHOT_PLUS_UPDATE_REQUEST = "2"

        class MarketDepth(Tag):
            Tag = 264
            Type = "INT"

        class MDUpdateType(Tag):
            Tag = 265
            Type = "INT"
            class Values:
                FULL_REFRESH = 0
                INCREMENTAL_REFRESH = 1

        class AggregatedBook(Tag):
            Tag = 266
            Type = "BOOLEAN"
            class Values:
                YES = 1
                NO = 0

        class NoMDEntryTypes(Tag):
            Tag = 267
            Type = "NUMINGROUP"

        class NoMDEntries(Tag):
            Tag = 268
            Type = "NUMINGROUP"

        class MDEntryType(Tag):
            Tag = 269
            Type = "CHAR"
            class Values:
                BID = "0"
                OFFER = "1"
                TRADE = "2"
                INDEX_VALUE = "3"
                OPENING_PRICE = "4"
                CLOSING_PRICE = "5"
                SETTLEMENT_PRICE = "6"
                TRADING_SESSION_HIGH_PRICE = "7"
                TRADING_SESSION_LOW_PRICE = "8"
                TRADING_SESSION_VWAP_PRICE = "9"
                IMBALANCE = "A"
                TRADE_VOLUME = "B"
                OPEN_INTEREST = "C"
                COMPOSITE_UNDERLYING_PRICE = "D"
                SIMULATED_SELL_PRICE = "E"
                SIMULATED_BUY_PRICE = "F"
                MARGIN_RATE = "G"
                MID_PRICE = "H"
                EMPTY_BOOK = "J"
                SETTLE_HIGH_PRICE = "K"
                SETTLE_LOW_PRICE = "L"
                PRIOR_SETTLE_PRICE = "M"
                SESSION_HIGH_BID = "N"
                SESSION_LOW_OFFER = "O"
                EARLY_PRICES = "P"
                AUCTION_CLEARING_PRICE = "Q"
                SWAP_VALUE_FACTOR = "S"
                DAILY_VALUE_ADJUSTMENT_FOR_LONG_POSITIONS = "R"
                CUMULATIVE_VALUE_ADJUSTMENT_FOR_LONG_POSITIONS = "T"
                DAILY_VALUE_ADJUSTMENT_FOR_SHORT_POSITIONS = "U"
                CUMULATIVE_VALUE_ADJUSTMENT_FOR_SHORT_POSITIONS = "V"
                RECOVERY_RATE = "Y"
                RECOVERY_RATE_FOR_LONG = "Z"
                RECOVERY_RATE_FOR_SHORT = "a"
                FIXING_PRICE = "W"
                CASH_RATE = "X"

        class MDEntryPx(Tag):
            Tag = 270
            Type = "PRICE"

        class MDEntrySize(Tag):
            Tag = 271
            Type = "QTY"

        class MDEntryDate(Tag):
            Tag = 272
            Type = "UTCDATEONLY"

        class MDEntryTime(Tag):
            Tag = 273
            Type = "UTCTIMEONLY"

        class TickDirection(Tag):
            Tag = 274
            Type = "CHAR"
            class Values:
                PLUS_TICK = "0"
                ZERO_PLUS_TICK = "1"
                MINUS_TICK = "2"
                ZERO_MINUS_TICK = "3"

        class MDMkt(Tag):
            Tag = 275
            Type = "EXCHANGE"

        class QuoteCondition(Tag):
            Tag = 276
            Type = "MULTIPLESTRINGVALUE"
            class Values:
                OPEN_ACTIVE = "A"
                CLOSED_INACTIVE = "B"
                EXCHANGE_BEST = "C"
                CONSOLIDATED_BEST = "D"
                LOCKED = "E"
                CROSSED = "F"
                DEPTH = "G"
                FAST_TRADING = "H"
                NON_FIRM = "I"
                MANUAL_SLOW_QUOTE = "L"
                OUTRIGHT_PRICE = "J"
                IMPLIED_PRICE = "K"
                DEPTH_ON_OFFER = "M"
                DEPTH_ON_BID = "N"
                CLOSING = "O"
                NEWS_DISSEMINATION = "P"
                TRADING_RANGE = "Q"
                ORDER_INFLUX = "R"
                DUE_TO_RELATED = "S"
                NEWS_PENDING = "T"
                ADDITIONAL_INFO = "U"
                ADDITIONAL_INFO_DUE_TO_RELATED = "V"
                RESUME = "W"
                VIEW_OF_COMMON = "X"
                VOLUME_ALERT = "Y"
                ORDER_IMBALANCE = "Z"
                EQUIPMENT_CHANGEOVER = "a"
                NO_OPEN = "b"
                REGULAR_ETH = "c"
                AUTOMATIC_EXECUTION = "d"
                AUTOMATIC_EXECUTION_ETH = "e"
                FAST_MARKET_ETH = "f "
                INACTIVE_ETH = "g"
                ROTATION = "h"
                ROTATION_ETH = "i"
                HALT = "j"
                HALT_ETH = "k"
                DUE_TO_NEWS_DISSEMINATION = "l"
                DUE_TO_NEWS_PENDING = "m"
                TRADING_RESUME = "n"
                OUT_OF_SEQUENCE = "o"
                BID_SPECIALIST = "p"
                OFFER_SPECIALIST = "q"
                BID_OFFER_SPECIALIST = "r"
                END_OF_DAY_SAM = "s"
                FORBIDDEN_SAM = "t"
                FROZEN_SAM = "u"
                PREOPENING_SAM = "v"
                OPENING_SAM = "w"
                OPEN_SAM = "x"
                SURVEILLANCE_SAM = "y"
                SUSPENDED_SAM = "z"
                RESERVED_SAM = "0"
                NO_ACTIVE_SAM = "1"
                RESTRICTED = "2"
                REST_OF_BOOK_VWAP = "3"
                BETTER_PRICES_IN_CONDITIONAL_ORDERS = "4"
                MEDIAN_PRICE = "5"
                FULL_CURVE = "6"
                FLAT_CURVE = "7"

        class TradeCondition(Tag):
            Tag = 277
            Type = "MULTIPLESTRINGVALUE"
            class Values:
                CASH = "A"
                AVERAGE_PRICE_TRADE = "B"
                CASH_TRADE = "C"
                NEXT_DAY = "D"
                OPENING_REOPENING_TRADE_DETAIL = "E"
                INTRADAY_TRADE_DETAIL = "F"
                RULE_127_TRADE = "G"
                RULE_155_TRADE = "H"
                SOLD_LAST = "I"
                NEXT_DAY_TRADE = "J"
                OPENED = "K"
                SELLER = "L"
                SOLD = "M"
                STOPPED_STOCK = "N"
                IMBALANCE_MORE_BUYERS = "P"
                IMBALANCE_MORE_SELLERS = "Q"
                OPENING_PRICE = "R"
                BARGAIN_CONDITION = "S"
                CONVERTED_PRICE_INDICATOR = "T"
                EXCHANGE_LAST = "U"
                FINAL_PRICE_OF_SESSION = "V"
                EX_PIT = "W"
                CROSSED_X = "X"
                TRADES_RESULTING_FROM_MANUAL_SLOW_QUOTE = "Y"
                TRADES_RESULTING_FROM_INTERMARKET_SWEEP = "Z"
                VOLUME_ONLY = "a"
                DIRECT_PLUS = "b"
                ACQUISITION = "c"
                BUNCHED = "d"
                DISTRIBUTION = "e"
                BUNCHED_SALE = "f"
                SPLIT_TRADE = "g"
                CANCEL_STOPPED = "h"
                CANCEL_ETH = "i"
                CANCEL_STOPPED_ETH = "j"
                OUT_OF_SEQUENCE_ETH = "k"
                CANCEL_LAST_ETH = "l"
                SOLD_LAST_SALE_ETH = "m"
                CANCEL_LAST = "n"
                SOLD_LAST_SALE = "o"
                CANCEL_OPEN = "p"
                CANCEL_OPEN_ETH = "q"
                OPENED_SALE_ETH = "r"
                CANCEL_ONLY = "s"
                CANCEL_ONLY_ETH = "t"
                LATE_OPEN_ETH = "u"
                AUTO_EXECUTION_ETH = "v"
                REOPEN = "w"
                REOPEN_ETH = "x"
                ADJUSTED = "y"
                ADJUSTED_ETH = "z"
                SPREAD = "AA"
                SPREAD_ETH = "AB"
                STRADDLE = "AC"
                STRADDLE_ETH = "AD"
                STOPPED = "AE"
                STOPPED_ETH = "AF"
                REGULAR_ETH = "AG"
                COMBO = "AH"
                COMBO_ETH = "AI"
                OFFICIAL_CLOSING_PRICE = "AJ"
                PRIOR_REFERENCE_PRICE = "AK"
                CANCEL = "0"
                STOPPED_SOLD_LAST = "AL"
                STOPPED_OUT_OF_SEQUENCE = "AM"
                OFFICAL_CLOSING_PRICE = "AN"
                CROSSED_AO = "AO"
                FAST_MARKET = "AP"
                AUTOMATIC_EXECUTION = "AQ"
                FORM_T = "AR"
                BASKET_INDEX = "AS"
                BURST_BASKET = "AT"
                OUTSIDE_SPREAD = "AV"
                IMPLIED_TRADE = "1"
                MARKETPLACE_ENTERED_TRADE = "2"
                MULT_ASSET_CLASS_MULTILEG_TRADE = "3"
                MULTILEG_TO_MULTILEG_TRADE = "4"

        class MDEntryID(Tag):
            Tag = 278
            Type = "STRING"

        class MDUpdateAction(Tag):
            Tag = 279
            Type = "CHAR"
            class Values:
                NEW = "0"
                CHANGE = "1"
                DELETE = "2"
                DELETE_THRU = "3"
                DELETE_FROM = "4"
                OVERLAY = "5"

        class MDEntryRefID(Tag):
            Tag = 280
            Type = "STRING"

        class MDReqRejReason(Tag):
            Tag = 281
            Type = "CHAR"
            class Values:
                UNKNOWN_SYMBOL = "0"
                DUPLICATE_MDREQID = "1"
                INSUFFICIENT_BANDWIDTH = "2"
                INSUFFICIENT_PERMISSIONS = "3"
                UNSUPPORTED_SUBSCRIPTIONREQUESTTYPE = "4"
                UNSUPPORTED_MARKETDEPTH = "5"
                UNSUPPORTED_MDUPDATETYPE = "6"
                UNSUPPORTED_AGGREGATEDBOOK = "7"
                UNSUPPORTED_MDENTRYTYPE = "8"
                UNSUPPORTED_TRADINGSESSIONID = "9"
                UNSUPPORTED_SCOPE = "A"
                UNSUPPORTED_OPENCLOSESETTLEFLAG = "B"
                UNSUPPORTED_MDIMPLICITDELETE = "C"
                INSUFFICIENT_CREDIT = "D"

        class MDEntryOriginator(Tag):
            Tag = 282
            Type = "STRING"

        class LocationID(Tag):
            Tag = 283
            Type = "STRING"

        class DeskID(Tag):
            Tag = 284
            Type = "STRING"

        class DeleteReason(Tag):
            Tag = 285
            Type = "CHAR"
            class Values:
                CANCELLATION = "0"
                ERROR = "1"

        class OpenCloseSettlFlag(Tag):
            Tag = 286
            Type = "MULTIPLECHARVALUE"
            class Values:
                DAILY_OPEN = "0"
                SESSION_OPEN = "1"
                DELIVERY_SETTLEMENT_ENTRY = "2"
                EXPECTED_ENTRY = "3"
                ENTRY_FROM_PREVIOUS_BUSINESS_DAY = "4"
                THEORETICAL_PRICE_VALUE = "5"

        class SellerDays(Tag):
            Tag = 287
            Type = "INT"

        class MDEntryBuyer(Tag):
            Tag = 288
            Type = "STRING"

        class MDEntrySeller(Tag):
            Tag = 289
            Type = "STRING"

        class MDEntryPositionNo(Tag):
            Tag = 290
            Type = "INT"

        class FinancialStatus(Tag):
            Tag = 291
            Type = "MULTIPLECHARVALUE"
            class Values:
                BANKRUPT = "1"
                PENDING_DELISTING = "2"
                RESTRICTED = "3"

        class CorporateAction(Tag):
            Tag = 292
            Type = "MULTIPLECHARVALUE"
            class Values:
                EX_DIVIDEND = "A"
                EX_DISTRIBUTION = "B"
                EX_RIGHTS = "C"
                NEW = "D"
                EX_INTEREST = "E"
                CASH_DIVIDEND = "F"
                STOCK_DIVIDEND = "G"
                NON_INTEGER_STOCK_SPLIT = "H"
                REVERSE_STOCK_SPLIT = "I"
                STANDARD_INTEGER_STOCK_SPLIT = "J"
                POSITION_CONSOLIDATION = "K"
                LIQUIDATION_REORGANIZATION = "L"
                MERGER_REORGANIZATION = "M"
                RIGHTS_OFFERING = "N"
                SHAREHOLDER_MEETING = "O"
                SPINOFF = "P"
                TENDER_OFFER = "Q"
                WARRANT = "R"
                SPECIAL_ACTION = "S"
                SYMBOL_CONVERSION = "T"
                CUSIP = "U"
                LEAP_ROLLOVER = "V"
                SUCCESSION_EVENT = "W"

        class DefBidSize(Tag):
            Tag = 293
            Type = "QTY"

        class DefOfferSize(Tag):
            Tag = 294
            Type = "QTY"

        class NoQuoteEntries(Tag):
            Tag = 295
            Type = "NUMINGROUP"

        class NoQuoteSets(Tag):
            Tag = 296
            Type = "NUMINGROUP"

        class QuoteStatus(Tag):
            Tag = 297
            Type = "INT"
            class Values:
                ACCEPTED = 0
                CANCEL_FOR_SYMBOL = 1
                CANCELED_FOR_SECURITY_TYPE = 2
                CANCELED_FOR_UNDERLYING = 3
                CANCELED_ALL = 4
                REJECTED = 5
                REMOVED_FROM_MARKET = 6
                EXPIRED = 7
                QUERY = 8
                QUOTE_NOT_FOUND = 9
                PENDING = 10
                PASS = 11
                LOCKED_MARKET_WARNING = 12
                CROSS_MARKET_WARNING = 13
                CANCELED_DUE_TO_LOCK_MARKET = 14
                CANCELED_DUE_TO_CROSS_MARKET = 15
                ACTIVE = 16
                CANCELED = 17
                UNSOLICITED_QUOTE_REPLENISHMENT = 18
                PENDING_END_TRADE = 19
                TOO_LATE_TO_END = 20

        class QuoteCancelType(Tag):
            Tag = 298
            Type = "INT"
            class Values:
                CANCEL_FOR_ONE_OR_MORE_SECURITIES = 1
                CANCEL_FOR_SECURITY_TYPE = 2
                CANCEL_FOR_UNDERLYING_SECURITY = 3
                CANCEL_ALL_QUOTES = 4
                CANCEL_QUOTE_SPECIFIED_IN_QUOTEID = 5
                CANCEL_BY_QUOTETYPE = 6
                CANCEL_FOR_SECURITY_ISSUER = 7
                CANCEL_FOR_ISSUER_OF_UNDERLYING_SECURITY = 8

        class QuoteEntryID(Tag):
            Tag = 299
            Type = "STRING"

        class QuoteRejectReason(Tag):
            Tag = 300
            Type = "INT"
            class Values:
                UNKNOWN_SYMBOL = 1
                EXCHANGE = 2
                QUOTE_REQUEST_EXCEEDS_LIMIT = 3
                TOO_LATE_TO_ENTER = 4
                UNKNOWN_QUOTE = 5
                DUPLICATE_QUOTE = 6
                INVALID_BID_ASK_SPREAD = 7
                INVALID_PRICE = 8
                NOT_AUTHORIZED_TO_QUOTE_SECURITY = 9
                PRICE_EXCEEDS_CURRENT_PRICE_BAND = 10
                QUOTE_LOCKED = 11
                OTHER = 99
                INVALID_OR_UNKNOWN_SECURITY_ISSUER = 12
                INVALID_OR_UNKNOWN_ISSUER_OF_UNDERLYING_SECURITY = 13

        class QuoteResponseLevel(Tag):
            Tag = 301
            Type = "INT"
            class Values:
                NO_ACKNOWLEDGEMENT = 0
                ACKNOWLEDGE_ONLY_NEGATIVE_OR_ERRONEOUS_QUOTES = 1
                ACKNOWLEDGE_EACH_QUOTE_MESSAGE = 2
                SUMMARY_ACKNOWLEDGEMENT = 3

        class QuoteSetID(Tag):
            Tag = 302
            Type = "STRING"

        class QuoteRequestType(Tag):
            Tag = 303
            Type = "INT"
            class Values:
                MANUAL = 1
                AUTOMATIC = 2

        class TotNoQuoteEntries(Tag):
            Tag = 304
            Type = "INT"

        class UnderlyingSecurityIDSource(Tag):
            Tag = 305
            Type = "STRING"

        class UnderlyingIssuer(Tag):
            Tag = 306
            Type = "STRING"

        class UnderlyingSecurityDesc(Tag):
            Tag = 307
            Type = "STRING"

        class UnderlyingSecurityExchange(Tag):
            Tag = 308
            Type = "EXCHANGE"

        class UnderlyingSecurityID(Tag):
            Tag = 309
            Type = "STRING"

        class UnderlyingSecurityType(Tag):
            Tag = 310
            Type = "STRING"

        class UnderlyingSymbol(Tag):
            Tag = 311
            Type = "STRING"

        class UnderlyingSymbolSfx(Tag):
            Tag = 312
            Type = "STRING"

        class UnderlyingMaturityMonthYear(Tag):
            Tag = 313
            Type = "MONTHYEAR"

        class UnderlyingPutOrCall(Tag):
            Tag = 315
            Type = "INT"

        class UnderlyingStrikePrice(Tag):
            Tag = 316
            Type = "PRICE"

        class UnderlyingOptAttribute(Tag):
            Tag = 317
            Type = "CHAR"

        class UnderlyingCurrency(Tag):
            Tag = 318
            Type = "CURRENCY"

        class SecurityReqID(Tag):
            Tag = 320
            Type = "STRING"

        class SecurityRequestType(Tag):
            Tag = 321
            Type = "INT"
            class Values:
                REQUEST_SECURITY_IDENTITY_AND_SPECIFICATIONS = 0
                REQUEST_SECURITY_IDENTITY_FOR_THE_SPECIFICATIONS_PROVIDED = 1
                REQUEST_LIST_SECURITY_TYPES = 2
                REQUEST_LIST_SECURITIES = 3
                SYMBOL = 4
                SECURITYTYPE_AND_OR_CFICODE = 5
                PRODUCT = 6
                TRADINGSESSIONID = 7
                ALL_SECURITIES = 8
                MARKETID_OR_MARKETID_PLUS_MARKETSEGMENTID = 9

        class SecurityResponseID(Tag):
            Tag = 322
            Type = "STRING"

        class SecurityResponseType(Tag):
            Tag = 323
            Type = "INT"
            class Values:
                ACCEPT_SECURITY_PROPOSAL_AS_IS = 1
                ACCEPT_SECURITY_PROPOSAL_WITH_REVISIONS_AS_INDICATED_IN_THE_MESSAGE = 2
                LIST_OF_SECURITY_TYPES_RETURNED_PER_REQUEST = 3
                LIST_OF_SECURITIES_RETURNED_PER_REQUEST = 4
                REJECT_SECURITY_PROPOSAL = 5
                CANNOT_MATCH_SELECTION_CRITERIA = 6

        class SecurityStatusReqID(Tag):
            Tag = 324
            Type = "STRING"

        class UnsolicitedIndicator(Tag):
            Tag = 325
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class SecurityTradingStatus(Tag):
            Tag = 326
            Type = "INT"
            class Values:
                OPENING_DELAY = 1
                TRADING_HALT = 2
                RESUME = 3
                NO_OPEN = 4
                PRICE_INDICATION = 5
                TRADING_RANGE_INDICATION = 6
                MARKET_IMBALANCE_BUY = 7
                MARKET_IMBALANCE_SELL = 8
                MARKET_ON_CLOSE_IMBALANCE_BUY = 9
                MARKET_ON_CLOSE_IMBALANCE_SELL = 10
                NO_MARKET_IMBALANCE = 12
                NO_MARKET_ON_CLOSE_IMBALANCE = 13
                ITS_PRE_OPENING = 14
                NEW_PRICE_INDICATION = 15
                TRADE_DISSEMINATION_TIME = 16
                READY_TO_TRADE = 17
                NOT_AVAILABLE_FOR_TRADING = 18
                NOT_TRADED_ON_THIS_MARKET = 19
                UNKNOWN_OR_INVALID = 20
                PRE_OPEN = 21
                OPENING_ROTATION = 22
                FAST_MARKET = 23
                PRE_CROSS = 24
                CROSS = 25
                POST_CLOSE = 26

        class HaltReasonInt(Tag):
            Tag = 327
            Type = "INT"
            class Values:
                NEWS_DISSEMINATION = 0
                ORDER_INFLUX = 1
                ORDER_IMBALANCE = 2
                ADDITIONAL_INFORMATION = 3
                NEWS_PENDING = 4
                EQUIPMENT_CHANGEOVER = 5

        class InViewOfCommon(Tag):
            Tag = 328
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class DueToRelated(Tag):
            Tag = 329
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class BuyVolume(Tag):
            Tag = 330
            Type = "QTY"

        class SellVolume(Tag):
            Tag = 331
            Type = "QTY"

        class HighPx(Tag):
            Tag = 332
            Type = "PRICE"

        class LowPx(Tag):
            Tag = 333
            Type = "PRICE"

        class Adjustment(Tag):
            Tag = 334
            Type = "INT"
            class Values:
                CANCEL = 1
                ERROR = 2
                CORRECTION = 3

        class TradSesReqID(Tag):
            Tag = 335
            Type = "STRING"

        class TradingSessionID(Tag):
            Tag = 336
            Type = "STRING"
            class Values:
                DAY = "1"
                HALFDAY = "2"
                MORNING = "3"
                AFTERNOON = "4"
                EVENING = "5"
                AFTER_HOURS = "6"

        class ContraTrader(Tag):
            Tag = 337
            Type = "STRING"

        class TradSesMethod(Tag):
            Tag = 338
            Type = "INT"
            class Values:
                ELECTRONIC = 1
                OPEN_OUTCRY = 2
                TWO_PARTY = 3

        class TradSesMode(Tag):
            Tag = 339
            Type = "INT"
            class Values:
                TESTING = 1
                SIMULATED = 2
                PRODUCTION = 3

        class TradSesStatus(Tag):
            Tag = 340
            Type = "INT"
            class Values:
                UNKNOWN = 0
                HALTED = 1
                OPEN = 2
                CLOSED = 3
                PRE_OPEN = 4
                PRE_CLOSE = 5
                REQUEST_REJECTED = 6

        class TradSesStartTime(Tag):
            Tag = 341
            Type = "UTCTIMESTAMP"

        class TradSesOpenTime(Tag):
            Tag = 342
            Type = "UTCTIMESTAMP"

        class TradSesPreCloseTime(Tag):
            Tag = 343
            Type = "UTCTIMESTAMP"

        class TradSesCloseTime(Tag):
            Tag = 344
            Type = "UTCTIMESTAMP"

        class TradSesEndTime(Tag):
            Tag = 345
            Type = "UTCTIMESTAMP"

        class NumberOfOrders(Tag):
            Tag = 346
            Type = "INT"

        class MessageEncoding(Tag):
            Tag = 347
            Type = "STRING"

        class EncodedIssuerLen(Tag):
            Tag = 348
            Type = "LENGTH"

        class EncodedIssuer(Tag):
            Tag = 349
            Type = "DATA"

        class EncodedSecurityDescLen(Tag):
            Tag = 350
            Type = "LENGTH"

        class EncodedSecurityDesc(Tag):
            Tag = 351
            Type = "DATA"

        class EncodedListExecInstLen(Tag):
            Tag = 352
            Type = "LENGTH"

        class EncodedListExecInst(Tag):
            Tag = 353
            Type = "DATA"

        class EncodedTextLen(Tag):
            Tag = 354
            Type = "LENGTH"

        class EncodedText(Tag):
            Tag = 355
            Type = "DATA"

        class EncodedSubjectLen(Tag):
            Tag = 356
            Type = "LENGTH"

        class EncodedSubject(Tag):
            Tag = 357
            Type = "DATA"

        class EncodedHeadlineLen(Tag):
            Tag = 358
            Type = "LENGTH"

        class EncodedHeadline(Tag):
            Tag = 359
            Type = "DATA"

        class EncodedAllocTextLen(Tag):
            Tag = 360
            Type = "LENGTH"

        class EncodedAllocText(Tag):
            Tag = 361
            Type = "DATA"

        class EncodedUnderlyingIssuerLen(Tag):
            Tag = 362
            Type = "LENGTH"

        class EncodedUnderlyingIssuer(Tag):
            Tag = 363
            Type = "DATA"

        class EncodedUnderlyingSecurityDescLen(Tag):
            Tag = 364
            Type = "LENGTH"

        class EncodedUnderlyingSecurityDesc(Tag):
            Tag = 365
            Type = "DATA"

        class AllocPrice(Tag):
            Tag = 366
            Type = "PRICE"

        class QuoteSetValidUntilTime(Tag):
            Tag = 367
            Type = "UTCTIMESTAMP"

        class QuoteEntryRejectReason(Tag):
            Tag = 368
            Type = "INT"

        class LastMsgSeqNumProcessed(Tag):
            Tag = 369
            Type = "SEQNUM"

        class RefTagID(Tag):
            Tag = 371
            Type = "INT"

        class RefMsgType(Tag):
            Tag = 372
            Type = "STRING"

        class SessionRejectReason(Tag):
            Tag = 373
            Type = "INT"
            class Values:
                INVALID_TAG_NUMBER = 0
                REQUIRED_TAG_MISSING = 1
                TAG_NOT_DEFINED_FOR_THIS_MESSAGE_TYPE = 2
                UNDEFINED_TAG = 3
                TAG_SPECIFIED_WITHOUT_A_VALUE = 4
                VALUE_IS_INCORRECT = 5
                INCORRECT_DATA_FORMAT_FOR_VALUE = 6
                DECRYPTION_PROBLEM = 7
                SIGNATURE_PROBLEM = 8
                COMPID_PROBLEM = 9
                SENDINGTIME_ACCURACY_PROBLEM = 10
                INVALID_MSGTYPE = 11
                XML_VALIDATION_ERROR = 12
                TAG_APPEARS_MORE_THAN_ONCE = 13
                TAG_SPECIFIED_OUT_OF_REQUIRED_ORDER = 14
                REPEATING_GROUP_FIELDS_OUT_OF_ORDER = 15
                INCORRECT_NUMINGROUP_COUNT_FOR_REPEATING_GROUP = 16
                NON_DATA_VALUE_INCLUDES_FIELD_DELIMITER = 17
                INVALID_UNSUPPORTED_APPLICATION_VERSION = 18
                OTHER = 99

        class BidRequestTransType(Tag):
            Tag = 374
            Type = "CHAR"
            class Values:
                CANCEL = "C"
                NO = "N"

        class ContraBroker(Tag):
            Tag = 375
            Type = "STRING"

        class ComplianceID(Tag):
            Tag = 376
            Type = "STRING"

        class SolicitedFlag(Tag):
            Tag = 377
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class ExecRestatementReason(Tag):
            Tag = 378
            Type = "INT"
            class Values:
                GT_CORPORATE_ACTION = 0
                GT_RENEWAL = 1
                VERBAL_CHANGE = 2
                REPRICING_OF_ORDER = 3
                BROKER_OPTION = 4
                PARTIAL_DECLINE_OF_ORDERQTY = 5
                CANCEL_ON_TRADING_HALT = 6
                CANCEL_ON_SYSTEM_FAILURE = 7
                MARKET = 8
                CANCELED_NOT_BEST = 9
                WAREHOUSE_RECAP = 10
                PEG_REFRESH = 11
                OTHER = 99

        class BusinessRejectRefID(Tag):
            Tag = 379
            Type = "STRING"

        class BusinessRejectReason(Tag):
            Tag = 380
            Type = "INT"
            class Values:
                OTHER = 0
                UNKNOWN_ID = 1
                UNKNOWN_SECURITY = 2
                UNSUPPORTED_MESSAGE_TYPE = 3
                APPLICATION_NOT_AVAILABLE = 4
                CONDITIONALLY_REQUIRED_FIELD_MISSING = 5
                NOT_AUTHORIZED = 6
                DELIVERTO_FIRM_NOT_AVAILABLE_AT_THIS_TIME = 7
                INVALID_PRICE_INCREMENT = 18

        class GrossTradeAmt(Tag):
            Tag = 381
            Type = "AMT"

        class NoContraBrokers(Tag):
            Tag = 382
            Type = "NUMINGROUP"

        class MaxMessageSize(Tag):
            Tag = 383
            Type = "LENGTH"

        class NoMsgTypes(Tag):
            Tag = 384
            Type = "NUMINGROUP"

        class MsgDirection(Tag):
            Tag = 385
            Type = "CHAR"
            class Values:
                RECEIVE = "R"
                SEND = "S"

        class NoTradingSessions(Tag):
            Tag = 386
            Type = "NUMINGROUP"

        class TotalVolumeTraded(Tag):
            Tag = 387
            Type = "QTY"

        class DiscretionInst(Tag):
            Tag = 388
            Type = "CHAR"
            class Values:
                RELATED_TO_DISPLAYED_PRICE = "0"
                RELATED_TO_MARKET_PRICE = "1"
                RELATED_TO_PRIMARY_PRICE = "2"
                RELATED_TO_LOCAL_PRIMARY_PRICE = "3"
                RELATED_TO_MIDPOINT_PRICE = "4"
                RELATED_TO_LAST_TRADE_PRICE = "5"
                RELATED_TO_VWAP = "6"
                AVERAGE_PRICE_GUARANTEE = "7"

        class DiscretionOffsetValue(Tag):
            Tag = 389
            Type = "FLOAT"

        class BidID(Tag):
            Tag = 390
            Type = "STRING"

        class ClientBidID(Tag):
            Tag = 391
            Type = "STRING"

        class ListName(Tag):
            Tag = 392
            Type = "STRING"

        class TotNoRelatedSym(Tag):
            Tag = 393
            Type = "INT"

        class BidType(Tag):
            Tag = 394
            Type = "INT"
            class Values:
                NON_DISCLOSED_STYLE = 1
                DISCLOSED_SYTLE = 2
                NO_BIDDING_PROCESS = 3

        class NumTickets(Tag):
            Tag = 395
            Type = "INT"

        class SideValue1(Tag):
            Tag = 396
            Type = "AMT"

        class SideValue2(Tag):
            Tag = 397
            Type = "AMT"

        class NoBidDescriptors(Tag):
            Tag = 398
            Type = "NUMINGROUP"

        class BidDescriptorType(Tag):
            Tag = 399
            Type = "INT"
            class Values:
                SECTOR = 1
                COUNTRY = 2
                INDEX = 3

        class BidDescriptor(Tag):
            Tag = 400
            Type = "STRING"

        class SideValueInd(Tag):
            Tag = 401
            Type = "INT"
            class Values:
                SIDE_VALUE_1 = 1
                SIDE_VALUE_2 = 2

        class LiquidityPctLow(Tag):
            Tag = 402
            Type = "PERCENTAGE"

        class LiquidityPctHigh(Tag):
            Tag = 403
            Type = "PERCENTAGE"

        class LiquidityValue(Tag):
            Tag = 404
            Type = "AMT"

        class EFPTrackingError(Tag):
            Tag = 405
            Type = "PERCENTAGE"

        class FairValue(Tag):
            Tag = 406
            Type = "AMT"

        class OutsideIndexPct(Tag):
            Tag = 407
            Type = "PERCENTAGE"

        class ValueOfFutures(Tag):
            Tag = 408
            Type = "AMT"

        class LiquidityIndType(Tag):
            Tag = 409
            Type = "INT"
            class Values:
                N5_DAY_MOVING_AVERAGE = 1
                N20_DAY_MOVING_AVERAGE = 2
                NORMAL_MARKET_SIZE = 3
                OTHER = 4

        class WtAverageLiquidity(Tag):
            Tag = 410
            Type = "PERCENTAGE"

        class ExchangeForPhysical(Tag):
            Tag = 411
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class OutMainCntryUIndex(Tag):
            Tag = 412
            Type = "AMT"

        class CrossPercent(Tag):
            Tag = 413
            Type = "PERCENTAGE"

        class ProgRptReqs(Tag):
            Tag = 414
            Type = "INT"
            class Values:
                BUY_SIDE_EXPLICITLY_REQUESTS_STATUS_USING_STATUE_REQUEST = 1
                SELL_SIDE_PERIODICALLY_SENDS_STATUS_USING_LIST_STATUS_PERIOD_OPTIONALLY_SPECIFIED_IN_PROGRESSPERIOD = 2
                REAL_TIME_EXECUTION_REPORTS = 3

        class ProgPeriodInterval(Tag):
            Tag = 415
            Type = "INT"

        class IncTaxInd(Tag):
            Tag = 416
            Type = "INT"
            class Values:
                NET = 1
                GROSS = 2

        class NumBidders(Tag):
            Tag = 417
            Type = "INT"

        class BidTradeType(Tag):
            Tag = 418
            Type = "CHAR"
            class Values:
                AGENCY = "A"
                VWAP_GUARANTEE = "G"
                GUARANTEED_CLOSE = "J"
                RISK_TRADE = "R"

        class BasisPxType(Tag):
            Tag = 419
            Type = "CHAR"
            class Values:
                CLOSING_PRICE_AT_MORNING_SESSION = "2"
                CLOSING_PRICE = "3"
                CURRENT_PRICE = "4"
                SQ = "5"
                VWAP_THROUGH_A_DAY = "6"
                VWAP_THROUGH_A_MORNING_SESSION = "7"
                VWAP_THROUGH_AN_AFTERNOON_SESSION = "8"
                VWAP_THROUGH_A_DAY_EXCEPT_YORI = "9"
                VWAP_THROUGH_A_MORNING_SESSION_EXCEPT_YORI = "A"
                VWAP_THROUGH_AN_AFTERNOON_SESSION_EXCEPT_YORI = "B"
                STRIKE = "C"
                OPEN = "D"
                OTHERS = "Z"

        class NoBidComponents(Tag):
            Tag = 420
            Type = "NUMINGROUP"

        class Country(Tag):
            Tag = 421
            Type = "COUNTRY"

        class TotNoStrikes(Tag):
            Tag = 422
            Type = "INT"

        class PriceType(Tag):
            Tag = 423
            Type = "INT"
            class Values:
                PERCENTAGE = 1
                PER_UNIT = 2
                FIXED_AMOUNT = 3
                DISCOUNT = 4
                PREMIUM = 5
                SPREAD = 6
                TED_PRICE = 7
                TED_YIELD = 8
                YIELD = 9
                FIXED_CABINET_TRADE_PRICE = 10
                VARIABLE_CABINET_TRADE_PRICE = 11
                PRODUCT_TICKS_IN_HALFS = 13
                PRODUCT_TICKS_IN_FOURTHS = 14
                PRODUCT_TICKS_IN_EIGHTS = 15
                PRODUCT_TICKS_IN_SIXTEENTHS = 16
                PRODUCT_TICKS_IN_THIRTY_SECONDS = 17
                PRODUCT_TICKS_IN_SIXTY_FORTHS = 18
                PRODUCT_TICKS_IN_ONE_TWENTY_EIGHTS = 19

        class DayOrderQty(Tag):
            Tag = 424
            Type = "QTY"

        class DayCumQty(Tag):
            Tag = 425
            Type = "QTY"

        class DayAvgPx(Tag):
            Tag = 426
            Type = "PRICE"

        class GTBookingInst(Tag):
            Tag = 427
            Type = "INT"
            class Values:
                BOOK_OUT_ALL_TRADES_ON_DAY_OF_EXECUTION = 0
                ACCUMULATE_EXECUTIONS_UNTIL_ORDER_IS_FILLED_OR_EXPIRES = 1
                ACCUMULATE_UNTIL_VERBALLY_NOTIFIED_OTHERWISE = 2

        class NoStrikes(Tag):
            Tag = 428
            Type = "NUMINGROUP"

        class ListStatusType(Tag):
            Tag = 429
            Type = "INT"
            class Values:
                ACK = 1
                RESPONSE = 2
                TIMED = 3
                EXEC_STARTED = 4
                ALL_DONE = 5
                ALERT = 6

        class NetGrossInd(Tag):
            Tag = 430
            Type = "INT"
            class Values:
                NET = 1
                GROSS = 2

        class ListOrderStatus(Tag):
            Tag = 431
            Type = "INT"
            class Values:
                IN_BIDDING_PROCESS = 1
                RECEIVED_FOR_EXECUTION = 2
                EXECUTING = 3
                CANCELLING = 4
                ALERT = 5
                ALL_DONE = 6
                REJECT = 7

        class ExpireDate(Tag):
            Tag = 432
            Type = "LOCALMKTDATE"

        class ListExecInstType(Tag):
            Tag = 433
            Type = "CHAR"
            class Values:
                IMMEDIATE = "1"
                WAIT_FOR_EXECUT_INSTRUCTION = "2"
                EXCHANGE_SWITCH_CIV_ORDER_3 = "3"
                EXCHANGE_SWITCH_CIV_ORDER_4 = "4"
                EXCHANGE_SWITCH_CIV_ORDER_5 = "5"

        class CxlRejResponseTo(Tag):
            Tag = 434
            Type = "CHAR"
            class Values:
                ORDER_CANCEL_REQUEST = "1"
                ORDER_CANCEL_REPLACE_REQUEST = "2"

        class UnderlyingCouponRate(Tag):
            Tag = 435
            Type = "PERCENTAGE"

        class UnderlyingContractMultiplier(Tag):
            Tag = 436
            Type = "FLOAT"

        class ContraTradeQty(Tag):
            Tag = 437
            Type = "QTY"

        class ContraTradeTime(Tag):
            Tag = 438
            Type = "UTCTIMESTAMP"

        class LiquidityNumSecurities(Tag):
            Tag = 441
            Type = "INT"

        class MultiLegReportingType(Tag):
            Tag = 442
            Type = "CHAR"
            class Values:
                SINGLE_SECURITY = "1"
                INDIVIDUAL_LEG_OF_A_MULTI_LEG_SECURITY = "2"
                MULTI_LEG_SECURITY = "3"

        class StrikeTime(Tag):
            Tag = 443
            Type = "UTCTIMESTAMP"

        class ListStatusText(Tag):
            Tag = 444
            Type = "STRING"

        class EncodedListStatusTextLen(Tag):
            Tag = 445
            Type = "LENGTH"

        class EncodedListStatusText(Tag):
            Tag = 446
            Type = "DATA"

        class PartyIDSource(Tag):
            Tag = 447
            Type = "CHAR"
            class Values:
                UK_NATIONAL_INSURANCE_OR_PENSION_NUMBER = "6"
                US_SOCIAL_SECURITY_NUMBER = "7"
                US_EMPLOYER_OR_TAX_ID_NUMBER = "8"
                AUSTRALIAN_BUSINESS_NUMBER = "9"
                AUSTRALIAN_TAX_FILE_NUMBER = "A"
                KOREAN_INVESTOR_ID = "1"
                TAIWANESE_QUALIFIED_FOREIGN_INVESTOR_ID_QFII_FID = "2"
                TAIWANESE_TRADING_ACCT = "3"
                MALAYSIAN_CENTRAL_DEPOSITORY = "4"
                CHINESE_INVESTOR_ID = "5"
                DIRECTED_BROKER_THREE_CHARACTER_ACRONYM_AS_DEFINED_IN_ISITC_ETC_BEST_PRACTICE_GUIDELINES_DOCUMENT = "I"
                BIC = "B"
                GENERALLY_ACCEPTED_MARKET_PARTICIPANT_IDENTIFIER = "C"
                PROPRIETARY = "D"
                ISO_COUNTRY_CODE = "E"
                SETTLEMENT_ENTITY_LOCATION = "F"
                MIC = "G"
                CSD_PARTICIPANT_MEMBER_CODE = "H"

        class PartyID(Tag):
            Tag = 448
            Type = "STRING"

        class NetChgPrevDay(Tag):
            Tag = 451
            Type = "PRICEOFFSET"

        class PartyRole(Tag):
            Tag = 452
            Type = "INT"
            class Values:
                EXECUTING_FIRM = 1
                BROKER_OF_CREDIT = 2
                CLIENT_ID = 3
                CLEARING_FIRM = 4
                INVESTOR_ID = 5
                INTRODUCING_FIRM = 6
                ENTERING_FIRM = 7
                LOCATE = 8
                FUND_MANAGER_CLIENT_ID = 9
                SETTLEMENT_LOCATION = 10
                ORDER_ORIGINATION_TRADER = 11
                EXECUTING_TRADER = 12
                ORDER_ORIGINATION_FIRM = 13
                GIVEUP_CLEARING_FIRM = 14
                CORRESPONDANT_CLEARING_FIRM = 15
                EXECUTING_SYSTEM = 16
                CONTRA_FIRM = 17
                CONTRA_CLEARING_FIRM = 18
                SPONSORING_FIRM = 19
                UNDERLYING_CONTRA_FIRM = 20
                CLEARING_ORGANIZATION = 21
                EXCHANGE = 22
                CUSTOMER_ACCOUNT = 24
                CORRESPONDENT_CLEARING_ORGANIZATION = 25
                CORRESPONDENT_BROKER = 26
                BUYER_SELLER = 27
                CUSTODIAN = 28
                INTERMEDIARY = 29
                AGENT = 30
                SUB_CUSTODIAN = 31
                BENEFICIARY = 32
                INTERESTED_PARTY = 33
                REGULATORY_BODY = 34
                LIQUIDITY_PROVIDER = 35
                ENTERING_TRADER = 36
                CONTRA_TRADER = 37
                POSITION_ACCOUNT = 38
                CONTRA_INVESTOR_ID = 39
                TRANSFER_TO_FIRM = 40
                CONTRA_POSITION_ACCOUNT = 41
                CONTRA_EXCHANGE = 42
                INTERNAL_CARRY_ACCOUNT = 43
                ORDER_ENTRY_OPERATOR_ID = 44
                SECONDARY_ACCOUNT_NUMBER = 45
                FOREIGN_FIRM = 46
                THIRD_PARTY_ALLOCATION_FIRM = 47
                CLAIMING_ACCOUNT = 48
                ASSET_MANAGER = 49
                PLEDGOR_ACCOUNT = 50
                PLEDGEE_ACCOUNT = 51
                LARGE_TRADER_REPORTABLE_ACCOUNT = 52
                TRADER_MNEMONIC = 53
                SENDER_LOCATION = 54
                SESSION_ID = 55
                ACCEPTABLE_COUNTERPARTY = 56
                UNACCEPTABLE_COUNTERPARTY = 57
                ENTERING_UNIT = 58
                EXECUTING_UNIT = 59
                INTRODUCING_BROKER = 60
                QUOTE_ORIGINATOR = 61
                REPORT_ORIGINATOR = 62
                SYSTEMATIC_INTERNALISER = 63
                MULTILATERAL_TRADING_FACILITY = 64
                REGULATED_MARKET = 65
                MARKET_MAKER = 66
                INVESTMENT_FIRM = 67
                HOST_COMPETENT_AUTHORITY = 68
                HOME_COMPETENT_AUTHORITY = 69
                COMPETENT_AUTHORITY_OF_THE_MOST_RELEVANT_MARKET_IN_TERMS_OF_LIQUIDITY = 70
                COMPETENT_AUTHORITY_OF_THE_TRANSACTION = 71
                REPORTING_INTERMEDIARY = 72
                EXECUTION_VENUE = 73
                MARKET_DATA_ENTRY_ORIGINATOR = 74
                LOCATION_ID = 75
                DESK_ID = 76
                MARKET_DATA_MARKET = 77
                ALLOCATION_ENTITY = 78
                PRIME_BROKER_PROVIDING_GENERAL_TRADE_SERVICES = 79
                STEP_OUT_FIRM = 80
                BROKERCLEARINGID = 81
                CENTRAL_REGISTRATION_DEPOSITORY = 82
                CLEARING_ACCOUNT = 83
                ACCEPTABLE_SETTLING_COUNTERPARTY = 84
                UNACCEPTABLE_SETTLING_COUNTERPARTY = 85

        class NoPartyIDs(Tag):
            Tag = 453
            Type = "NUMINGROUP"

        class NoSecurityAltID(Tag):
            Tag = 454
            Type = "NUMINGROUP"

        class SecurityAltID(Tag):
            Tag = 455
            Type = "STRING"

        class SecurityAltIDSource(Tag):
            Tag = 456
            Type = "STRING"

        class NoUnderlyingSecurityAltID(Tag):
            Tag = 457
            Type = "NUMINGROUP"

        class UnderlyingSecurityAltID(Tag):
            Tag = 458
            Type = "STRING"

        class UnderlyingSecurityAltIDSource(Tag):
            Tag = 459
            Type = "STRING"

        class Product(Tag):
            Tag = 460
            Type = "INT"
            class Values:
                AGENCY = 1
                COMMODITY = 2
                CORPORATE = 3
                CURRENCY = 4
                EQUITY = 5
                GOVERNMENT = 6
                INDEX = 7
                LOAN = 8
                MONEYMARKET = 9
                MORTGAGE = 10
                MUNICIPAL = 11
                OTHER = 12
                FINANCING = 13

        class CFICode(Tag):
            Tag = 461
            Type = "STRING"

        class UnderlyingProduct(Tag):
            Tag = 462
            Type = "INT"

        class UnderlyingCFICode(Tag):
            Tag = 463
            Type = "STRING"

        class TestMessageIndicator(Tag):
            Tag = 464
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class BookingRefID(Tag):
            Tag = 466
            Type = "STRING"

        class IndividualAllocID(Tag):
            Tag = 467
            Type = "STRING"

        class RoundingDirection(Tag):
            Tag = 468
            Type = "CHAR"
            class Values:
                ROUND_TO_NEAREST = "0"
                ROUND_DOWN = "1"
                ROUND_UP = "2"

        class RoundingModulus(Tag):
            Tag = 469
            Type = "FLOAT"

        class CountryOfIssue(Tag):
            Tag = 470
            Type = "COUNTRY"

        class StateOrProvinceOfIssue(Tag):
            Tag = 471
            Type = "STRING"

        class LocaleOfIssue(Tag):
            Tag = 472
            Type = "STRING"

        class NoRegistDtls(Tag):
            Tag = 473
            Type = "NUMINGROUP"

        class MailingDtls(Tag):
            Tag = 474
            Type = "STRING"

        class InvestorCountryOfResidence(Tag):
            Tag = 475
            Type = "COUNTRY"

        class PaymentRef(Tag):
            Tag = 476
            Type = "STRING"

        class DistribPaymentMethod(Tag):
            Tag = 477
            Type = "INT"
            class Values:
                CREST = 1
                NSCC = 2
                EUROCLEAR = 3
                CLEARSTREAM = 4
                CHEQUE = 5
                TELEGRAPHIC_TRANSFER = 6
                FED_WIRE = 7
                DIRECT_CREDIT = 8
                ACH_CREDIT = 9
                BPAY = 10
                HIGH_VALUE_CLEARING_SYSTEM_HVACS = 11
                REINVEST_IN_FUND = 12

        class CashDistribCurr(Tag):
            Tag = 478
            Type = "CURRENCY"

        class CommCurrency(Tag):
            Tag = 479
            Type = "CURRENCY"

        class CancellationRights(Tag):
            Tag = 480
            Type = "CHAR"
            class Values:
                YES = "Y"
                NO_N = "N"
                NO_M = "M"
                NO_O = "O"

        class MoneyLaunderingStatus(Tag):
            Tag = 481
            Type = "CHAR"
            class Values:
                PASSED = "Y"
                NOT_CHECKED = "N"
                EXEMPT_1 = "1"
                EXEMPT_2 = "2"
                EXEMPT_3 = "3"

        class MailingInst(Tag):
            Tag = 482
            Type = "STRING"

        class TransBkdTime(Tag):
            Tag = 483
            Type = "UTCTIMESTAMP"

        class ExecPriceType(Tag):
            Tag = 484
            Type = "CHAR"
            class Values:
                BID_PRICE = "B"
                CREATION_PRICE = "C"
                CREATION_PRICE_PLUS_ADJUSTMENT_PERCENT = "D"
                CREATION_PRICE_PLUS_ADJUSTMENT_AMOUNT = "E"
                OFFER_PRICE = "O"
                OFFER_PRICE_MINUS_ADJUSTMENT_PERCENT = "P"
                OFFER_PRICE_MINUS_ADJUSTMENT_AMOUNT = "Q"
                SINGLE_PRICE = "S"

        class ExecPriceAdjustment(Tag):
            Tag = 485
            Type = "FLOAT"

        class DateOfBirth(Tag):
            Tag = 486
            Type = "LOCALMKTDATE"

        class TradeReportTransType(Tag):
            Tag = 487
            Type = "INT"
            class Values:
                NEW = 0
                CANCEL = 1
                REPLACE = 2
                RELEASE = 3
                REVERSE = 4
                CANCEL_DUE_TO_BACK_OUT_OF_TRADE = 5

        class CardHolderName(Tag):
            Tag = 488
            Type = "STRING"

        class CardNumber(Tag):
            Tag = 489
            Type = "STRING"

        class CardExpDate(Tag):
            Tag = 490
            Type = "LOCALMKTDATE"

        class CardIssNum(Tag):
            Tag = 491
            Type = "STRING"

        class PaymentMethod(Tag):
            Tag = 492
            Type = "INT"
            class Values:
                CREST = 1
                NSCC = 2
                EUROCLEAR = 3
                CLEARSTREAM = 4
                CHEQUE = 5
                TELEGRAPHIC_TRANSFER = 6
                FED_WIRE = 7
                DEBIT_CARD = 8
                DIRECT_DEBIT = 9
                DIRECT_CREDIT = 10
                CREDIT_CARD = 11
                ACH_DEBIT = 12
                ACH_CREDIT = 13
                BPAY = 14
                HIGH_VALUE_CLEARING_SYSTEM = 15

        class RegistAcctType(Tag):
            Tag = 493
            Type = "STRING"

        class Designation(Tag):
            Tag = 494
            Type = "STRING"

        class TaxAdvantageType(Tag):
            Tag = 495
            Type = "INT"
            class Values:
                NONE_NOT_APPLICABLE = 0
                MAXI_ISA = 1
                TESSA = 2
                MINI_CASH_ISA = 3
                MINI_STOCKS_AND_SHARES_ISA = 4
                MINI_INSURANCE_ISA = 5
                CURRENT_YEAR_PAYMENT = 6
                PRIOR_YEAR_PAYMENT = 7
                ASSET_TRANSFER = 8
                EMPLOYEE_9 = 9
                EMPLOYEE_10 = 10
                EMPLOYER_11 = 11
                EMPLOYER_12 = 12
                NON_FUND_PROTOTYPE_IRA = 13
                NON_FUND_QUALIFIED_PLAN = 14
                DEFINED_CONTRIBUTION_PLAN = 15
                INDIVIDUAL_RETIREMENT_ACCOUNT_16 = 16
                INDIVIDUAL_RETIREMENT_ACCOUNT_17 = 17
                KEOGH = 18
                PROFIT_SHARING_PLAN = 19
                N401 = 20
                SELF_DIRECTED_IRA = 21
                N403 = 22
                N457 = 23
                ROTH_IRA_24 = 24
                ROTH_IRA_25 = 25
                ROTH_CONVERSION_IRA_26 = 26
                ROTH_CONVERSION_IRA_27 = 27
                EDUCATION_IRA_28 = 28
                EDUCATION_IRA_29 = 29
                OTHER = 999

        class RegistRejReasonText(Tag):
            Tag = 496
            Type = "STRING"

        class FundRenewWaiv(Tag):
            Tag = 497
            Type = "CHAR"
            class Values:
                NO = "N"
                YES = "Y"

        class CashDistribAgentName(Tag):
            Tag = 498
            Type = "STRING"

        class CashDistribAgentCode(Tag):
            Tag = 499
            Type = "STRING"

        class CashDistribAgentAcctNumber(Tag):
            Tag = 500
            Type = "STRING"

        class CashDistribPayRef(Tag):
            Tag = 501
            Type = "STRING"

        class CashDistribAgentAcctName(Tag):
            Tag = 502
            Type = "STRING"

        class CardStartDate(Tag):
            Tag = 503
            Type = "LOCALMKTDATE"

        class PaymentDate(Tag):
            Tag = 504
            Type = "LOCALMKTDATE"

        class PaymentRemitterID(Tag):
            Tag = 505
            Type = "STRING"

        class RegistStatus(Tag):
            Tag = 506
            Type = "CHAR"
            class Values:
                ACCEPTED = "A"
                REJECTED = "R"
                HELD = "H"
                REMINDER = "N"

        class RegistRejReasonCode(Tag):
            Tag = 507
            Type = "INT"
            class Values:
                INVALID_UNACCEPTABLE_ACCOUNT_TYPE = 1
                INVALID_UNACCEPTABLE_TAX_EXEMPT_TYPE = 2
                INVALID_UNACCEPTABLE_OWNERSHIP_TYPE = 3
                INVALID_UNACCEPTABLE_NO_REG_DETAILS = 4
                INVALID_UNACCEPTABLE_REG_SEQ_NO = 5
                INVALID_UNACCEPTABLE_REG_DETAILS = 6
                INVALID_UNACCEPTABLE_MAILING_DETAILS = 7
                INVALID_UNACCEPTABLE_MAILING_INSTRUCTIONS = 8
                INVALID_UNACCEPTABLE_INVESTOR_ID = 9
                INVALID_UNACEEPTABLE_INVESTOR_ID_SOURCE = 10
                INVALID_UNACCEPTABLE_DATE_OF_BIRTH = 11
                INVALID_UNACCEPTABLE_INVESTOR_COUNTRY_OF_RESIDENCE = 12
                INVALID_UNACCEPTABLE_NO_DISTRIB_INSTNS = 13
                INVALID_UNACCEPTABLE_DISTRIB_PERCENTAGE = 14
                INVALID_UNACCEPTABLE_DISTRIB_PAYMENT_METHOD = 15
                INVALID_UNACCEPTABLE_CASH_DISTRIB_AGENT_ACCT_NAME = 16
                INVALID_UNACCEPTABLE_CASH_DISTRIB_AGENT_CODE = 17
                INVALID_UNACCEPTABLE_CASH_DISTRIB_AGENT_ACCT_NUM = 18
                OTHER = 99

        class RegistRefID(Tag):
            Tag = 508
            Type = "STRING"

        class RegistDtls(Tag):
            Tag = 509
            Type = "STRING"

        class NoDistribInsts(Tag):
            Tag = 510
            Type = "NUMINGROUP"

        class RegistEmail(Tag):
            Tag = 511
            Type = "STRING"

        class DistribPercentage(Tag):
            Tag = 512
            Type = "PERCENTAGE"

        class RegistID(Tag):
            Tag = 513
            Type = "STRING"

        class RegistTransType(Tag):
            Tag = 514
            Type = "CHAR"
            class Values:
                NEW = "0"
                CANCEL = "2"
                REPLACE = "1"

        class ExecValuationPoint(Tag):
            Tag = 515
            Type = "UTCTIMESTAMP"

        class OrderPercent(Tag):
            Tag = 516
            Type = "PERCENTAGE"

        class OwnershipType(Tag):
            Tag = 517
            Type = "CHAR"
            class Values:
                JOINT_INVESTORS = "J"
                TENANTS_IN_COMMON = "T"
                JOINT_TRUSTEES = "2"

        class NoContAmts(Tag):
            Tag = 518
            Type = "NUMINGROUP"

        class ContAmtType(Tag):
            Tag = 519
            Type = "INT"
            class Values:
                COMMISSION_AMOUNT = 1
                COMMISSION_PERCENT = 2
                INITIAL_CHARGE_AMOUNT = 3
                INITIAL_CHARGE_PERCENT = 4
                DISCOUNT_AMOUNT = 5
                DISCOUNT_PERCENT = 6
                DILUTION_LEVY_AMOUNT = 7
                DILUTION_LEVY_PERCENT = 8
                EXIT_CHARGE_AMOUNT = 9
                EXIT_CHARGE_PERCENT = 10
                FUND_BASED_RENEWAL_COMMISSION_PERCENT = 11
                PROJECTED_FUND_VALUE = 12
                FUND_BASED_RENEWAL_COMMISSION_AMOUNT_13 = 13
                FUND_BASED_RENEWAL_COMMISSION_AMOUNT_14 = 14
                NET_SETTLEMENT_AMOUNT = 15

        class ContAmtValue(Tag):
            Tag = 520
            Type = "FLOAT"

        class ContAmtCurr(Tag):
            Tag = 521
            Type = "CURRENCY"

        class OwnerType(Tag):
            Tag = 522
            Type = "INT"
            class Values:
                INDIVIDUAL_INVESTOR = 1
                PUBLIC_COMPANY = 2
                PRIVATE_COMPANY = 3
                INDIVIDUAL_TRUSTEE = 4
                COMPANY_TRUSTEE = 5
                PENSION_PLAN = 6
                CUSTODIAN_UNDER_GIFTS_TO_MINORS_ACT = 7
                TRUSTS = 8
                FIDUCIARIES = 9
                NETWORKING_SUB_ACCOUNT = 10
                NON_PROFIT_ORGANIZATION = 11
                CORPORATE_BODY = 12
                NOMINEE = 13

        class PartySubID(Tag):
            Tag = 523
            Type = "STRING"

        class NestedPartyID(Tag):
            Tag = 524
            Type = "STRING"

        class NestedPartyIDSource(Tag):
            Tag = 525
            Type = "CHAR"

        class SecondaryClOrdID(Tag):
            Tag = 526
            Type = "STRING"

        class SecondaryExecID(Tag):
            Tag = 527
            Type = "STRING"

        class OrderCapacity(Tag):
            Tag = 528
            Type = "CHAR"
            class Values:
                AGENCY = "A"
                PROPRIETARY = "G"
                INDIVIDUAL = "I"
                PRINCIPAL = "P"
                RISKLESS_PRINCIPAL = "R"
                AGENT_FOR_OTHER_MEMBER = "W"

        class OrderRestrictions(Tag):
            Tag = 529
            Type = "MULTIPLECHARVALUE"
            class Values:
                PROGRAM_TRADE = "1"
                INDEX_ARBITRAGE = "2"
                NON_INDEX_ARBITRAGE = "3"
                COMPETING_MARKET_MAKER = "4"
                ACTING_AS_MARKET_MAKER_OR_SPECIALIST_IN_THE_SECURITY = "5"
                ACTING_AS_MARKET_MAKER_OR_SPECIALIST_IN_THE_UNDERLYING_SECURITY_OF_A_DERIVATIVE_SECURITY = "6"
                FOREIGN_ENTITY = "7"
                EXTERNAL_MARKET_PARTICIPANT = "8"
                EXTERNAL_INTER_CONNECTED_MARKET_LINKAGE = "9"
                RISKLESS_ARBITRAGE = "A"
                ISSUER_HOLDING = "B"
                ISSUE_PRICE_STABILIZATION = "C"
                NON_ALGORITHMIC = "D"
                ALGORITHMIC = "E"
                CROSS = "F"

        class MassCancelRequestType(Tag):
            Tag = 530
            Type = "CHAR"
            class Values:
                CANCEL_ORDERS_FOR_A_SECURITY = "1"
                CANCEL_ORDERS_FOR_AN_UNDERLYING_SECURITY = "2"
                CANCEL_ORDERS_FOR_A_PRODUCT = "3"
                CANCEL_ORDERS_FOR_A_CFICODE = "4"
                CANCEL_ORDERS_FOR_A_SECURITYTYPE = "5"
                CANCEL_ORDERS_FOR_A_TRADING_SESSION = "6"
                CANCEL_ALL_ORDERS = "7"
                CANCEL_ORDERS_FOR_A_MARKET = "8"
                CANCEL_ORDERS_FOR_A_MARKET_SEGMENT = "9"
                CANCEL_ORDERS_FOR_A_SECURITY_GROUP = "A"
                CANCEL_FOR_SECURITY_ISSUER = "B"
                CANCEL_FOR_ISSUER_OF_UNDERLYING_SECURITY = "C"

        class MassCancelResponse(Tag):
            Tag = 531
            Type = "CHAR"
            class Values:
                CANCEL_REQUEST_REJECTED = "0"
                CANCEL_ORDERS_FOR_A_SECURITY = "1"
                CANCEL_ORDERS_FOR_AN_UNDERLYING_SECURITY = "2"
                CANCEL_ORDERS_FOR_A_PRODUCT = "3"
                CANCEL_ORDERS_FOR_A_CFICODE = "4"
                CANCEL_ORDERS_FOR_A_SECURITYTYPE = "5"
                CANCEL_ORDERS_FOR_A_TRADING_SESSION = "6"
                CANCEL_ALL_ORDERS = "7"
                CANCEL_ORDERS_FOR_A_MARKET = "8"
                CANCEL_ORDERS_FOR_A_MARKET_SEGMENT = "9"
                CANCEL_ORDERS_FOR_A_SECURITY_GROUP = "A"
                CANCEL_ORDERS_FOR_A_SECURITIES_ISSUER = "B"
                CANCEL_ORDERS_FOR_ISSUER_OF_UNDERLYING_SECURITY = "C"

        class MassCancelRejectReason(Tag):
            Tag = 532
            Type = "INT"
            class Values:
                MASS_CANCEL_NOT_SUPPORTED = 0
                INVALID_OR_UNKNOWN_SECURITY = 1
                INVALID_OR_UNKOWN_UNDERLYING_SECURITY = 2
                INVALID_OR_UNKNOWN_PRODUCT = 3
                INVALID_OR_UNKNOWN_CFICODE = 4
                INVALID_OR_UNKNOWN_SECURITYTYPE = 5
                INVALID_OR_UNKNOWN_TRADING_SESSION = 6
                INVALID_OR_UNKNOWN_MARKET = 7
                INVALID_OR_UNKOWN_MARKET_SEGMENT = 8
                INVALID_OR_UNKNOWN_SECURITY_GROUP = 9
                OTHER = 99
                INVALID_OR_UNKNOWN_SECURITY_ISSUER = 10
                INVALID_OR_UNKNOWN_ISSUER_OF_UNDERLYING_SECURITY = 11

        class TotalAffectedOrders(Tag):
            Tag = 533
            Type = "INT"

        class NoAffectedOrders(Tag):
            Tag = 534
            Type = "NUMINGROUP"

        class AffectedOrderID(Tag):
            Tag = 535
            Type = "STRING"

        class AffectedSecondaryOrderID(Tag):
            Tag = 536
            Type = "STRING"

        class QuoteType(Tag):
            Tag = 537
            Type = "INT"
            class Values:
                INDICATIVE = 0
                TRADEABLE = 1
                RESTRICTED_TRADEABLE = 2
                COUNTER = 3

        class NestedPartyRole(Tag):
            Tag = 538
            Type = "INT"

        class NoNestedPartyIDs(Tag):
            Tag = 539
            Type = "NUMINGROUP"

        class TotalAccruedInterestAmt(Tag):
            Tag = 540
            Type = "AMT"

        class MaturityDate(Tag):
            Tag = 541
            Type = "LOCALMKTDATE"

        class UnderlyingMaturityDate(Tag):
            Tag = 542
            Type = "LOCALMKTDATE"

        class InstrRegistry(Tag):
            Tag = 543
            Type = "STRING"

        class CashMargin(Tag):
            Tag = 544
            Type = "CHAR"
            class Values:
                CASH = "1"
                MARGIN_OPEN = "2"
                MARGIN_CLOSE = "3"

        class NestedPartySubID(Tag):
            Tag = 545
            Type = "STRING"

        class Scope(Tag):
            Tag = 546
            Type = "MULTIPLECHARVALUE"
            class Values:
                LOCAL_MARKET = "1"
                NATIONAL = "2"
                GLOBAL = "3"

        class MDImplicitDelete(Tag):
            Tag = 547
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class CrossID(Tag):
            Tag = 548
            Type = "STRING"

        class CrossType(Tag):
            Tag = 549
            Type = "INT"
            class Values:
                CROSS_AON = 1
                CROSS_IOC = 2
                CROSS_ONE_SIDE = 3
                CROSS_SAME_PRICE = 4

        class CrossPrioritization(Tag):
            Tag = 550
            Type = "INT"
            class Values:
                NONE = 0
                BUY_SIDE_IS_PRIORITIZED = 1
                SELL_SIDE_IS_PRIORITIZED = 2

        class OrigCrossID(Tag):
            Tag = 551
            Type = "STRING"

        class NoSides(Tag):
            Tag = 552
            Type = "NUMINGROUP"
            class Values:
                ONE_SIDE = 1
                BOTH_SIDES = 2

        class Username(Tag):
            Tag = 553
            Type = "STRING"

        class Password(Tag):
            Tag = 554
            Type = "STRING"

        class NoLegs(Tag):
            Tag = 555
            Type = "NUMINGROUP"

        class LegCurrency(Tag):
            Tag = 556
            Type = "CURRENCY"

        class TotNoSecurityTypes(Tag):
            Tag = 557
            Type = "INT"

        class NoSecurityTypes(Tag):
            Tag = 558
            Type = "NUMINGROUP"

        class SecurityListRequestType(Tag):
            Tag = 559
            Type = "INT"
            class Values:
                SYMBOL = 0
                SECURITYTYPE_AND_OR_CFICODE = 1
                PRODUCT = 2
                TRADINGSESSIONID = 3
                ALL_SECURITIES = 4
                MARKETID_OR_MARKETID_PLUS_MARKETSEGMENTID = 5

        class SecurityRequestResult(Tag):
            Tag = 560
            Type = "INT"
            class Values:
                VALID_REQUEST = 0
                INVALID_OR_UNSUPPORTED_REQUEST = 1
                NO_INSTRUMENTS_FOUND_THAT_MATCH_SELECTION_CRITERIA = 2
                NOT_AUTHORIZED_TO_RETRIEVE_INSTRUMENT_DATA = 3
                INSTRUMENT_DATA_TEMPORARILY_UNAVAILABLE = 4
                REQUEST_FOR_INSTRUMENT_DATA_NOT_SUPPORTED = 5

        class RoundLot(Tag):
            Tag = 561
            Type = "QTY"

        class MinTradeVol(Tag):
            Tag = 562
            Type = "QTY"

        class MultiLegRptTypeReq(Tag):
            Tag = 563
            Type = "INT"
            class Values:
                REPORT_BY_MULITLEG_SECURITY_ONLY = 0
                REPORT_BY_MULTILEG_SECURITY_AND_BY_INSTRUMENT_LEGS_BELONGING_TO_THE_MULTILEG_SECURITY = 1
                REPORT_BY_INSTRUMENT_LEGS_BELONGING_TO_THE_MULTILEG_SECURITY_ONLY = 2

        class LegPositionEffect(Tag):
            Tag = 564
            Type = "CHAR"

        class LegCoveredOrUncovered(Tag):
            Tag = 565
            Type = "INT"

        class LegPrice(Tag):
            Tag = 566
            Type = "PRICE"

        class TradSesStatusRejReason(Tag):
            Tag = 567
            Type = "INT"
            class Values:
                UNKNOWN_OR_INVALID_TRADINGSESSIONID = 1
                OTHER = 99

        class TradeRequestID(Tag):
            Tag = 568
            Type = "STRING"

        class TradeRequestType(Tag):
            Tag = 569
            Type = "INT"
            class Values:
                ALL_TRADES = 0
                MATCHED_TRADES_MATCHING_CRITERIA_PROVIDED_ON_REQUEST = 1
                UNMATCHED_TRADES_THAT_MATCH_CRITERIA = 2
                UNREPORTED_TRADES_THAT_MATCH_CRITERIA = 3
                ADVISORIES_THAT_MATCH_CRITERIA = 4

        class PreviouslyReported(Tag):
            Tag = 570
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class TradeReportID(Tag):
            Tag = 571
            Type = "STRING"

        class TradeReportRefID(Tag):
            Tag = 572
            Type = "STRING"

        class MatchStatus(Tag):
            Tag = 573
            Type = "CHAR"
            class Values:
                COMPARED_MATCHED_OR_AFFIRMED = "0"
                UNCOMPARED_UNMATCHED_OR_UNAFFIRMED = "1"
                ADVISORY_OR_ALERT = "2"

        class MatchType(Tag):
            Tag = 574
            Type = "STRING"
            class Values:
                ONE_PARTY_TRADE_REPORT = "1"
                TWO_PARTY_TRADE_REPORT = "2"
                CONFIRMED_TRADE_REPORT = "3"
                AUTO_MATCH = "4"
                CROSS_AUCTION = "5"
                COUNTER_ORDER_SELECTION = "6"
                CALL_AUCTION = "7"
                ISSUING_BUY_BACK_AUCTION = "8"
                ACT_ACCEPTED_TRADE = "M3"
                ACT_DEFAULT_TRADE = "M4"
                ACT_DEFAULT_AFTER_M2 = "M5"
                ACT_M6_MATCH = "M6"
                EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_FOUR_BADGES_AND_EXECUTION_TIME = "A1"
                EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_FOUR_BADGES = "A2"
                EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_TWO_BADGES_AND_EXECUTION_TIME = "A3"
                EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_TWO_BADGES = "A4"
                EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADETYPE_AND_SPECIAL_TRADE_INDICATOR_PLUS_EXECUTION_TIME = "A5"
                COMPARED_RECORDS_RESULTING_FROM_STAMPED_ADVISORIES_OR_SPECIALIST_ACCEPTS_PAIR_OFFS = "AQ"
                SUMMARIZED_MATCH_USING_A1_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIED = "S1"
                SUMMARIZED_MATCH_USING_A2_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED = "S2"
                SUMMARIZED_MATCH_USING_A3_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED = "S3"
                SUMMARIZED_MATCH_USING_A4_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED = "S4"
                SUMMARIZED_MATCH_USING_A5_EXACT_MATCH_CRITERIA_EXCEPT_QUANTITY_IS_SUMMARIZED = "S5"
                EXACT_MATCH_ON_TRADE_DATE_STOCK_SYMBOL_QUANTITY_PRICE_TRADE_TYPE_AND_SPECIAL_TRADE_INDICATOR_MINUS_BADGES_AND_TIMES_ACT_M1_MATCH = "M1"
                SUMMARIZED_MATCH_MINUS_BADGES_AND_TIMES_ACT_M2_MATCH = "M2"
                OCS_LOCKED_IN_NON_ACT = "MT"

        class OddLot(Tag):
            Tag = 575
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class NoClearingInstructions(Tag):
            Tag = 576
            Type = "NUMINGROUP"

        class ClearingInstruction(Tag):
            Tag = 577
            Type = "INT"
            class Values:
                PROCESS_NORMALLY = 0
                EXCLUDE_FROM_ALL_NETTING = 1
                BILATERAL_NETTING_ONLY = 2
                EX_CLEARING = 3
                SPECIAL_TRADE = 4
                MULTILATERAL_NETTING = 5
                CLEAR_AGAINST_CENTRAL_COUNTERPARTY = 6
                EXCLUDE_FROM_CENTRAL_COUNTERPARTY = 7
                MANUAL_MODE = 8
                AUTOMATIC_POSTING_MODE = 9
                AUTOMATIC_GIVE_UP_MODE = 10
                QUALIFIED_SERVICE_REPRESENTATIVE_QSR = 11
                CUSTOMER_TRADE = 12
                SELF_CLEARING = 13

        class TradeInputSource(Tag):
            Tag = 578
            Type = "STRING"

        class TradeInputDevice(Tag):
            Tag = 579
            Type = "STRING"

        class NoDates(Tag):
            Tag = 580
            Type = "NUMINGROUP"

        class AccountType(Tag):
            Tag = 581
            Type = "INT"
            class Values:
                ACCOUNT_IS_CARRIED_ON_CUSTOMER_SIDE_OF_THE_BOOKS = 1
                ACCOUNT_IS_CARRIED_ON_NON_CUSTOMER_SIDE_OF_BOOKS = 2
                HOUSE_TRADER = 3
                FLOOR_TRADER = 4
                ACCOUNT_IS_CARRIED_ON_NON_CUSTOMER_SIDE_OF_BOOKS_AND_IS_CROSS_MARGINED = 6
                ACCOUNT_IS_HOUSE_TRADER_AND_IS_CROSS_MARGINED = 7
                JOINT_BACK_OFFICE_ACCOUNT = 8

        class CustOrderCapacity(Tag):
            Tag = 582
            Type = "INT"
            class Values:
                MEMBER_TRADING_FOR_THEIR_OWN_ACCOUNT = 1
                CLEARING_FIRM_TRADING_FOR_ITS_PROPRIETARY_ACCOUNT = 2
                MEMBER_TRADING_FOR_ANOTHER_MEMBER = 3
                ALL_OTHER = 4

        class ClOrdLinkID(Tag):
            Tag = 583
            Type = "STRING"

        class MassStatusReqID(Tag):
            Tag = 584
            Type = "STRING"

        class MassStatusReqType(Tag):
            Tag = 585
            Type = "INT"
            class Values:
                STATUS_FOR_ORDERS_FOR_A_SECURITY = 1
                STATUS_FOR_ORDERS_FOR_AN_UNDERLYING_SECURITY = 2
                STATUS_FOR_ORDERS_FOR_A_PRODUCT = 3
                STATUS_FOR_ORDERS_FOR_A_CFICODE = 4
                STATUS_FOR_ORDERS_FOR_A_SECURITYTYPE = 5
                STATUS_FOR_ORDERS_FOR_A_TRADING_SESSION = 6
                STATUS_FOR_ALL_ORDERS = 7
                STATUS_FOR_ORDERS_FOR_A_PARTYID = 8
                STATUS_FOR_SECURITY_ISSUER = 9
                STATUS_FOR_ISSUER_OF_UNDERLYING_SECURITY = 10

        class OrigOrdModTime(Tag):
            Tag = 586
            Type = "UTCTIMESTAMP"

        class LegSettlType(Tag):
            Tag = 587
            Type = "CHAR"

        class LegSettlDate(Tag):
            Tag = 588
            Type = "LOCALMKTDATE"

        class DayBookingInst(Tag):
            Tag = 589
            Type = "CHAR"
            class Values:
                CAN_TRIGGER_BOOKING_WITHOUT_REFERENCE_TO_THE_ORDER_INITIATOR = "0"
                SPEAK_WITH_ORDER_INITIATOR_BEFORE_BOOKING = "1"
                ACCUMULATE = "2"

        class BookingUnit(Tag):
            Tag = 590
            Type = "CHAR"
            class Values:
                EACH_PARTIAL_EXECUTION_IS_A_BOOKABLE_UNIT = "0"
                AGGREGATE_PARTIAL_EXECUTIONS_ON_THIS_ORDER_AND_BOOK_ONE_TRADE_PER_ORDER = "1"
                AGGREGATE_EXECUTIONS_FOR_THIS_SYMBOL_SIDE_AND_SETTLEMENT_DATE = "2"

        class PreallocMethod(Tag):
            Tag = 591
            Type = "CHAR"
            class Values:
                PRO_RATA = "0"
                DO_NOT_PRO_RATA = "1"

        class UnderlyingCountryOfIssue(Tag):
            Tag = 592
            Type = "COUNTRY"

        class UnderlyingStateOrProvinceOfIssue(Tag):
            Tag = 593
            Type = "STRING"

        class UnderlyingLocaleOfIssue(Tag):
            Tag = 594
            Type = "STRING"

        class UnderlyingInstrRegistry(Tag):
            Tag = 595
            Type = "STRING"

        class LegCountryOfIssue(Tag):
            Tag = 596
            Type = "COUNTRY"

        class LegStateOrProvinceOfIssue(Tag):
            Tag = 597
            Type = "STRING"

        class LegLocaleOfIssue(Tag):
            Tag = 598
            Type = "STRING"

        class LegInstrRegistry(Tag):
            Tag = 599
            Type = "STRING"

        class LegSymbol(Tag):
            Tag = 600
            Type = "STRING"

        class LegSymbolSfx(Tag):
            Tag = 601
            Type = "STRING"

        class LegSecurityID(Tag):
            Tag = 602
            Type = "STRING"

        class LegSecurityIDSource(Tag):
            Tag = 603
            Type = "STRING"

        class NoLegSecurityAltID(Tag):
            Tag = 604
            Type = "NUMINGROUP"

        class LegSecurityAltID(Tag):
            Tag = 605
            Type = "STRING"

        class LegSecurityAltIDSource(Tag):
            Tag = 606
            Type = "STRING"

        class LegProduct(Tag):
            Tag = 607
            Type = "INT"

        class LegCFICode(Tag):
            Tag = 608
            Type = "STRING"

        class LegSecurityType(Tag):
            Tag = 609
            Type = "STRING"

        class LegMaturityMonthYear(Tag):
            Tag = 610
            Type = "MONTHYEAR"

        class LegMaturityDate(Tag):
            Tag = 611
            Type = "LOCALMKTDATE"

        class LegStrikePrice(Tag):
            Tag = 612
            Type = "PRICE"

        class LegOptAttribute(Tag):
            Tag = 613
            Type = "CHAR"

        class LegContractMultiplier(Tag):
            Tag = 614
            Type = "FLOAT"

        class LegCouponRate(Tag):
            Tag = 615
            Type = "PERCENTAGE"

        class LegSecurityExchange(Tag):
            Tag = 616
            Type = "EXCHANGE"

        class LegIssuer(Tag):
            Tag = 617
            Type = "STRING"

        class EncodedLegIssuerLen(Tag):
            Tag = 618
            Type = "LENGTH"

        class EncodedLegIssuer(Tag):
            Tag = 619
            Type = "DATA"

        class LegSecurityDesc(Tag):
            Tag = 620
            Type = "STRING"

        class EncodedLegSecurityDescLen(Tag):
            Tag = 621
            Type = "LENGTH"

        class EncodedLegSecurityDesc(Tag):
            Tag = 622
            Type = "DATA"

        class LegRatioQty(Tag):
            Tag = 623
            Type = "FLOAT"

        class LegSide(Tag):
            Tag = 624
            Type = "CHAR"

        class TradingSessionSubID(Tag):
            Tag = 625
            Type = "STRING"
            class Values:
                PRE_TRADING = "1"
                OPENING_OR_OPENING_AUCTION = "2"
                N3 = "3"
                CLOSING_OR_CLOSING_AUCTION = "4"
                POST_TRADING = "5"
                INTRADAY_AUCTION = "6"
                QUIESCENT = "7"

        class AllocType(Tag):
            Tag = 626
            Type = "INT"
            class Values:
                CALCULATED = 1
                PRELIMINARY = 2
                SELLSIDE_CALCULATED_USING_PRELIMINARY = 3
                SELLSIDE_CALCULATED_WITHOUT_PRELIMINARY = 4
                READY_TO_BOOK = 5
                BUYSIDE_READY_TO_BOOK = 6
                WAREHOUSE_INSTRUCTION = 7
                REQUEST_TO_INTERMEDIARY = 8
                ACCEPT = 9
                REJECT = 10
                ACCEPT_PENDING = 11
                INCOMPLETE_GROUP = 12
                COMPLETE_GROUP = 13
                REVERSAL_PENDING = 14

        class NoHops(Tag):
            Tag = 627
            Type = "NUMINGROUP"

        class HopCompID(Tag):
            Tag = 628
            Type = "STRING"

        class HopSendingTime(Tag):
            Tag = 629
            Type = "UTCTIMESTAMP"

        class HopRefID(Tag):
            Tag = 630
            Type = "SEQNUM"

        class MidPx(Tag):
            Tag = 631
            Type = "PRICE"

        class BidYield(Tag):
            Tag = 632
            Type = "PERCENTAGE"

        class MidYield(Tag):
            Tag = 633
            Type = "PERCENTAGE"

        class OfferYield(Tag):
            Tag = 634
            Type = "PERCENTAGE"

        class ClearingFeeIndicator(Tag):
            Tag = 635
            Type = "STRING"
            class Values:
                N1ST_YEAR_DELEGATE_TRADING_FOR_OWN_ACCOUNT = "1"
                N2ND_YEAR_DELEGATE_TRADING_FOR_OWN_ACCOUNT = "2"
                N3RD_YEAR_DELEGATE_TRADING_FOR_OWN_ACCOUNT = "3"
                N4TH_YEAR_DELEGATE_TRADING_FOR_OWN_ACCOUNT = "4"
                N5TH_YEAR_DELEGATE_TRADING_FOR_OWN_ACCOUNT = "5"
                N6TH_YEAR_DELEGATE_TRADING_FOR_OWN_ACCOUNT = "9"
                CBOE_MEMBER = "B"
                NON_MEMBER_AND_CUSTOMER = "C"
                EQUITY_MEMBER_AND_CLEARING_MEMBER = "E"
                FULL_AND_ASSOCIATE_MEMBER_TRADING_FOR_OWN_ACCOUNT_AND_AS_FLOOR_BROKERS = "F"
                N106H_AND_106J_FIRMS = "H"
                GIM_IDEM_AND_COM_MEMBERSHIP_INTEREST_HOLDERS = "I"
                LESSEE_106F_EMPLOYEES = "L"
                ALL_OTHER_OWNERSHIP_TYPES = "M"

        class WorkingIndicator(Tag):
            Tag = 636
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class LegLastPx(Tag):
            Tag = 637
            Type = "PRICE"

        class PriorityIndicator(Tag):
            Tag = 638
            Type = "INT"
            class Values:
                PRIORITY_UNCHANGED = 0
                LOST_PRIORITY_AS_RESULT_OF_ORDER_CHANGE = 1

        class PriceImprovement(Tag):
            Tag = 639
            Type = "PRICEOFFSET"

        class Price2(Tag):
            Tag = 640
            Type = "PRICE"

        class LastForwardPoints2(Tag):
            Tag = 641
            Type = "PRICEOFFSET"

        class BidForwardPoints2(Tag):
            Tag = 642
            Type = "PRICEOFFSET"

        class OfferForwardPoints2(Tag):
            Tag = 643
            Type = "PRICEOFFSET"

        class RFQReqID(Tag):
            Tag = 644
            Type = "STRING"

        class MktBidPx(Tag):
            Tag = 645
            Type = "PRICE"

        class MktOfferPx(Tag):
            Tag = 646
            Type = "PRICE"

        class MinBidSize(Tag):
            Tag = 647
            Type = "QTY"

        class MinOfferSize(Tag):
            Tag = 648
            Type = "QTY"

        class QuoteStatusReqID(Tag):
            Tag = 649
            Type = "STRING"

        class LegalConfirm(Tag):
            Tag = 650
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class UnderlyingLastPx(Tag):
            Tag = 651
            Type = "PRICE"

        class UnderlyingLastQty(Tag):
            Tag = 652
            Type = "QTY"

        class LegRefID(Tag):
            Tag = 654
            Type = "STRING"

        class ContraLegRefID(Tag):
            Tag = 655
            Type = "STRING"

        class SettlCurrBidFxRate(Tag):
            Tag = 656
            Type = "FLOAT"

        class SettlCurrOfferFxRate(Tag):
            Tag = 657
            Type = "FLOAT"

        class QuoteRequestRejectReason(Tag):
            Tag = 658
            Type = "INT"
            class Values:
                UNKNOWN_SYMBOL = 1
                EXCHANGE = 2
                QUOTE_REQUEST_EXCEEDS_LIMIT = 3
                TOO_LATE_TO_ENTER = 4
                INVALID_PRICE = 5
                NOT_AUTHORIZED_TO_REQUEST_QUOTE = 6
                NO_MATCH_FOR_INQUIRY = 7
                NO_MARKET_FOR_INSTRUMENT = 8
                NO_INVENTORY = 9
                PASS = 10
                INSUFFICIENT_CREDIT = 11
                OTHER = 99

        class SideComplianceID(Tag):
            Tag = 659
            Type = "STRING"

        class AcctIDSource(Tag):
            Tag = 660
            Type = "INT"
            class Values:
                BIC = 1
                SID_CODE = 2
                TFM = 3
                OMGEO = 4
                DTCC_CODE = 5
                OTHER = 99

        class AllocAcctIDSource(Tag):
            Tag = 661
            Type = "INT"

        class BenchmarkPrice(Tag):
            Tag = 662
            Type = "PRICE"

        class BenchmarkPriceType(Tag):
            Tag = 663
            Type = "INT"

        class ConfirmID(Tag):
            Tag = 664
            Type = "STRING"

        class ConfirmStatus(Tag):
            Tag = 665
            Type = "INT"
            class Values:
                RECEIVED = 1
                MISMATCHED_ACCOUNT = 2
                MISSING_SETTLEMENT_INSTRUCTIONS = 3
                CONFIRMED = 4
                REQUEST_REJECTED = 5

        class ConfirmTransType(Tag):
            Tag = 666
            Type = "INT"
            class Values:
                NEW = 0
                REPLACE = 1
                CANCEL = 2

        class ContractSettlMonth(Tag):
            Tag = 667
            Type = "MONTHYEAR"

        class DeliveryForm(Tag):
            Tag = 668
            Type = "INT"
            class Values:
                BOOK_ENTRY = 1
                BEARER = 2

        class LastParPx(Tag):
            Tag = 669
            Type = "PRICE"

        class NoLegAllocs(Tag):
            Tag = 670
            Type = "NUMINGROUP"

        class LegAllocAccount(Tag):
            Tag = 671
            Type = "STRING"

        class LegIndividualAllocID(Tag):
            Tag = 672
            Type = "STRING"

        class LegAllocQty(Tag):
            Tag = 673
            Type = "QTY"

        class LegAllocAcctIDSource(Tag):
            Tag = 674
            Type = "STRING"

        class LegSettlCurrency(Tag):
            Tag = 675
            Type = "CURRENCY"

        class LegBenchmarkCurveCurrency(Tag):
            Tag = 676
            Type = "CURRENCY"

        class LegBenchmarkCurveName(Tag):
            Tag = 677
            Type = "STRING"

        class LegBenchmarkCurvePoint(Tag):
            Tag = 678
            Type = "STRING"

        class LegBenchmarkPrice(Tag):
            Tag = 679
            Type = "PRICE"

        class LegBenchmarkPriceType(Tag):
            Tag = 680
            Type = "INT"

        class LegBidPx(Tag):
            Tag = 681
            Type = "PRICE"

        class LegIOIQty(Tag):
            Tag = 682
            Type = "STRING"

        class NoLegStipulations(Tag):
            Tag = 683
            Type = "NUMINGROUP"

        class LegOfferPx(Tag):
            Tag = 684
            Type = "PRICE"

        class LegOrderQty(Tag):
            Tag = 685
            Type = "QTY"

        class LegPriceType(Tag):
            Tag = 686
            Type = "INT"

        class LegQty(Tag):
            Tag = 687
            Type = "QTY"

        class LegStipulationType(Tag):
            Tag = 688
            Type = "STRING"

        class LegStipulationValue(Tag):
            Tag = 689
            Type = "STRING"

        class LegSwapType(Tag):
            Tag = 690
            Type = "INT"
            class Values:
                PAR_FOR_PAR = 1
                MODIFIED_DURATION = 2
                RISK = 4
                PROCEEDS = 5

        class Pool(Tag):
            Tag = 691
            Type = "STRING"

        class QuotePriceType(Tag):
            Tag = 692
            Type = "INT"
            class Values:
                PERCENT = 1
                PER_SHARE = 2
                FIXED_AMOUNT = 3
                DISCOUNT = 4
                PREMIUM = 5
                SPREAD = 6
                TED_PRICE = 7
                TED_YIELD = 8
                YIELD_SPREAD = 9
                YIELD = 10

        class QuoteRespID(Tag):
            Tag = 693
            Type = "STRING"

        class QuoteRespType(Tag):
            Tag = 694
            Type = "INT"
            class Values:
                HIT_LIFT = 1
                COUNTER = 2
                EXPIRED = 3
                COVER = 4
                DONE_AWAY = 5
                PASS = 6
                END_TRADE = 7
                TIMED_OUT = 8

        class QuoteQualifier(Tag):
            Tag = 695
            Type = "CHAR"

        class YieldRedemptionDate(Tag):
            Tag = 696
            Type = "LOCALMKTDATE"

        class YieldRedemptionPrice(Tag):
            Tag = 697
            Type = "PRICE"

        class YieldRedemptionPriceType(Tag):
            Tag = 698
            Type = "INT"

        class BenchmarkSecurityID(Tag):
            Tag = 699
            Type = "STRING"

        class ReversalIndicator(Tag):
            Tag = 700
            Type = "BOOLEAN"

        class YieldCalcDate(Tag):
            Tag = 701
            Type = "LOCALMKTDATE"

        class NoPositions(Tag):
            Tag = 702
            Type = "NUMINGROUP"

        class PosType(Tag):
            Tag = 703
            Type = "STRING"
            class Values:
                ALLOCATION_TRADE_QTY = "ALC"
                OPTION_ASSIGNMENT = "AS"
                AS_OF_TRADE_QTY = "ASF"
                DELIVERY_QTY = "DLV"
                ELECTRONIC_TRADE_QTY = "ETR"
                OPTION_EXERCISE_QTY = "EX"
                END_OF_DAY_QTY = "FIN"
                INTRA_SPREAD_QTY = "IAS"
                INTER_SPREAD_QTY = "IES"
                ADJUSTMENT_QTY = "PA"
                PIT_TRADE_QTY = "PIT"
                START_OF_DAY_QTY = "SOD"
                INTEGRAL_SPLIT = "SPL"
                TRANSACTION_FROM_ASSIGNMENT = "TA"
                TOTAL_TRANSACTION_QTY = "TOT"
                TRANSACTION_QUANTITY = "TQ"
                TRANSFER_TRADE_QTY = "TRF"
                TRANSACTION_FROM_EXERCISE = "TX"
                CROSS_MARGIN_QTY = "XM"
                RECEIVE_QUANTITY = "RCV"
                CORPORATE_ACTION_ADJUSTMENT = "CAA"
                DELIVERY_NOTICE_QTY = "DN"
                EXCHANGE_FOR_PHYSICAL_QTY = "EP"
                PRIVATELY_NEGOTIATED_TRADE_QTY = "PNTN"
                NET_DELTA_QTY = "DLT"
                CREDIT_EVENT_ADJUSTMENT = "CEA"
                SUCCESSION_EVENT_ADJUSTMENT = "SEA"

        class LongQty(Tag):
            Tag = 704
            Type = "QTY"

        class ShortQty(Tag):
            Tag = 705
            Type = "QTY"

        class PosQtyStatus(Tag):
            Tag = 706
            Type = "INT"
            class Values:
                SUBMITTED = 0
                ACCEPTED = 1
                REJECTED = 2

        class PosAmtType(Tag):
            Tag = 707
            Type = "STRING"
            class Values:
                CASH_AMOUNT = "CASH"
                CASH_RESIDUAL_AMOUNT = "CRES"
                FINAL_MARK_TO_MARKET_AMOUNT = "FMTM"
                INCREMENTAL_MARK_TO_MARKET_AMOUNT = "IMTM"
                PREMIUM_AMOUNT = "PREM"
                START_OF_DAY_MARK_TO_MARKET_AMOUNT = "SMTM"
                TRADE_VARIATION_AMOUNT = "TVAR"
                VALUE_ADJUSTED_AMOUNT = "VADJ"
                SETTLEMENT_VALUE = "SETL"
                INITIAL_TRADE_COUPON_AMOUNT = "ICPN"
                ACCRUED_COUPON_AMOUNT = "ACPN"
                COUPON_AMOUNT = "CPN"
                INCREMENTAL_ACCRUED_COUPON = "IACPN"
                COLLATERALIZED_MARK_TO_MARKET = "CMTM"
                INCREMENTAL_COLLATERALIZED_MARK_TO_MARKET = "ICMTM"
                COMPENSATION_AMOUNT = "DLV"
                TOTAL_BANKED_AMOUNT = "BANK"
                TOTAL_COLLATERALIZED_AMOUNT = "COLAT"

        class PosAmt(Tag):
            Tag = 708
            Type = "AMT"

        class PosTransType(Tag):
            Tag = 709
            Type = "INT"
            class Values:
                EXERCISE = 1
                DO_NOT_EXERCISE = 2
                POSITION_ADJUSTMENT = 3
                POSITION_CHANGE_SUBMISSION_MARGIN_DISPOSITION = 4
                PLEDGE = 5
                LARGE_TRADER_SUBMISSION = 6

        class PosReqID(Tag):
            Tag = 710
            Type = "STRING"

        class NoUnderlyings(Tag):
            Tag = 711
            Type = "NUMINGROUP"

        class PosMaintAction(Tag):
            Tag = 712
            Type = "INT"
            class Values:
                NEW = 1
                REPLACE = 2
                CANCEL = 3
                REVERSE = 4

        class OrigPosReqRefID(Tag):
            Tag = 713
            Type = "STRING"

        class PosMaintRptRefID(Tag):
            Tag = 714
            Type = "STRING"

        class ClearingBusinessDate(Tag):
            Tag = 715
            Type = "LOCALMKTDATE"

        class SettlSessID(Tag):
            Tag = 716
            Type = "STRING"
            class Values:
                INTRADAY = "ITD"
                REGULAR_TRADING_HOURS = "RTH"
                ELECTRONIC_TRADING_HOURS = "ETH"
                END_OF_DAY = "EOD"

        class SettlSessSubID(Tag):
            Tag = 717
            Type = "STRING"

        class AdjustmentType(Tag):
            Tag = 718
            Type = "INT"
            class Values:
                PROCESS_REQUEST_AS_MARGIN_DISPOSITION = 0
                DELTA_PLUS = 1
                DELTA_MINUS = 2
                FINAL = 3

        class ContraryInstructionIndicator(Tag):
            Tag = 719
            Type = "BOOLEAN"

        class PriorSpreadIndicator(Tag):
            Tag = 720
            Type = "BOOLEAN"

        class PosMaintRptID(Tag):
            Tag = 721
            Type = "STRING"

        class PosMaintStatus(Tag):
            Tag = 722
            Type = "INT"
            class Values:
                ACCEPTED = 0
                ACCEPTED_WITH_WARNINGS = 1
                REJECTED = 2
                COMPLETED = 3
                COMPLETED_WITH_WARNINGS = 4

        class PosMaintResult(Tag):
            Tag = 723
            Type = "INT"
            class Values:
                SUCCESSFUL_COMPLETION = 0
                REJECTED = 1
                OTHER = 99

        class PosReqType(Tag):
            Tag = 724
            Type = "INT"
            class Values:
                POSITIONS = 0
                TRADES = 1
                EXERCISES = 2
                ASSIGNMENTS = 3
                SETTLEMENT_ACTIVITY = 4
                BACKOUT_MESSAGE = 5
                DELTA_POSITIONS = 6

        class ResponseTransportType(Tag):
            Tag = 725
            Type = "INT"
            class Values:
                INBAND = 0
                OUT_OF_BAND = 1

        class ResponseDestination(Tag):
            Tag = 726
            Type = "STRING"

        class TotalNumPosReports(Tag):
            Tag = 727
            Type = "INT"

        class PosReqResult(Tag):
            Tag = 728
            Type = "INT"
            class Values:
                VALID_REQUEST = 0
                INVALID_OR_UNSUPPORTED_REQUEST = 1
                NO_POSITIONS_FOUND_THAT_MATCH_CRITERIA = 2
                NOT_AUTHORIZED_TO_REQUEST_POSITIONS = 3
                REQUEST_FOR_POSITION_NOT_SUPPORTED = 4
                OTHER = 99

        class PosReqStatus(Tag):
            Tag = 729
            Type = "INT"
            class Values:
                COMPLETED = 0
                COMPLETED_WITH_WARNINGS = 1
                REJECTED = 2

        class SettlPrice(Tag):
            Tag = 730
            Type = "PRICE"

        class SettlPriceType(Tag):
            Tag = 731
            Type = "INT"
            class Values:
                FINAL = 1
                THEORETICAL = 2

        class UnderlyingSettlPrice(Tag):
            Tag = 732
            Type = "PRICE"

        class UnderlyingSettlPriceType(Tag):
            Tag = 733
            Type = "INT"

        class PriorSettlPrice(Tag):
            Tag = 734
            Type = "PRICE"

        class NoQuoteQualifiers(Tag):
            Tag = 735
            Type = "NUMINGROUP"

        class AllocSettlCurrency(Tag):
            Tag = 736
            Type = "CURRENCY"

        class AllocSettlCurrAmt(Tag):
            Tag = 737
            Type = "AMT"

        class InterestAtMaturity(Tag):
            Tag = 738
            Type = "AMT"

        class LegDatedDate(Tag):
            Tag = 739
            Type = "LOCALMKTDATE"

        class LegPool(Tag):
            Tag = 740
            Type = "STRING"

        class AllocInterestAtMaturity(Tag):
            Tag = 741
            Type = "AMT"

        class AllocAccruedInterestAmt(Tag):
            Tag = 742
            Type = "AMT"

        class DeliveryDate(Tag):
            Tag = 743
            Type = "LOCALMKTDATE"

        class AssignmentMethod(Tag):
            Tag = 744
            Type = "CHAR"
            class Values:
                PRO_RATA = "P"
                RANDOM = "R"

        class AssignmentUnit(Tag):
            Tag = 745
            Type = "QTY"

        class OpenInterest(Tag):
            Tag = 746
            Type = "AMT"

        class ExerciseMethod(Tag):
            Tag = 747
            Type = "CHAR"
            class Values:
                AUTOMATIC = "A"
                MANUAL = "M"

        class TotNumTradeReports(Tag):
            Tag = 748
            Type = "INT"

        class TradeRequestResult(Tag):
            Tag = 749
            Type = "INT"
            class Values:
                SUCCESSFUL = 0
                INVALID_OR_UNKNOWN_INSTRUMENT = 1
                INVALID_TYPE_OF_TRADE_REQUESTED = 2
                INVALID_PARTIES = 3
                INVALID_TRANSPORT_TYPE_REQUESTED = 4
                INVALID_DESTINATION_REQUESTED = 5
                TRADEREQUESTTYPE_NOT_SUPPORTED = 8
                NOT_AUTHORIZED = 9
                OTHER = 99

        class TradeRequestStatus(Tag):
            Tag = 750
            Type = "INT"
            class Values:
                ACCEPTED = 0
                COMPLETED = 1
                REJECTED = 2

        class TradeReportRejectReason(Tag):
            Tag = 751
            Type = "INT"
            class Values:
                SUCCESSFUL = 0
                INVALID_PARTY_ONFORMATION = 1
                UNKNOWN_INSTRUMENT = 2
                UNAUTHORIZED_TO_REPORT_TRADES = 3
                INVALID_TRADE_TYPE = 4
                OTHER = 99

        class SideMultiLegReportingType(Tag):
            Tag = 752
            Type = "INT"
            class Values:
                SINGLE_SECURITY = 1
                INDIVIDUAL_LEG_OF_A_MULTILEG_SECURITY = 2
                MULTILEG_SECURITY = 3

        class NoPosAmt(Tag):
            Tag = 753
            Type = "NUMINGROUP"

        class AutoAcceptIndicator(Tag):
            Tag = 754
            Type = "BOOLEAN"

        class AllocReportID(Tag):
            Tag = 755
            Type = "STRING"

        class NoNested2PartyIDs(Tag):
            Tag = 756
            Type = "NUMINGROUP"

        class Nested2PartyID(Tag):
            Tag = 757
            Type = "STRING"

        class Nested2PartyIDSource(Tag):
            Tag = 758
            Type = "CHAR"

        class Nested2PartyRole(Tag):
            Tag = 759
            Type = "INT"

        class Nested2PartySubID(Tag):
            Tag = 760
            Type = "STRING"

        class BenchmarkSecurityIDSource(Tag):
            Tag = 761
            Type = "STRING"

        class SecuritySubType(Tag):
            Tag = 762
            Type = "STRING"

        class UnderlyingSecuritySubType(Tag):
            Tag = 763
            Type = "STRING"

        class LegSecuritySubType(Tag):
            Tag = 764
            Type = "STRING"

        class AllowableOneSidednessPct(Tag):
            Tag = 765
            Type = "PERCENTAGE"

        class AllowableOneSidednessValue(Tag):
            Tag = 766
            Type = "AMT"

        class AllowableOneSidednessCurr(Tag):
            Tag = 767
            Type = "CURRENCY"

        class NoTrdRegTimestamps(Tag):
            Tag = 768
            Type = "NUMINGROUP"

        class TrdRegTimestamp(Tag):
            Tag = 769
            Type = "UTCTIMESTAMP"

        class TrdRegTimestampType(Tag):
            Tag = 770
            Type = "INT"
            class Values:
                EXECUTION_TIME = 1
                TIME_IN = 2
                TIME_OUT = 3
                BROKER_RECEIPT = 4
                BROKER_EXECUTION = 5
                DESK_RECEIPT = 6
                SUBMISSION_TO_CLEARING = 7

        class TrdRegTimestampOrigin(Tag):
            Tag = 771
            Type = "STRING"

        class ConfirmRefID(Tag):
            Tag = 772
            Type = "STRING"

        class ConfirmType(Tag):
            Tag = 773
            Type = "INT"
            class Values:
                STATUS = 1
                CONFIRMATION = 2
                CONFIRMATION_REQUEST_REJECTED = 3

        class ConfirmRejReason(Tag):
            Tag = 774
            Type = "INT"
            class Values:
                MISMATCHED_ACCOUNT = 1
                MISSING_SETTLEMENT_INSTRUCTIONS = 2
                OTHER = 99

        class BookingType(Tag):
            Tag = 775
            Type = "INT"
            class Values:
                REGULAR_BOOKING = 0
                CFD = 1
                TOTAL_RETURN_SWAP = 2

        class IndividualAllocRejCode(Tag):
            Tag = 776
            Type = "INT"

        class SettlInstMsgID(Tag):
            Tag = 777
            Type = "STRING"

        class NoSettlInst(Tag):
            Tag = 778
            Type = "NUMINGROUP"

        class LastUpdateTime(Tag):
            Tag = 779
            Type = "UTCTIMESTAMP"

        class AllocSettlInstType(Tag):
            Tag = 780
            Type = "INT"
            class Values:
                USE_DEFAULT_INSTRUCTIONS = 0
                DERIVE_FROM_PARAMETERS_PROVIDED = 1
                FULL_DETAILS_PROVIDED = 2
                SSI_DB_IDS_PROVIDED = 3
                PHONE_FOR_INSTRUCTIONS = 4

        class NoSettlPartyIDs(Tag):
            Tag = 781
            Type = "NUMINGROUP"

        class SettlPartyID(Tag):
            Tag = 782
            Type = "STRING"

        class SettlPartyIDSource(Tag):
            Tag = 783
            Type = "CHAR"

        class SettlPartyRole(Tag):
            Tag = 784
            Type = "INT"

        class SettlPartySubID(Tag):
            Tag = 785
            Type = "STRING"

        class SettlPartySubIDType(Tag):
            Tag = 786
            Type = "INT"

        class DlvyInstType(Tag):
            Tag = 787
            Type = "CHAR"
            class Values:
                CASH = "C"
                SECURITIES = "S"

        class TerminationType(Tag):
            Tag = 788
            Type = "INT"
            class Values:
                OVERNIGHT = 1
                TERM = 2
                FLEXIBLE = 3
                OPEN = 4

        class NextExpectedMsgSeqNum(Tag):
            Tag = 789
            Type = "SEQNUM"

        class OrdStatusReqID(Tag):
            Tag = 790
            Type = "STRING"

        class SettlInstReqID(Tag):
            Tag = 791
            Type = "STRING"

        class SettlInstReqRejCode(Tag):
            Tag = 792
            Type = "INT"
            class Values:
                UNABLE_TO_PROCESS_REQUEST = 0
                UNKNOWN_ACCOUNT = 1
                NO_MATCHING_SETTLEMENT_INSTRUCTIONS_FOUND = 2
                OTHER = 99

        class SecondaryAllocID(Tag):
            Tag = 793
            Type = "STRING"

        class AllocReportType(Tag):
            Tag = 794
            Type = "INT"
            class Values:
                PRELIMINARY_REQUEST_TO_INTERMEDIARY = 2
                SELLSIDE_CALCULATED_USING_PRELIMINARY = 3
                SELLSIDE_CALCULATED_WITHOUT_PRELIMINARY = 4
                WAREHOUSE_RECAP = 5
                REQUEST_TO_INTERMEDIARY = 8
                ACCEPT = 9
                REJECT = 10
                ACCEPT_PENDING = 11
                COMPLETE = 12
                REVERSE_PENDING = 14

        class AllocReportRefID(Tag):
            Tag = 795
            Type = "STRING"

        class AllocCancReplaceReason(Tag):
            Tag = 796
            Type = "INT"
            class Values:
                ORIGINAL_DETAILS_INCOMPLETE_INCORRECT = 1
                CHANGE_IN_UNDERLYING_ORDER_DETAILS = 2
                OTHER = 99

        class CopyMsgIndicator(Tag):
            Tag = 797
            Type = "BOOLEAN"

        class AllocAccountType(Tag):
            Tag = 798
            Type = "INT"
            class Values:
                ACCOUNT_IS_CARRIED_PN_CUSTOMER_SIDE_OF_BOOKS = 1
                ACCOUNT_IS_CARRIED_ON_NON_CUSTOMER_SIDE_OF_BOOKS = 2
                HOUSE_TRADER = 3
                FLOOR_TRADER = 4
                ACCOUNT_IS_CARRIED_ON_NON_CUSTOMER_SIDE_OF_BOOKS_AND_IS_CROSS_MARGINED = 6
                ACCOUNT_IS_HOUSE_TRADER_AND_IS_CROSS_MARGINED = 7
                JOINT_BACK_OFFICE_ACCOUNT = 8

        class OrderAvgPx(Tag):
            Tag = 799
            Type = "PRICE"

        class OrderBookingQty(Tag):
            Tag = 800
            Type = "QTY"

        class NoSettlPartySubIDs(Tag):
            Tag = 801
            Type = "NUMINGROUP"

        class NoPartySubIDs(Tag):
            Tag = 802
            Type = "NUMINGROUP"

        class PartySubIDType(Tag):
            Tag = 803
            Type = "INT"
            class Values:
                FIRM = 1
                PERSON = 2
                SYSTEM = 3
                APPLICATION = 4
                FULL_LEGAL_NAME_OF_FIRM = 5
                POSTAL_ADDRESS = 6
                PHONE_NUMBER = 7
                EMAIL_ADDRESS = 8
                CONTACT_NAME = 9
                SECURITIES_ACCOUNT_NUMBER = 10
                REGISTRATION_NUMBER = 11
                REGISTERED_ADDRESS_12 = 12
                REGULATORY_STATUS = 13
                REGISTRATION_NAME = 14
                CASH_ACCOUNT_NUMBER = 15
                BIC = 16
                CSD_PARTICIPANT_MEMBER_CODE = 17
                REGISTERED_ADDRESS_18 = 18
                FUND_ACCOUNT_NAME = 19
                TELEX_NUMBER = 20
                FAX_NUMBER = 21
                SECURITIES_ACCOUNT_NAME = 22
                CASH_ACCOUNT_NAME = 23
                DEPARTMENT = 24
                LOCATION_DESK = 25
                POSITION_ACCOUNT_TYPE = 26
                SECURITY_LOCATE_ID = 27
                MARKET_MAKER = 28
                ELIGIBLE_COUNTERPARTY = 29
                PROFESSIONAL_CLIENT = 30
                LOCATION = 31
                EXECUTION_VENUE = 32
                CURRENCY_DELIVERY_IDENTIFIER = 33

        class NoNestedPartySubIDs(Tag):
            Tag = 804
            Type = "NUMINGROUP"

        class NestedPartySubIDType(Tag):
            Tag = 805
            Type = "INT"

        class NoNested2PartySubIDs(Tag):
            Tag = 806
            Type = "NUMINGROUP"

        class Nested2PartySubIDType(Tag):
            Tag = 807
            Type = "INT"

        class AllocIntermedReqType(Tag):
            Tag = 808
            Type = "INT"
            class Values:
                PENDING_ACCEPT = 1
                PENDING_RELEASE = 2
                PENDING_REVERSAL = 3
                ACCEPT = 4
                BLOCK_LEVEL_REJECT = 5
                ACCOUNT_LEVEL_REJECT = 6

        class NoUsernames(Tag):
            Tag = 809
            Type = "NUMINGROUP"

        class UnderlyingPx(Tag):
            Tag = 810
            Type = "PRICE"

        class PriceDelta(Tag):
            Tag = 811
            Type = "FLOAT"

        class ApplQueueMax(Tag):
            Tag = 812
            Type = "INT"

        class ApplQueueDepth(Tag):
            Tag = 813
            Type = "INT"

        class ApplQueueResolution(Tag):
            Tag = 814
            Type = "INT"
            class Values:
                NO_ACTION_TAKEN = 0
                QUEUE_FLUSHED = 1
                OVERLAY_LAST = 2
                END_SESSION = 3

        class ApplQueueAction(Tag):
            Tag = 815
            Type = "INT"
            class Values:
                NO_ACTION_TAKEN = 0
                QUEUE_FLUSHED = 1
                OVERLAY_LAST = 2
                END_SESSION = 3

        class NoAltMDSource(Tag):
            Tag = 816
            Type = "NUMINGROUP"

        class AltMDSourceID(Tag):
            Tag = 817
            Type = "STRING"

        class SecondaryTradeReportID(Tag):
            Tag = 818
            Type = "STRING"

        class AvgPxIndicator(Tag):
            Tag = 819
            Type = "INT"
            class Values:
                NO_AVERAGE_PRICING = 0
                TRADE_IS_PART_OF_AN_AVERAGE_PRICE_GROUP_IDENTIFIED_BY_THE_TRADELINKID = 1
                LAST_TRADE_IS_THE_AVERAGE_PRICE_GROUP_IDENTIFIED_BY_THE_TRADELINKID = 2

        class TradeLinkID(Tag):
            Tag = 820
            Type = "STRING"

        class OrderInputDevice(Tag):
            Tag = 821
            Type = "STRING"

        class UnderlyingTradingSessionID(Tag):
            Tag = 822
            Type = "STRING"

        class UnderlyingTradingSessionSubID(Tag):
            Tag = 823
            Type = "STRING"

        class TradeLegRefID(Tag):
            Tag = 824
            Type = "STRING"

        class ExchangeRule(Tag):
            Tag = 825
            Type = "STRING"

        class TradeAllocIndicator(Tag):
            Tag = 826
            Type = "INT"
            class Values:
                ALLOCATION_NOT_REQUIRED = 0
                ALLOCATION_REQUIRED = 1
                USE_ALLOCATION_PROVIDED_WITH_THE_TRADE = 2
                ALLOCATION_GIVE_UP_EXECUTOR = 3
                ALLOCATION_FROM_EXECUTOR = 4
                ALLOCATION_TO_CLAIM_ACCOUNT = 5

        class ExpirationCycle(Tag):
            Tag = 827
            Type = "INT"
            class Values:
                EXPIRE_ON_TRADING_SESSION_CLOSE = 0
                EXPIRE_ON_TRADING_SESSION_OPEN = 1
                TRADING_ELIGIBILITY_EXPIRATION_SPECIFIED_IN_THE_DATE_AND_TIME_FIELDS_EVENTDATE = 2

        class TrdType(Tag):
            Tag = 828
            Type = "INT"
            class Values:
                REGULAR_TRADE = 0
                BLOCK_TRADE_1 = 1
                EFP = 2
                TRANSFER = 3
                LATE_TRADE = 4
                T_TRADE = 5
                WEIGHTED_AVERAGE_PRICE_TRADE = 6
                BUNCHED_TRADE = 7
                LATE_BUNCHED_TRADE = 8
                PRIOR_REFERENCE_PRICE_TRADE = 9
                AFTER_HOURS_TRADE = 10
                EXCHANGE_FOR_RISK = 11
                EXCHANGE_FOR_SWAP = 12
                EXCHANGE_OF_FUTURES_FOR = 13
                EXCHANGE_OF_OPTIONS_FOR_OPTIONS = 14
                TRADING_AT_SETTLEMENT = 15
                ALL_OR_NONE = 16
                FUTURES_LARGE_ORDER_EXECUTION = 17
                EXCHANGE_OF_FUTURES_FOR_FUTURES = 18
                OPTION_INTERIM_TRADE = 19
                OPTION_CABINET_TRADE = 20
                PRIVATELY_NEGOTIATED_TRADES = 22
                SUBSTITUTION_OF_FUTURES_FOR_FORWARDS = 23
                NON_STANDARD_SETTLEMENT = 48
                DERIVATIVE_RELATED_TRANSACTION = 49
                PORTFOLIO_TRADE = 50
                VOLUME_WEIGHTED_AVERAGE_TRADE = 51
                EXCHANGE_GRANTED_TRADE = 52
                REPURCHASE_AGREEMENT = 53
                OTC = 54
                EXCHANGE_BASIS_FACILITY = 55
                ERROR_TRADE = 24
                SPECIAL_CUM_DIVIDEND = 25
                SPECIAL_EX_DIVIDEND = 26
                SPECIAL_CUM_COUPON = 27
                SPECIAL_EX_COUPON = 28
                CASH_SETTLEMENT = 29
                SPECIAL_PRICE = 30
                GUARANTEED_DELIVERY = 31
                SPECIAL_CUM_RIGHTS = 32
                SPECIAL_EX_RIGHTS = 33
                SPECIAL_CUM_CAPITAL_REPAYMENTS = 34
                SPECIAL_EX_CAPITAL_REPAYMENTS = 35
                SPECIAL_CUM_BONUS = 36
                SPECIAL_EX_BONUS = 37
                BLOCK_TRADE_38 = 38
                WORKED_PRINCIPAL_TRADE = 39
                BLOCK_TRADES = 40
                NAME_CHANGE = 41
                PORTFOLIO_TRANSFER = 42
                PROROGATION_BUY = 43
                PROROGATION_SELL = 44
                OPTION_EXERCISE = 45
                DELTA_NEUTRAL_TRANSACTION = 46
                FINANCING_TRANSACTION = 47

        class TrdSubType(Tag):
            Tag = 829
            Type = "INT"
            class Values:
                CMTA = 0
                INTERNAL_TRANSFER_OR_ADJUSTMENT = 1
                EXTERNAL_TRANSFER_OR_TRANSFER_OF_ACCOUNT = 2
                REJECT_FOR_SUBMITTING_SIDE = 3
                ADVISORY_FOR_CONTRA_SIDE = 4
                OFFSET_DUE_TO_AN_ALLOCATION = 5
                ONSET_DUE_TO_AN_ALLOCATION = 6
                DIFFERENTIAL_SPREAD = 7
                IMPLIED_SPREAD_LEG_EXECUTED_AGAINST_AN_OUTRIGHT = 8
                TRANSACTION_FROM_EXERCISE = 9
                TRANSACTION_FROM_ASSIGNMENT = 10
                ACATS = 11
                OFF_HOURS_TRADE = 33
                ON_HOURS_TRADE = 34
                OTC_QUOTE = 35
                CONVERTED_SWAP = 36
                AI = 14
                B = 15
                K = 16
                LC = 17
                M = 18
                N = 19
                NM = 20
                NR = 21
                P = 22
                PA = 23
                PC = 24
                PN = 25
                R = 26
                RO = 27
                RT = 28
                SW = 29
                T = 30
                WN = 31
                WT = 32
                CROSSED_TRADE = 37
                INTERIM_PROTECTED_TRADE = 38
                LARGE_IN_SCALE = 39

        class TransferReason(Tag):
            Tag = 830
            Type = "STRING"

        class TotNumAssignmentReports(Tag):
            Tag = 832
            Type = "INT"

        class AsgnRptID(Tag):
            Tag = 833
            Type = "STRING"

        class ThresholdAmount(Tag):
            Tag = 834
            Type = "PRICEOFFSET"

        class PegMoveType(Tag):
            Tag = 835
            Type = "INT"
            class Values:
                FLOATING = 0
                FIXED = 1

        class PegOffsetType(Tag):
            Tag = 836
            Type = "INT"
            class Values:
                PRICE = 0
                BASIS_POINTS = 1
                TICKS = 2
                PRICE_TIER = 3

        class PegLimitType(Tag):
            Tag = 837
            Type = "INT"
            class Values:
                OR_BETTER = 0
                STRICT = 1
                OR_WORSE = 2

        class PegRoundDirection(Tag):
            Tag = 838
            Type = "INT"
            class Values:
                MORE_AGGRESSIVE = 1
                MORE_PASSIVE = 2

        class PeggedPrice(Tag):
            Tag = 839
            Type = "PRICE"

        class PegScope(Tag):
            Tag = 840
            Type = "INT"
            class Values:
                LOCAL = 1
                NATIONAL = 2
                GLOBAL = 3
                NATIONAL_EXCLUDING_LOCAL = 4

        class DiscretionMoveType(Tag):
            Tag = 841
            Type = "INT"
            class Values:
                FLOATING = 0
                FIXED = 1

        class DiscretionOffsetType(Tag):
            Tag = 842
            Type = "INT"
            class Values:
                PRICE = 0
                BASIS_POINTS = 1
                TICKS = 2
                PRICE_TIER = 3

        class DiscretionLimitType(Tag):
            Tag = 843
            Type = "INT"
            class Values:
                OR_BETTER = 0
                STRICT = 1
                OR_WORSE = 2

        class DiscretionRoundDirection(Tag):
            Tag = 844
            Type = "INT"
            class Values:
                MORE_AGGRESSIVE = 1
                MORE_PASSIVE = 2

        class DiscretionPrice(Tag):
            Tag = 845
            Type = "PRICE"

        class DiscretionScope(Tag):
            Tag = 846
            Type = "INT"
            class Values:
                LOCAL = 1
                NATIONAL = 2
                GLOBAL = 3
                NATIONAL_EXCLUDING_LOCAL = 4

        class TargetStrategy(Tag):
            Tag = 847
            Type = "INT"
            class Values:
                VWAP = 1
                PARTICIPATE = 2
                MININIZE_MARKET_IMPACT = 3

        class TargetStrategyParameters(Tag):
            Tag = 848
            Type = "STRING"

        class ParticipationRate(Tag):
            Tag = 849
            Type = "PERCENTAGE"

        class TargetStrategyPerformance(Tag):
            Tag = 850
            Type = "FLOAT"

        class LastLiquidityInd(Tag):
            Tag = 851
            Type = "INT"
            class Values:
                ADDED_LIQUIDITY = 1
                REMOVED_LIQUIDITY = 2
                LIQUIDITY_ROUTED_OUT = 3
                AUCTION = 4

        class PublishTrdIndicator(Tag):
            Tag = 852
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class ShortSaleReason(Tag):
            Tag = 853
            Type = "INT"
            class Values:
                DEALER_SOLD_SHORT = 0
                DEALER_SOLD_SHORT_EXEMPT = 1
                SELLING_CUSTOMER_SOLD_SHORT = 2
                SELLING_CUSTOMER_SOLD_SHORT_EXEMPT = 3
                QUALIFIED_SERVICE_REPRESENTATIVE = 4
                QSR_OR_AGU_CONTRA_SIDE_SOLD_SHORT_EXEMPT = 5

        class QtyType(Tag):
            Tag = 854
            Type = "INT"
            class Values:
                UNITS = 0
                CONTRACTS = 1
                UNITS_OF_MEASURE_PER_TIME_UNIT = 2

        class SecondaryTrdType(Tag):
            Tag = 855
            Type = "INT"

        class TradeReportType(Tag):
            Tag = 856
            Type = "INT"
            class Values:
                SUBMIT = 0
                ALLEGED_1 = 1
                ACCEPT = 2
                DECLINE = 3
                ADDENDUM = 4
                NO_WAS = 5
                TRADE_REPORT_CANCEL = 6
                N7 = 7
                DEFAULTED = 8
                INVALID_CMTA = 9
                PENDED = 10
                ALLEGED_NEW = 11
                ALLEGED_ADDENDUM = 12
                ALLEGED_NO_WAS = 13
                ALLEGED_TRADE_REPORT_CANCEL = 14
                ALLEGED_15 = 15

        class AllocNoOrdersType(Tag):
            Tag = 857
            Type = "INT"
            class Values:
                NOT_SPECIFIED = 0
                EXPLICIT_LIST_PROVIDED = 1

        class SharedCommission(Tag):
            Tag = 858
            Type = "AMT"

        class ConfirmReqID(Tag):
            Tag = 859
            Type = "STRING"

        class AvgParPx(Tag):
            Tag = 860
            Type = "PRICE"

        class ReportedPx(Tag):
            Tag = 861
            Type = "PRICE"

        class NoCapacities(Tag):
            Tag = 862
            Type = "NUMINGROUP"

        class OrderCapacityQty(Tag):
            Tag = 863
            Type = "QTY"

        class NoEvents(Tag):
            Tag = 864
            Type = "NUMINGROUP"

        class EventType(Tag):
            Tag = 865
            Type = "INT"
            class Values:
                PUT = 1
                CALL = 2
                TENDER = 3
                SINKING_FUND_CALL = 4
                ACTIVATION = 5
                INACTIVIATION = 6
                LAST_ELIGIBLE_TRADE_DATE = 7
                SWAP_START_DATE = 8
                SWAP_END_DATE = 9
                SWAP_ROLL_DATE = 10
                SWAP_NEXT_START_DATE = 11
                SWAP_NEXT_ROLL_DATE = 12
                FIRST_DELIVERY_DATE = 13
                LAST_DELIVERY_DATE = 14
                INITIAL_INVENTORY_DUE_DATE = 15
                FINAL_INVENTORY_DUE_DATE = 16
                FIRST_INTENT_DATE = 17
                LAST_INTENT_DATE = 18
                POSITION_REMOVAL_DATE = 19
                OTHER = 99

        class EventDate(Tag):
            Tag = 866
            Type = "LOCALMKTDATE"

        class EventPx(Tag):
            Tag = 867
            Type = "PRICE"

        class EventText(Tag):
            Tag = 868
            Type = "STRING"

        class PctAtRisk(Tag):
            Tag = 869
            Type = "PERCENTAGE"

        class NoInstrAttrib(Tag):
            Tag = 870
            Type = "NUMINGROUP"

        class InstrAttribType(Tag):
            Tag = 871
            Type = "INT"
            class Values:
                FLAT = 1
                ZERO_COUPON = 2
                INTEREST_BEARING = 3
                NO_PERIODIC_PAYMENTS = 4
                VARIABLE_RATE = 5
                LESS_FEE_FOR_PUT = 6
                STEPPED_COUPON = 7
                COUPON_PERIOD = 8
                WHEN_AND_IF_ISSUED = 9
                ORIGINAL_ISSUE_DISCOUNT = 10
                CALLABLE_PUTTABLE = 11
                ESCROWED_TO_MATURITY = 12
                ESCROWED_TO_REDEMPTION_DATE = 13
                PRE_REFUNDED = 14
                IN_DEFAULT = 15
                UNRATED = 16
                TAXABLE = 17
                INDEXED = 18
                SUBJECT_TO_ALTERNATIVE_MINIMUM_TAX = 19
                ORIGINAL_ISSUE_DISCOUNT_PRICE_SUPPLY_PRICE_IN_THE_INSTRATTRIBVALUE = 20
                CALLABLE_BELOW_MATURITY_VALUE = 21
                CALLABLE_WITHOUT_NOTICE_BY_MAIL_TO_HOLDER_UNLESS_REGISTERED = 22
                PRICE_TICK_RULES_FOR_SECURITY = 23
                TRADE_TYPE_ELIGIBILITY_DETAILS_FOR_SECURITY = 24
                INSTRUMENT_DENOMINATOR = 25
                INSTRUMENT_NUMERATOR = 26
                INSTRUMENT_PRICE_PRECISION = 27
                INSTRUMENT_STRIKE_PRICE = 28
                TRADEABLE_INDICATOR = 29
                TEXT_SUPPLY_THE_TEXT_OF_THE_ATTRIBUTE_OR_DISCLAIMER_IN_THE_INSTRATTRIBVALUE = 99

        class InstrAttribValue(Tag):
            Tag = 872
            Type = "STRING"

        class DatedDate(Tag):
            Tag = 873
            Type = "LOCALMKTDATE"

        class InterestAccrualDate(Tag):
            Tag = 874
            Type = "LOCALMKTDATE"

        class CPProgram(Tag):
            Tag = 875
            Type = "INT"
            class Values:
                N3 = 1
                N4 = 2
                OTHER = 99

        class CPRegType(Tag):
            Tag = 876
            Type = "STRING"

        class UnderlyingCPProgram(Tag):
            Tag = 877
            Type = "STRING"

        class UnderlyingCPRegType(Tag):
            Tag = 878
            Type = "STRING"

        class UnderlyingQty(Tag):
            Tag = 879
            Type = "QTY"

        class TrdMatchID(Tag):
            Tag = 880
            Type = "STRING"

        class SecondaryTradeReportRefID(Tag):
            Tag = 881
            Type = "STRING"

        class UnderlyingDirtyPrice(Tag):
            Tag = 882
            Type = "PRICE"

        class UnderlyingEndPrice(Tag):
            Tag = 883
            Type = "PRICE"

        class UnderlyingStartValue(Tag):
            Tag = 884
            Type = "AMT"

        class UnderlyingCurrentValue(Tag):
            Tag = 885
            Type = "AMT"

        class UnderlyingEndValue(Tag):
            Tag = 886
            Type = "AMT"

        class NoUnderlyingStips(Tag):
            Tag = 887
            Type = "NUMINGROUP"

        class UnderlyingStipType(Tag):
            Tag = 888
            Type = "STRING"

        class UnderlyingStipValue(Tag):
            Tag = 889
            Type = "STRING"

        class MaturityNetMoney(Tag):
            Tag = 890
            Type = "AMT"

        class MiscFeeBasis(Tag):
            Tag = 891
            Type = "INT"
            class Values:
                ABSOLUTE = 0
                PER_UNIT = 1
                PERCENTAGE = 2

        class TotNoAllocs(Tag):
            Tag = 892
            Type = "INT"

        class LastFragment(Tag):
            Tag = 893
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class CollReqID(Tag):
            Tag = 894
            Type = "STRING"

        class CollAsgnReason(Tag):
            Tag = 895
            Type = "INT"
            class Values:
                INITIAL = 0
                SCHEDULED = 1
                TIME_WARNING = 2
                MARGIN_DEFICIENCY = 3
                MARGIN_EXCESS = 4
                FORWARD_COLLATERAL_DEMAND = 5
                EVENT_OF_DEFAULT = 6
                ADVERSE_TAX_EVENT = 7

        class CollInquiryQualifier(Tag):
            Tag = 896
            Type = "INT"
            class Values:
                TRADE_DATE = 0
                GC_INSTRUMENT = 1
                COLLATERAL_INSTRUMENT = 2
                SUBSTITUTION_ELIGIBLE = 3
                NOT_ASSIGNED = 4
                PARTIALLY_ASSIGNED = 5
                FULLY_ASSIGNED = 6
                OUTSTANDING_TRADES = 7

        class NoTrades(Tag):
            Tag = 897
            Type = "NUMINGROUP"

        class MarginRatio(Tag):
            Tag = 898
            Type = "PERCENTAGE"

        class MarginExcess(Tag):
            Tag = 899
            Type = "AMT"

        class TotalNetValue(Tag):
            Tag = 900
            Type = "AMT"

        class CashOutstanding(Tag):
            Tag = 901
            Type = "AMT"

        class CollAsgnID(Tag):
            Tag = 902
            Type = "STRING"

        class CollAsgnTransType(Tag):
            Tag = 903
            Type = "INT"
            class Values:
                NEW = 0
                REPLACE = 1
                CANCEL = 2
                RELEASE = 3
                REVERSE = 4

        class CollRespID(Tag):
            Tag = 904
            Type = "STRING"

        class CollAsgnRespType(Tag):
            Tag = 905
            Type = "INT"
            class Values:
                RECEIVED = 0
                ACCEPTED = 1
                DECLINED = 2
                REJECTED = 3

        class CollAsgnRejectReason(Tag):
            Tag = 906
            Type = "INT"
            class Values:
                UNKNOWN_DEAL = 0
                UNKNOWN_OR_INVALID_INSTRUMENT = 1
                UNAUTHORIZED_TRANSACTION = 2
                INSUFFICIENT_COLLATERAL = 3
                INVALID_TYPE_OF_COLLATERAL = 4
                EXCESSIVE_SUBSTITUTION = 5
                OTHER = 99

        class CollAsgnRefID(Tag):
            Tag = 907
            Type = "STRING"

        class CollRptID(Tag):
            Tag = 908
            Type = "STRING"

        class CollInquiryID(Tag):
            Tag = 909
            Type = "STRING"

        class CollStatus(Tag):
            Tag = 910
            Type = "INT"
            class Values:
                UNASSIGNED = 0
                PARTIALLY_ASSIGNED = 1
                ASSIGNMENT_PROPOSED = 2
                ASSIGNED = 3
                CHALLENGED = 4

        class TotNumReports(Tag):
            Tag = 911
            Type = "INT"

        class LastRptRequested(Tag):
            Tag = 912
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class AgreementDesc(Tag):
            Tag = 913
            Type = "STRING"

        class AgreementID(Tag):
            Tag = 914
            Type = "STRING"

        class AgreementDate(Tag):
            Tag = 915
            Type = "LOCALMKTDATE"

        class StartDate(Tag):
            Tag = 916
            Type = "LOCALMKTDATE"

        class EndDate(Tag):
            Tag = 917
            Type = "LOCALMKTDATE"

        class AgreementCurrency(Tag):
            Tag = 918
            Type = "CURRENCY"

        class DeliveryType(Tag):
            Tag = 919
            Type = "INT"
            class Values:
                VERSUS_PAYMENT_DELIVER = 0
                FREE_DELIVER = 1
                TRI_PARTY = 2
                HOLD_IN_CUSTODY = 3

        class EndAccruedInterestAmt(Tag):
            Tag = 920
            Type = "AMT"

        class StartCash(Tag):
            Tag = 921
            Type = "AMT"

        class EndCash(Tag):
            Tag = 922
            Type = "AMT"

        class UserRequestID(Tag):
            Tag = 923
            Type = "STRING"

        class UserRequestType(Tag):
            Tag = 924
            Type = "INT"
            class Values:
                LOG_ON_USER = 1
                LOG_OFF_USER = 2
                CHANGE_PASSWORD_FOR_USER = 3
                REQUEST_INDIVIDUAL_USER_STATUS = 4

        class NewPassword(Tag):
            Tag = 925
            Type = "STRING"

        class UserStatus(Tag):
            Tag = 926
            Type = "INT"
            class Values:
                LOGGED_IN = 1
                NOT_LOGGED_IN = 2
                USER_NOT_RECOGNISED = 3
                PASSWORD_INCORRECT = 4
                PASSWORD_CHANGED = 5
                OTHER = 6
                FORCED_USER_LOGOUT_BY_EXCHANGE = 7
                SESSION_SHUTDOWN_WARNING = 8

        class UserStatusText(Tag):
            Tag = 927
            Type = "STRING"

        class StatusValue(Tag):
            Tag = 928
            Type = "INT"
            class Values:
                CONNECTED = 1
                NOT_CONNECTED_2 = 2
                NOT_CONNECTED_3 = 3
                IN_PROCESS = 4

        class StatusText(Tag):
            Tag = 929
            Type = "STRING"

        class RefCompID(Tag):
            Tag = 930
            Type = "STRING"

        class RefSubID(Tag):
            Tag = 931
            Type = "STRING"

        class NetworkResponseID(Tag):
            Tag = 932
            Type = "STRING"

        class NetworkRequestID(Tag):
            Tag = 933
            Type = "STRING"

        class LastNetworkResponseID(Tag):
            Tag = 934
            Type = "STRING"

        class NetworkRequestType(Tag):
            Tag = 935
            Type = "INT"
            class Values:
                SNAPSHOT = 1
                SUBSCRIBE = 2
                STOP_SUBSCRIBING = 4
                LEVEL_OF_DETAIL_THEN_NOCOMPIDS_BECOMES_REQUIRED = 8

        class NoCompIDs(Tag):
            Tag = 936
            Type = "NUMINGROUP"

        class NetworkStatusResponseType(Tag):
            Tag = 937
            Type = "INT"
            class Values:
                FULL = 1
                INCREMENTAL_UPDATE = 2

        class NoCollInquiryQualifier(Tag):
            Tag = 938
            Type = "NUMINGROUP"

        class TrdRptStatus(Tag):
            Tag = 939
            Type = "INT"
            class Values:
                ACCEPTED = 0
                REJECTED = 1
                ACCEPTED_WITH_ERRORS = 3

        class AffirmStatus(Tag):
            Tag = 940
            Type = "INT"
            class Values:
                RECEIVED = 1
                CONFIRM_REJECTED_IE_NOT_AFFIRMED = 2
                AFFIRMED = 3

        class UnderlyingStrikeCurrency(Tag):
            Tag = 941
            Type = "CURRENCY"

        class LegStrikeCurrency(Tag):
            Tag = 942
            Type = "CURRENCY"

        class TimeBracket(Tag):
            Tag = 943
            Type = "STRING"

        class CollAction(Tag):
            Tag = 944
            Type = "INT"
            class Values:
                RETAIN = 0
                ADD = 1
                REMOVE = 2

        class CollInquiryStatus(Tag):
            Tag = 945
            Type = "INT"
            class Values:
                ACCEPTED = 0
                ACCEPTED_WITH_WARNINGS = 1
                COMPLETED = 2
                COMPLETED_WITH_WARNINGS = 3
                REJECTED = 4

        class CollInquiryResult(Tag):
            Tag = 946
            Type = "INT"
            class Values:
                SUCCESSFUL = 0
                INVALID_OR_UNKNOWN_INSTRUMENT = 1
                INVALID_OR_UNKNOWN_COLLATERAL_TYPE = 2
                INVALID_PARTIES = 3
                INVALID_TRANSPORT_TYPE_REQUESTED = 4
                INVALID_DESTINATION_REQUESTED = 5
                NO_COLLATERAL_FOUND_FOR_THE_TRADE_SPECIFIED = 6
                NO_COLLATERAL_FOUND_FOR_THE_ORDER_SPECIFIED = 7
                COLLATERAL_INQUIRY_TYPE_NOT_SUPPORTED = 8
                UNAUTHORIZED_FOR_COLLATERAL_INQUIRY = 9
                OTHER = 99

        class StrikeCurrency(Tag):
            Tag = 947
            Type = "CURRENCY"

        class NoNested3PartyIDs(Tag):
            Tag = 948
            Type = "NUMINGROUP"

        class Nested3PartyID(Tag):
            Tag = 949
            Type = "STRING"

        class Nested3PartyIDSource(Tag):
            Tag = 950
            Type = "CHAR"

        class Nested3PartyRole(Tag):
            Tag = 951
            Type = "INT"

        class NoNested3PartySubIDs(Tag):
            Tag = 952
            Type = "NUMINGROUP"

        class Nested3PartySubID(Tag):
            Tag = 953
            Type = "STRING"

        class Nested3PartySubIDType(Tag):
            Tag = 954
            Type = "INT"

        class LegContractSettlMonth(Tag):
            Tag = 955
            Type = "MONTHYEAR"

        class LegInterestAccrualDate(Tag):
            Tag = 956
            Type = "LOCALMKTDATE"

        class NoStrategyParameters(Tag):
            Tag = 957
            Type = "NUMINGROUP"

        class StrategyParameterName(Tag):
            Tag = 958
            Type = "STRING"

        class StrategyParameterType(Tag):
            Tag = 959
            Type = "INT"
            class Values:
                INT = 1
                LENGTH = 2
                NUMINGROUP = 3
                SEQNUM = 4
                TAGNUM = 5
                FLOAT = 6
                QTY = 7
                PRICE = 8
                PRICEOFFSET = 9
                AMT = 10
                PERCENTAGE = 11
                CHAR = 12
                BOOLEAN = 13
                STRING = 14
                MULTIPLECHARVALUE = 15
                CURRENCY = 16
                EXCHANGE = 17
                MONTHYEAR = 18
                UTCTIMESTAMP = 19
                UTCTIMEONLY = 20
                LOCALMKTDATE = 21
                UTCDATEONLY = 22
                DATA = 23
                MULTIPLESTRINGVALUE = 24
                COUNTRY = 25
                LANGUAGE = 26
                TZTIMEONLY = 27
                TZTIMESTAMP = 28
                TENOR = 29

        class StrategyParameterValue(Tag):
            Tag = 960
            Type = "STRING"

        class HostCrossID(Tag):
            Tag = 961
            Type = "STRING"

        class SideTimeInForce(Tag):
            Tag = 962
            Type = "UTCTIMESTAMP"

        class MDReportID(Tag):
            Tag = 963
            Type = "INT"

        class SecurityReportID(Tag):
            Tag = 964
            Type = "INT"

        class SecurityStatus(Tag):
            Tag = 965
            Type = "STRING"
            class Values:
                ACTIVE = "1"
                INACTIVE = "2"

        class SettleOnOpenFlag(Tag):
            Tag = 966
            Type = "STRING"

        class StrikeMultiplier(Tag):
            Tag = 967
            Type = "FLOAT"

        class StrikeValue(Tag):
            Tag = 968
            Type = "FLOAT"

        class MinPriceIncrement(Tag):
            Tag = 969
            Type = "FLOAT"

        class PositionLimit(Tag):
            Tag = 970
            Type = "INT"

        class NTPositionLimit(Tag):
            Tag = 971
            Type = "INT"

        class UnderlyingAllocationPercent(Tag):
            Tag = 972
            Type = "PERCENTAGE"

        class UnderlyingCashAmount(Tag):
            Tag = 973
            Type = "AMT"

        class UnderlyingCashType(Tag):
            Tag = 974
            Type = "STRING"
            class Values:
                FIXED = "FIXED"
                DIFF = "DIFF"

        class UnderlyingSettlementType(Tag):
            Tag = 975
            Type = "INT"
            class Values:
                T_PLUS_1 = 2
                T_PLUS_3 = 4
                T_PLUS_4 = 5

        class QuantityDate(Tag):
            Tag = 976
            Type = "LOCALMKTDATE"

        class ContIntRptID(Tag):
            Tag = 977
            Type = "STRING"

        class LateIndicator(Tag):
            Tag = 978
            Type = "BOOLEAN"

        class InputSource(Tag):
            Tag = 979
            Type = "STRING"

        class SecurityUpdateAction(Tag):
            Tag = 980
            Type = "CHAR"
            class Values:
                ADD = "A"
                DELETE = "D"
                MODIFY = "M"

        class NoExpiration(Tag):
            Tag = 981
            Type = "NUMINGROUP"

        class ExpirationQtyType(Tag):
            Tag = 982
            Type = "INT"
            class Values:
                AUTO_EXERCISE = 1
                NON_AUTO_EXERCISE = 2
                FINAL_WILL_BE_EXERCISED = 3
                CONTRARY_INTENTION = 4
                DIFFERENCE = 5

        class ExpQty(Tag):
            Tag = 983
            Type = "QTY"

        class NoUnderlyingAmounts(Tag):
            Tag = 984
            Type = "NUMINGROUP"

        class UnderlyingPayAmount(Tag):
            Tag = 985
            Type = "AMT"

        class UnderlyingCollectAmount(Tag):
            Tag = 986
            Type = "AMT"

        class UnderlyingSettlementDate(Tag):
            Tag = 987
            Type = "LOCALMKTDATE"

        class UnderlyingSettlementStatus(Tag):
            Tag = 988
            Type = "STRING"

        class SecondaryIndividualAllocID(Tag):
            Tag = 989
            Type = "STRING"

        class LegReportID(Tag):
            Tag = 990
            Type = "STRING"

        class RndPx(Tag):
            Tag = 991
            Type = "PRICE"

        class IndividualAllocType(Tag):
            Tag = 992
            Type = "INT"
            class Values:
                SUB_ALLOCATE = 1
                THIRD_PARTY_ALLOCATION = 2

        class AllocCustomerCapacity(Tag):
            Tag = 993
            Type = "STRING"

        class TierCode(Tag):
            Tag = 994
            Type = "STRING"

        class UnitOfMeasure(Tag):
            Tag = 996
            Type = "STRING"
            class Values:
                BILLION_CUBIC_FEET = "Bcf"
                MILLION_BARRELS = "MMbbl"
                ONE_MILLION_BTU = "MMBtu"
                MEGAWATT_HOURS = "MWh"
                BARRELS = "Bbl"
                BUSHELS = "Bu"
                POUNDS = "lbs"
                GALLONS = "Gal"
                TROY_OUNCES = "oz_tr"
                METRIC_TONS = "t"
                TONS = "tn"
                US_DOLLARS = "USD"
                ALLOWANCES = "Alw"

        class TimeUnit(Tag):
            Tag = 997
            Type = "STRING"
            class Values:
                HOUR = "H"
                MINUTE = "Min"
                SECOND = "S"
                DAY = "D"
                WEEK = "Wk"
                MONTH = "Mo"
                YEAR = "Yr"

        class UnderlyingUnitOfMeasure(Tag):
            Tag = 998
            Type = "STRING"

        class LegUnitOfMeasure(Tag):
            Tag = 999
            Type = "STRING"

        class UnderlyingTimeUnit(Tag):
            Tag = 1000
            Type = "STRING"

        class LegTimeUnit(Tag):
            Tag = 1001
            Type = "STRING"

        class AllocMethod(Tag):
            Tag = 1002
            Type = "INT"
            class Values:
                AUTOMATIC = 1
                GUARANTOR = 2
                MANUAL = 3

        class TradeID(Tag):
            Tag = 1003
            Type = "STRING"

        class SideTradeReportID(Tag):
            Tag = 1005
            Type = "STRING"

        class SideFillStationCd(Tag):
            Tag = 1006
            Type = "STRING"

        class SideReasonCd(Tag):
            Tag = 1007
            Type = "STRING"

        class SideTrdSubTyp(Tag):
            Tag = 1008
            Type = "INT"

        class SideLastQty(Tag):
            Tag = 1009
            Type = "INT"

        class MessageEventSource(Tag):
            Tag = 1011
            Type = "STRING"

        class SideTrdRegTimestamp(Tag):
            Tag = 1012
            Type = "UTCTIMESTAMP"

        class SideTrdRegTimestampType(Tag):
            Tag = 1013
            Type = "INT"

        class SideTrdRegTimestampSrc(Tag):
            Tag = 1014
            Type = "STRING"

        class AsOfIndicator(Tag):
            Tag = 1015
            Type = "CHAR"
            class Values:
                FALSE = "0"
                TRUE = "1"

        class NoSideTrdRegTS(Tag):
            Tag = 1016
            Type = "NUMINGROUP"

        class LegOptionRatio(Tag):
            Tag = 1017
            Type = "FLOAT"

        class NoInstrumentParties(Tag):
            Tag = 1018
            Type = "NUMINGROUP"

        class InstrumentPartyID(Tag):
            Tag = 1019
            Type = "STRING"

        class TradeVolume(Tag):
            Tag = 1020
            Type = "QTY"

        class MDBookType(Tag):
            Tag = 1021
            Type = "INT"
            class Values:
                TOP_OF_BOOK = 1
                PRICE_DEPTH = 2
                ORDER_DEPTH = 3

        class MDFeedType(Tag):
            Tag = 1022
            Type = "STRING"

        class MDPriceLevel(Tag):
            Tag = 1023
            Type = "INT"

        class MDOriginType(Tag):
            Tag = 1024
            Type = "INT"
            class Values:
                BOOK = 0
                OFF_BOOK = 1
                CROSS = 2

        class FirstPx(Tag):
            Tag = 1025
            Type = "PRICE"

        class MDEntrySpotRate(Tag):
            Tag = 1026
            Type = "FLOAT"

        class MDEntryForwardPoints(Tag):
            Tag = 1027
            Type = "PRICEOFFSET"

        class ManualOrderIndicator(Tag):
            Tag = 1028
            Type = "BOOLEAN"

        class CustDirectedOrder(Tag):
            Tag = 1029
            Type = "BOOLEAN"

        class ReceivedDeptID(Tag):
            Tag = 1030
            Type = "STRING"

        class CustOrderHandlingInst(Tag):
            Tag = 1031
            Type = "MULTIPLESTRINGVALUE"
            class Values:
                ADD_ON_ORDER = "ADD"
                ALL_OR_NONE = "AON"
                CASH_NOT_HELD = "CNH"
                DIRECTED_ORDER = "DIR"
                EXCHANGE_FOR_PHYSICAL_TRANSACTION = "E.W"
                FILL_OR_KILL = "FOK"
                IMBALANCE_ONLY = "IO"
                IMMEDIATE_OR_CANCEL = "IOC"
                LIMIT_ON_OPEN = "LOO"
                LIMIT_ON_CLOSE = "LOC"
                MARKET_AT_OPEN = "MAO"
                MARKET_AT_CLOSE = "MAC"
                MARKET_ON_OPEN = "MOO"
                MARKET_ON_CLOSE = "MOC"
                MINIMUM_QUANTITY = "MQT"
                NOT_HELD = "NH"
                OVER_THE_DAY = "OVD"
                PEGGED = "PEG"
                RESERVE_SIZE_ORDER = "RSV"
                STOP_STOCK_TRANSACTION = "S.W"
                SCALE = "SCL"
                TIME_ORDER = "TMO"
                TRAILING_STOP = "TS"
                WORK = "WRK"

        class OrderHandlingInstSource(Tag):
            Tag = 1032
            Type = "INT"
            class Values:
                NASD_OATS = 1

        class DeskType(Tag):
            Tag = 1033
            Type = "STRING"
            class Values:
                AGENCY = "A"
                ARBITRAGE = "AR"
                DERIVATIVES = "D"
                INTERNATIONAL = "IN"
                INSTITUTIONAL = "IS"
                OTHER = "O"
                PREFERRED_TRADING = "PF"
                PROPRIETARY = "PR"
                PROGRAM_TRADING = "PT"
                SALES = "S"
                TRADING = "T"

        class DeskTypeSource(Tag):
            Tag = 1034
            Type = "INT"
            class Values:
                NASD_OATS = 1

        class DeskOrderHandlingInst(Tag):
            Tag = 1035
            Type = "MULTIPLESTRINGVALUE"
            class Values:
                ADD_ON_ORDER = "ADD"
                ALL_OR_NONE = "AON"
                CASH_NOT_HELD = "CNH"
                DIRECTED_ORDER = "DIR"
                EXCHANGE_FOR_PHYSICAL_TRANSACTION = "E.W"
                FILL_OR_KILL = "FOK"
                IMBALANCE_ONLY = "IO"
                IMMEDIATE_OR_CANCEL = "IOC"
                LIMIT_ON_OPEN = "LOO"
                LIMIT_ON_CLOSE = "LOC"
                MARKET_AT_OPEN = "MAO"
                MARKET_AT_CLOSE = "MAC"
                MARKET_ON_OPEN = "MOO"
                MARKET_ON_CLOSE = "MOC"
                MINIMUM_QUANTITY = "MQT"
                NOT_HELD = "NH"
                OVER_THE_DAY = "OVD"
                PEGGED = "PEG"
                RESERVE_SIZE_ORDER = "RSV"
                STOP_STOCK_TRANSACTION = "S.W"
                SCALE = "SCL"
                TIME_ORDER = "TMO"
                TRAILING_STOP = "TS"
                WORK = "WRK"

        class ExecAckStatus(Tag):
            Tag = 1036
            Type = "CHAR"
            class Values:
                RECEIVED_NOT_YET_PROCESSED = "0"
                ACCEPTED = "1"
                DONT_KNOW = "2"

        class UnderlyingDeliveryAmount(Tag):
            Tag = 1037
            Type = "AMT"

        class UnderlyingCapValue(Tag):
            Tag = 1038
            Type = "AMT"

        class UnderlyingSettlMethod(Tag):
            Tag = 1039
            Type = "STRING"

        class SecondaryTradeID(Tag):
            Tag = 1040
            Type = "STRING"

        class FirmTradeID(Tag):
            Tag = 1041
            Type = "STRING"

        class SecondaryFirmTradeID(Tag):
            Tag = 1042
            Type = "STRING"

        class CollApplType(Tag):
            Tag = 1043
            Type = "INT"
            class Values:
                SPECIFIC_DEPOSIT = 0
                GENERAL = 1

        class UnderlyingAdjustedQuantity(Tag):
            Tag = 1044
            Type = "QTY"

        class UnderlyingFXRate(Tag):
            Tag = 1045
            Type = "FLOAT"

        class UnderlyingFXRateCalc(Tag):
            Tag = 1046
            Type = "CHAR"
            class Values:
                DIVIDE = "D"
                MULTIPLY = "M"

        class AllocPositionEffect(Tag):
            Tag = 1047
            Type = "CHAR"
            class Values:
                OPEN = "O"
                CLOSE = "C"
                ROLLED = "R"
                FIFO = "F"

        class DealingCapacity(Tag):
            Tag = 1048
            Type = "CHAR"
            class Values:
                AGENT = "A"
                PRINCIPAL = "P"
                RISKLESS_PRINCIPAL = "R"

        class InstrmtAssignmentMethod(Tag):
            Tag = 1049
            Type = "CHAR"
            class Values:
                PRO_RATA = "P"
                RANDOM = "R"

        class InstrumentPartyIDSource(Tag):
            Tag = 1050
            Type = "CHAR"

        class InstrumentPartyRole(Tag):
            Tag = 1051
            Type = "INT"

        class NoInstrumentPartySubIDs(Tag):
            Tag = 1052
            Type = "NUMINGROUP"

        class InstrumentPartySubID(Tag):
            Tag = 1053
            Type = "STRING"

        class InstrumentPartySubIDType(Tag):
            Tag = 1054
            Type = "INT"

        class PositionCurrency(Tag):
            Tag = 1055
            Type = "STRING"

        class CalculatedCcyLastQty(Tag):
            Tag = 1056
            Type = "QTY"

        class AggressorIndicator(Tag):
            Tag = 1057
            Type = "BOOLEAN"
            class Values:
                YES = 1
                NO = 0

        class NoUndlyInstrumentParties(Tag):
            Tag = 1058
            Type = "NUMINGROUP"

        class UnderlyingInstrumentPartyID(Tag):
            Tag = 1059
            Type = "STRING"

        class UnderlyingInstrumentPartyIDSource(Tag):
            Tag = 1060
            Type = "CHAR"

        class UnderlyingInstrumentPartyRole(Tag):
            Tag = 1061
            Type = "INT"

        class NoUndlyInstrumentPartySubIDs(Tag):
            Tag = 1062
            Type = "NUMINGROUP"

        class UnderlyingInstrumentPartySubID(Tag):
            Tag = 1063
            Type = "STRING"

        class UnderlyingInstrumentPartySubIDType(Tag):
            Tag = 1064
            Type = "INT"

        class BidSwapPoints(Tag):
            Tag = 1065
            Type = "PRICEOFFSET"

        class OfferSwapPoints(Tag):
            Tag = 1066
            Type = "PRICEOFFSET"

        class LegBidForwardPoints(Tag):
            Tag = 1067
            Type = "PRICEOFFSET"

        class LegOfferForwardPoints(Tag):
            Tag = 1068
            Type = "PRICEOFFSET"

        class SwapPoints(Tag):
            Tag = 1069
            Type = "PRICEOFFSET"

        class MDQuoteType(Tag):
            Tag = 1070
            Type = "INT"
            class Values:
                INDICATIVE = 0
                TRADEABLE = 1
                RESTRICTED_TRADEABLE = 2
                COUNTER = 3
                INDICATIVE_AND_TRADEABLE = 4

        class LastSwapPoints(Tag):
            Tag = 1071
            Type = "PRICEOFFSET"

        class SideGrossTradeAmt(Tag):
            Tag = 1072
            Type = "AMT"

        class LegLastForwardPoints(Tag):
            Tag = 1073
            Type = "PRICEOFFSET"

        class LegCalculatedCcyLastQty(Tag):
            Tag = 1074
            Type = "QTY"

        class LegGrossTradeAmt(Tag):
            Tag = 1075
            Type = "AMT"

        class MaturityTime(Tag):
            Tag = 1079
            Type = "TZTIMEONLY"

        class RefOrderID(Tag):
            Tag = 1080
            Type = "STRING"

        class RefOrderIDSource(Tag):
            Tag = 1081
            Type = "CHAR"
            class Values:
                SECONDARYORDERID = "0"
                ORDERID = "1"
                MDENTRYID = "2"
                QUOTEENTRYID = "3"
                ORIGINAL_ORDER_ID = "4"

        class SecondaryDisplayQty(Tag):
            Tag = 1082
            Type = "QTY"

        class DisplayWhen(Tag):
            Tag = 1083
            Type = "CHAR"
            class Values:
                IMMEDIATE = "1"
                EXHAUST = "2"

        class DisplayMethod(Tag):
            Tag = 1084
            Type = "CHAR"
            class Values:
                INITIAL = "1"
                NEW = "2"
                RANDOM = "3"
                UNDISCLOSED = "4"

        class DisplayLowQty(Tag):
            Tag = 1085
            Type = "QTY"

        class DisplayHighQty(Tag):
            Tag = 1086
            Type = "QTY"

        class DisplayMinIncr(Tag):
            Tag = 1087
            Type = "QTY"

        class RefreshQty(Tag):
            Tag = 1088
            Type = "QTY"

        class MatchIncrement(Tag):
            Tag = 1089
            Type = "QTY"

        class MaxPriceLevels(Tag):
            Tag = 1090
            Type = "INT"

        class PreTradeAnonymity(Tag):
            Tag = 1091
            Type = "BOOLEAN"

        class PriceProtectionScope(Tag):
            Tag = 1092
            Type = "CHAR"
            class Values:
                NONE = "0"
                LOCAL = "1"
                NATIONAL = "2"
                GLOBAL = "3"

        class LotType(Tag):
            Tag = 1093
            Type = "CHAR"
            class Values:
                ODD_LOT = "1"
                ROUND_LOT = "2"
                BLOCK_LOT = "3"
                ROUND_LOT_BASED_UPON_UNITOFMEASURE = "4"

        class PegPriceType(Tag):
            Tag = 1094
            Type = "INT"
            class Values:
                LAST_PEG = 1
                MID_PRICE_PEG = 2
                OPENING_PEG = 3
                MARKET_PEG = 4
                PRIMARY_PEG = 5
                PEG_TO_VWAP = 7
                TRAILING_STOP_PEG = 8
                PEG_TO_LIMIT_PRICE = 9

        class PeggedRefPrice(Tag):
            Tag = 1095
            Type = "PRICE"

        class PegSecurityIDSource(Tag):
            Tag = 1096
            Type = "STRING"

        class PegSecurityID(Tag):
            Tag = 1097
            Type = "STRING"

        class PegSymbol(Tag):
            Tag = 1098
            Type = "STRING"

        class PegSecurityDesc(Tag):
            Tag = 1099
            Type = "STRING"

        class TriggerType(Tag):
            Tag = 1100
            Type = "CHAR"
            class Values:
                PARTIAL_EXECUTION = "1"
                SPECIFIED_TRADING_SESSION = "2"
                NEXT_AUCTION = "3"
                PRICE_MOVEMENT = "4"

        class TriggerAction(Tag):
            Tag = 1101
            Type = "CHAR"
            class Values:
                ACTIVATE = "1"
                MODIFY = "2"
                CANCEL = "3"

        class TriggerPrice(Tag):
            Tag = 1102
            Type = "PRICE"

        class TriggerSymbol(Tag):
            Tag = 1103
            Type = "STRING"

        class TriggerSecurityID(Tag):
            Tag = 1104
            Type = "STRING"

        class TriggerSecurityIDSource(Tag):
            Tag = 1105
            Type = "STRING"

        class TriggerSecurityDesc(Tag):
            Tag = 1106
            Type = "STRING"

        class TriggerPriceType(Tag):
            Tag = 1107
            Type = "CHAR"
            class Values:
                BEST_OFFER = "1"
                LAST_TRADE = "2"
                BEST_BID = "3"
                BEST_BID_OR_LAST_TRADE = "4"
                BEST_OFFER_OR_LAST_TRADE = "5"
                BEST_MID = "6"

        class TriggerPriceTypeScope(Tag):
            Tag = 1108
            Type = "CHAR"
            class Values:
                NONE = "0"
                LOCAL = "1"
                NATIONAL = "2"
                GLOBAL = "3"

        class TriggerPriceDirection(Tag):
            Tag = 1109
            Type = "CHAR"
            class Values:
                TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_UP_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE = "U"
                TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_DOWN_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE = "D"

        class TriggerNewPrice(Tag):
            Tag = 1110
            Type = "PRICE"

        class TriggerOrderType(Tag):
            Tag = 1111
            Type = "CHAR"
            class Values:
                MARKET = "1"
                LIMIT = "2"

        class TriggerNewQty(Tag):
            Tag = 1112
            Type = "QTY"

        class TriggerTradingSessionID(Tag):
            Tag = 1113
            Type = "STRING"

        class TriggerTradingSessionSubID(Tag):
            Tag = 1114
            Type = "STRING"

        class OrderCategory(Tag):
            Tag = 1115
            Type = "CHAR"
            class Values:
                ORDER = "1"
                QUOTE = "2"
                PRIVATELY_NEGOTIATED_TRADE = "3"
                MULTILEG_ORDER = "4"
                LINKED_ORDER = "5"
                QUOTE_REQUEST = "6"
                IMPLIED_ORDER = "7"
                CROSS_ORDER = "8"
                STREAMING_PRICE = "9"

        class NoRootPartyIDs(Tag):
            Tag = 1116
            Type = "NUMINGROUP"

        class RootPartyID(Tag):
            Tag = 1117
            Type = "STRING"

        class RootPartyIDSource(Tag):
            Tag = 1118
            Type = "CHAR"

        class RootPartyRole(Tag):
            Tag = 1119
            Type = "INT"

        class NoRootPartySubIDs(Tag):
            Tag = 1120
            Type = "NUMINGROUP"

        class RootPartySubID(Tag):
            Tag = 1121
            Type = "STRING"

        class RootPartySubIDType(Tag):
            Tag = 1122
            Type = "INT"

        class TradeHandlingInstr(Tag):
            Tag = 1123
            Type = "CHAR"
            class Values:
                TRADE_CONFIRMATION = "0"
                TWO_PARTY_REPORT = "1"
                ONE_PARTY_REPORT_FOR_MATCHING = "2"
                ONE_PARTY_REPORT_FOR_PASS_THROUGH = "3"
                AUTOMATED_FLOOR_ORDER_ROUTING = "4"
                TWO_PARTY_REPORT_FOR_CLAIM = "5"

        class OrigTradeHandlingInstr(Tag):
            Tag = 1124
            Type = "CHAR"

        class OrigTradeDate(Tag):
            Tag = 1125
            Type = "LOCALMKTDATE"

        class OrigTradeID(Tag):
            Tag = 1126
            Type = "STRING"

        class OrigSecondaryTradeID(Tag):
            Tag = 1127
            Type = "STRING"

        class ApplVerID(Tag):
            Tag = 1128
            Type = "STRING"
            class Values:
                FIX27 = "0"
                FIX30 = "1"
                FIX40 = "2"
                FIX41 = "3"
                FIX42 = "4"
                FIX43 = "5"
                FIX44 = "6"
                FIX50 = "7"
                FIX50SP1 = "8"
                FIX50SP2 = "9"

        class CstmApplVerID(Tag):
            Tag = 1129
            Type = "STRING"

        class RefApplVerID(Tag):
            Tag = 1130
            Type = "STRING"

        class RefCstmApplVerID(Tag):
            Tag = 1131
            Type = "STRING"

        class TZTransactTime(Tag):
            Tag = 1132
            Type = "TZTIMESTAMP"

        class ExDestinationIDSource(Tag):
            Tag = 1133
            Type = "CHAR"
            class Values:
                BIC = "B"
                GENERALLY_ACCEPTED_MARKET_PARTICIPANT_IDENTIFIER = "C"
                PROPRIETARY = "D"
                ISO_COUNTRY_CODE = "E"
                MIC = "G"

        class ReportedPxDiff(Tag):
            Tag = 1134
            Type = "BOOLEAN"

        class RptSys(Tag):
            Tag = 1135
            Type = "STRING"

        class AllocClearingFeeIndicator(Tag):
            Tag = 1136
            Type = "STRING"

        class DefaultApplVerID(Tag):
            Tag = 1137
            Type = "STRING"

        class DisplayQty(Tag):
            Tag = 1138
            Type = "QTY"

        class ExchangeSpecialInstructions(Tag):
            Tag = 1139
            Type = "STRING"

        class MaxTradeVol(Tag):
            Tag = 1140
            Type = "QTY"

        class NoMDFeedTypes(Tag):
            Tag = 1141
            Type = "NUMINGROUP"

        class MatchAlgorithm(Tag):
            Tag = 1142
            Type = "STRING"

        class MaxPriceVariation(Tag):
            Tag = 1143
            Type = "FLOAT"

        class ImpliedMarketIndicator(Tag):
            Tag = 1144
            Type = "INT"
            class Values:
                NOT_IMPLIED = 0
                IMPLIED_IN = 1
                IMPLIED_OUT = 2
                BOTH_IMPLIED_IN_AND_IMPLIED_OUT = 3

        class EventTime(Tag):
            Tag = 1145
            Type = "UTCTIMESTAMP"

        class MinPriceIncrementAmount(Tag):
            Tag = 1146
            Type = "AMT"

        class UnitOfMeasureQty(Tag):
            Tag = 1147
            Type = "QTY"

        class LowLimitPrice(Tag):
            Tag = 1148
            Type = "PRICE"

        class HighLimitPrice(Tag):
            Tag = 1149
            Type = "PRICE"

        class TradingReferencePrice(Tag):
            Tag = 1150
            Type = "PRICE"

        class SecurityGroup(Tag):
            Tag = 1151
            Type = "STRING"

        class LegNumber(Tag):
            Tag = 1152
            Type = "INT"

        class SettlementCycleNo(Tag):
            Tag = 1153
            Type = "INT"

        class SideCurrency(Tag):
            Tag = 1154
            Type = "CURRENCY"

        class SideSettlCurrency(Tag):
            Tag = 1155
            Type = "CURRENCY"

        class ApplExtID(Tag):
            Tag = 1156
            Type = "INT"

        class CcyAmt(Tag):
            Tag = 1157
            Type = "AMT"

        class NoSettlDetails(Tag):
            Tag = 1158
            Type = "NUMINGROUP"

        class SettlObligMode(Tag):
            Tag = 1159
            Type = "INT"
            class Values:
                PRELIMINARY = 1
                FINAL = 2

        class SettlObligMsgID(Tag):
            Tag = 1160
            Type = "STRING"

        class SettlObligID(Tag):
            Tag = 1161
            Type = "STRING"

        class SettlObligTransType(Tag):
            Tag = 1162
            Type = "CHAR"
            class Values:
                CANCEL = "C"
                NEW = "N"
                REPLACE = "R"
                RESTATE = "T"

        class SettlObligRefID(Tag):
            Tag = 1163
            Type = "STRING"

        class SettlObligSource(Tag):
            Tag = 1164
            Type = "CHAR"
            class Values:
                INSTRUCTIONS_OF_BROKER = "1"
                INSTRUCTIONS_FOR_INSTITUTION = "2"
                INVESTOR = "3"

        class NoSettlOblig(Tag):
            Tag = 1165
            Type = "NUMINGROUP"

        class QuoteMsgID(Tag):
            Tag = 1166
            Type = "STRING"

        class QuoteEntryStatus(Tag):
            Tag = 1167
            Type = "INT"
            class Values:
                ACCEPTED = 0
                REJECTED = 5
                REMOVED_FROM_MARKET = 6
                EXPIRED = 7
                LOCKED_MARKET_WARNING = 12
                CROSS_MARKET_WARNING = 13
                CANCELED_DUE_TO_LOCK_MARKET = 14
                CANCELED_DUE_TO_CROSS_MARKET = 15
                ACTIVE = 16

        class TotNoCxldQuotes(Tag):
            Tag = 1168
            Type = "INT"

        class TotNoAccQuotes(Tag):
            Tag = 1169
            Type = "INT"

        class TotNoRejQuotes(Tag):
            Tag = 1170
            Type = "INT"

        class PrivateQuote(Tag):
            Tag = 1171
            Type = "BOOLEAN"
            class Values:
                YES = 1
                NO = 0

        class RespondentType(Tag):
            Tag = 1172
            Type = "INT"
            class Values:
                ALL_MARKET_PARTICIPANTS = 1
                SPECIFIED_MARKET_PARTICIPANTS = 2
                ALL_MARKET_MAKERS = 3
                PRIMARY_MARKET_MAKER = 4

        class MDSubBookType(Tag):
            Tag = 1173
            Type = "INT"

        class SecurityTradingEvent(Tag):
            Tag = 1174
            Type = "INT"
            class Values:
                ORDER_IMBALANCE_AUCTION_IS_EXTENDED = 1
                TRADING_RESUMES = 2
                PRICE_VOLATILITY_INTERRUPTION = 3
                CHANGE_OF_TRADING_SESSION = 4
                CHANGE_OF_TRADING_SUBSESSION = 5
                CHANGE_OF_SECURITY_TRADING_STATUS = 6
                CHANGE_OF_BOOK_TYPE = 7
                CHANGE_OF_MARKET_DEPTH = 8

        class NoStatsIndicators(Tag):
            Tag = 1175
            Type = "NUMINGROUP"

        class StatsType(Tag):
            Tag = 1176
            Type = "INT"
            class Values:
                EXCHANGE_LAST = 1
                HIGH = 2
                AVERAGE_PRICE = 3
                TURNOVER = 4

        class NoOfSecSizes(Tag):
            Tag = 1177
            Type = "NUMINGROUP"

        class MDSecSizeType(Tag):
            Tag = 1178
            Type = "INT"
            class Values:
                CUSTOMER = 1

        class MDSecSize(Tag):
            Tag = 1179
            Type = "QTY"

        class ApplID(Tag):
            Tag = 1180
            Type = "STRING"

        class ApplSeqNum(Tag):
            Tag = 1181
            Type = "SEQNUM"

        class ApplBegSeqNum(Tag):
            Tag = 1182
            Type = "SEQNUM"

        class ApplEndSeqNum(Tag):
            Tag = 1183
            Type = "SEQNUM"

        class SecurityXMLLen(Tag):
            Tag = 1184
            Type = "LENGTH"

        class SecurityXML(Tag):
            Tag = 1185
            Type = "XMLDATA"

        class SecurityXMLSchema(Tag):
            Tag = 1186
            Type = "STRING"

        class RefreshIndicator(Tag):
            Tag = 1187
            Type = "BOOLEAN"

        class Volatility(Tag):
            Tag = 1188
            Type = "FLOAT"

        class TimeToExpiration(Tag):
            Tag = 1189
            Type = "FLOAT"

        class RiskFreeRate(Tag):
            Tag = 1190
            Type = "FLOAT"

        class PriceUnitOfMeasure(Tag):
            Tag = 1191
            Type = "STRING"

        class PriceUnitOfMeasureQty(Tag):
            Tag = 1192
            Type = "QTY"

        class SettlMethod(Tag):
            Tag = 1193
            Type = "CHAR"
            class Values:
                CASH_SETTLEMENT_REQUIRED = "C"
                PHYSICAL_SETTLEMENT_REQUIRED = "P"

        class ExerciseStyle(Tag):
            Tag = 1194
            Type = "INT"
            class Values:
                EUROPEAN = 0
                AMERICAN = 1
                BERMUDA = 2

        class OptPayoutAmount(Tag):
            Tag = 1195
            Type = "AMT"

        class PriceQuoteMethod(Tag):
            Tag = 1196
            Type = "STRING"
            class Values:
                STANDARD_MONEY_PER_UNIT_OF_A_PHYSICAL = "STD"
                INDEX = "INX"
                INTEREST_RATE_INDEX = "INT"
                PERCENT_OF_PAR = "PCTPAR"

        class ValuationMethod(Tag):
            Tag = 1197
            Type = "STRING"
            class Values:
                PREMIUM_STYLE = "EQTY"
                FUTURES_STYLE_MARK_TO_MARKET = "FUT"
                FUTURES_STYLE_WITH_AN_ATTACHED_CASH_ADJUSTMENT = "FUTDA"
                CDS_STYLE_COLLATERALIZATION_OF_MARKET_TO_MARKET_AND_COUPON = "CDS"
                CDS_IN_DELIVERY = "CDSD"

        class ListMethod(Tag):
            Tag = 1198
            Type = "INT"
            class Values:
                PRE_LISTED_ONLY = 0
                USER_REQUESTED = 1

        class CapPrice(Tag):
            Tag = 1199
            Type = "PRICE"

        class FloorPrice(Tag):
            Tag = 1200
            Type = "PRICE"

        class NoStrikeRules(Tag):
            Tag = 1201
            Type = "NUMINGROUP"

        class StartStrikePxRange(Tag):
            Tag = 1202
            Type = "PRICE"

        class EndStrikePxRange(Tag):
            Tag = 1203
            Type = "PRICE"

        class StrikeIncrement(Tag):
            Tag = 1204
            Type = "FLOAT"

        class NoTickRules(Tag):
            Tag = 1205
            Type = "NUMINGROUP"

        class StartTickPriceRange(Tag):
            Tag = 1206
            Type = "PRICE"

        class EndTickPriceRange(Tag):
            Tag = 1207
            Type = "PRICE"

        class TickIncrement(Tag):
            Tag = 1208
            Type = "PRICE"

        class TickRuleType(Tag):
            Tag = 1209
            Type = "INT"
            class Values:
                REGULAR = 0
                VARIABLE = 1
                FIXED = 2
                TRADED_AS_A_SPREAD_LEG = 3
                SETTLED_AS_A_SPREAD_LEG = 4

        class NestedInstrAttribType(Tag):
            Tag = 1210
            Type = "INT"

        class NestedInstrAttribValue(Tag):
            Tag = 1211
            Type = "STRING"

        class LegMaturityTime(Tag):
            Tag = 1212
            Type = "TZTIMEONLY"

        class UnderlyingMaturityTime(Tag):
            Tag = 1213
            Type = "TZTIMEONLY"

        class DerivativeSymbol(Tag):
            Tag = 1214
            Type = "STRING"

        class DerivativeSymbolSfx(Tag):
            Tag = 1215
            Type = "STRING"

        class DerivativeSecurityID(Tag):
            Tag = 1216
            Type = "STRING"

        class DerivativeSecurityIDSource(Tag):
            Tag = 1217
            Type = "STRING"

        class NoDerivativeSecurityAltID(Tag):
            Tag = 1218
            Type = "NUMINGROUP"

        class DerivativeSecurityAltID(Tag):
            Tag = 1219
            Type = "STRING"

        class DerivativeSecurityAltIDSource(Tag):
            Tag = 1220
            Type = "STRING"

        class SecondaryLowLimitPrice(Tag):
            Tag = 1221
            Type = "PRICE"

        class MaturityRuleID(Tag):
            Tag = 1222
            Type = "STRING"

        class StrikeRuleID(Tag):
            Tag = 1223
            Type = "STRING"

        class LegUnitOfMeasureQty(Tag):
            Tag = 1224
            Type = "QTY"

        class DerivativeOptPayAmount(Tag):
            Tag = 1225
            Type = "AMT"

        class EndMaturityMonthYear(Tag):
            Tag = 1226
            Type = "MONTHYEAR"

        class ProductComplex(Tag):
            Tag = 1227
            Type = "STRING"

        class DerivativeProductComplex(Tag):
            Tag = 1228
            Type = "STRING"

        class MaturityMonthYearIncrement(Tag):
            Tag = 1229
            Type = "INT"

        class SecondaryHighLimitPrice(Tag):
            Tag = 1230
            Type = "PRICE"

        class MinLotSize(Tag):
            Tag = 1231
            Type = "QTY"

        class NoExecInstRules(Tag):
            Tag = 1232
            Type = "NUMINGROUP"

        class NoLotTypeRules(Tag):
            Tag = 1234
            Type = "NUMINGROUP"

        class NoMatchRules(Tag):
            Tag = 1235
            Type = "NUMINGROUP"

        class NoMaturityRules(Tag):
            Tag = 1236
            Type = "NUMINGROUP"

        class NoOrdTypeRules(Tag):
            Tag = 1237
            Type = "NUMINGROUP"

        class NoTimeInForceRules(Tag):
            Tag = 1239
            Type = "NUMINGROUP"

        class SecondaryTradingReferencePrice(Tag):
            Tag = 1240
            Type = "PRICE"

        class StartMaturityMonthYear(Tag):
            Tag = 1241
            Type = "MONTHYEAR"

        class FlexProductEligibilityIndicator(Tag):
            Tag = 1242
            Type = "BOOLEAN"

        class DerivFlexProductEligibilityIndicator(Tag):
            Tag = 1243
            Type = "BOOLEAN"

        class FlexibleIndicator(Tag):
            Tag = 1244
            Type = "BOOLEAN"

        class TradingCurrency(Tag):
            Tag = 1245
            Type = "CURRENCY"

        class DerivativeProduct(Tag):
            Tag = 1246
            Type = "INT"

        class DerivativeSecurityGroup(Tag):
            Tag = 1247
            Type = "STRING"

        class DerivativeCFICode(Tag):
            Tag = 1248
            Type = "STRING"

        class DerivativeSecurityType(Tag):
            Tag = 1249
            Type = "STRING"

        class DerivativeSecuritySubType(Tag):
            Tag = 1250
            Type = "STRING"

        class DerivativeMaturityMonthYear(Tag):
            Tag = 1251
            Type = "MONTHYEAR"

        class DerivativeMaturityDate(Tag):
            Tag = 1252
            Type = "LOCALMKTDATE"

        class DerivativeMaturityTime(Tag):
            Tag = 1253
            Type = "TZTIMEONLY"

        class DerivativeSettleOnOpenFlag(Tag):
            Tag = 1254
            Type = "STRING"

        class DerivativeInstrmtAssignmentMethod(Tag):
            Tag = 1255
            Type = "CHAR"

        class DerivativeSecurityStatus(Tag):
            Tag = 1256
            Type = "STRING"

        class DerivativeInstrRegistry(Tag):
            Tag = 1257
            Type = "STRING"

        class DerivativeCountryOfIssue(Tag):
            Tag = 1258
            Type = "COUNTRY"

        class DerivativeStateOrProvinceOfIssue(Tag):
            Tag = 1259
            Type = "STRING"

        class DerivativeLocaleOfIssue(Tag):
            Tag = 1260
            Type = "STRING"

        class DerivativeStrikePrice(Tag):
            Tag = 1261
            Type = "PRICE"

        class DerivativeStrikeCurrency(Tag):
            Tag = 1262
            Type = "CURRENCY"

        class DerivativeStrikeMultiplier(Tag):
            Tag = 1263
            Type = "FLOAT"

        class DerivativeStrikeValue(Tag):
            Tag = 1264
            Type = "FLOAT"

        class DerivativeOptAttribute(Tag):
            Tag = 1265
            Type = "CHAR"

        class DerivativeContractMultiplier(Tag):
            Tag = 1266
            Type = "FLOAT"

        class DerivativeMinPriceIncrement(Tag):
            Tag = 1267
            Type = "FLOAT"

        class DerivativeMinPriceIncrementAmount(Tag):
            Tag = 1268
            Type = "AMT"

        class DerivativeUnitOfMeasure(Tag):
            Tag = 1269
            Type = "STRING"

        class DerivativeUnitOfMeasureQty(Tag):
            Tag = 1270
            Type = "QTY"

        class DerivativeTimeUnit(Tag):
            Tag = 1271
            Type = "STRING"

        class DerivativeSecurityExchange(Tag):
            Tag = 1272
            Type = "EXCHANGE"

        class DerivativePositionLimit(Tag):
            Tag = 1273
            Type = "INT"

        class DerivativeNTPositionLimit(Tag):
            Tag = 1274
            Type = "INT"

        class DerivativeIssuer(Tag):
            Tag = 1275
            Type = "STRING"

        class DerivativeIssueDate(Tag):
            Tag = 1276
            Type = "LOCALMKTDATE"

        class DerivativeEncodedIssuerLen(Tag):
            Tag = 1277
            Type = "LENGTH"

        class DerivativeEncodedIssuer(Tag):
            Tag = 1278
            Type = "DATA"

        class DerivativeSecurityDesc(Tag):
            Tag = 1279
            Type = "STRING"

        class DerivativeEncodedSecurityDescLen(Tag):
            Tag = 1280
            Type = "LENGTH"

        class DerivativeEncodedSecurityDesc(Tag):
            Tag = 1281
            Type = "DATA"

        class DerivativeSecurityXMLLen(Tag):
            Tag = 1282
            Type = "LENGTH"

        class DerivativeSecurityXML(Tag):
            Tag = 1283
            Type = "DATA"

        class DerivativeSecurityXMLSchema(Tag):
            Tag = 1284
            Type = "STRING"

        class DerivativeContractSettlMonth(Tag):
            Tag = 1285
            Type = "MONTHYEAR"

        class NoDerivativeEvents(Tag):
            Tag = 1286
            Type = "NUMINGROUP"

        class DerivativeEventType(Tag):
            Tag = 1287
            Type = "INT"

        class DerivativeEventDate(Tag):
            Tag = 1288
            Type = "LOCALMKTDATE"

        class DerivativeEventTime(Tag):
            Tag = 1289
            Type = "UTCTIMESTAMP"

        class DerivativeEventPx(Tag):
            Tag = 1290
            Type = "PRICE"

        class DerivativeEventText(Tag):
            Tag = 1291
            Type = "STRING"

        class NoDerivativeInstrumentParties(Tag):
            Tag = 1292
            Type = "NUMINGROUP"

        class DerivativeInstrumentPartyID(Tag):
            Tag = 1293
            Type = "STRING"

        class DerivativeInstrumentPartyIDSource(Tag):
            Tag = 1294
            Type = "STRING"

        class DerivativeInstrumentPartyRole(Tag):
            Tag = 1295
            Type = "INT"

        class NoDerivativeInstrumentPartySubIDs(Tag):
            Tag = 1296
            Type = "NUMINGROUP"

        class DerivativeInstrumentPartySubID(Tag):
            Tag = 1297
            Type = "STRING"

        class DerivativeInstrumentPartySubIDType(Tag):
            Tag = 1298
            Type = "INT"

        class DerivativeExerciseStyle(Tag):
            Tag = 1299
            Type = "CHAR"

        class MarketSegmentID(Tag):
            Tag = 1300
            Type = "STRING"

        class MarketID(Tag):
            Tag = 1301
            Type = "EXCHANGE"

        class MaturityMonthYearIncrementUnits(Tag):
            Tag = 1302
            Type = "INT"
            class Values:
                MONTHS = 0
                DAYS = 1
                WEEKS = 2
                YEARS = 3

        class MaturityMonthYearFormat(Tag):
            Tag = 1303
            Type = "INT"
            class Values:
                YEARMONTH_ONLY = 0
                YEARMONTHDAY = 1
                YEARMONTHWEEK = 2

        class StrikeExerciseStyle(Tag):
            Tag = 1304
            Type = "INT"

        class SecondaryPriceLimitType(Tag):
            Tag = 1305
            Type = "INT"

        class PriceLimitType(Tag):
            Tag = 1306
            Type = "INT"
            class Values:
                PRICE = 0
                TICKS = 1
                PERCENTAGE = 2

        class ExecInstValue(Tag):
            Tag = 1308
            Type = "CHAR"

        class NoTradingSessionRules(Tag):
            Tag = 1309
            Type = "NUMINGROUP"

        class NoMarketSegments(Tag):
            Tag = 1310
            Type = "NUMINGROUP"

        class NoDerivativeInstrAttrib(Tag):
            Tag = 1311
            Type = "NUMINGROUP"

        class NoNestedInstrAttrib(Tag):
            Tag = 1312
            Type = "NUMINGROUP"

        class DerivativeInstrAttribType(Tag):
            Tag = 1313
            Type = "INT"

        class DerivativeInstrAttribValue(Tag):
            Tag = 1314
            Type = "STRING"

        class DerivativePriceUnitOfMeasure(Tag):
            Tag = 1315
            Type = "STRING"

        class DerivativePriceUnitOfMeasureQty(Tag):
            Tag = 1316
            Type = "QTY"

        class DerivativeSettlMethod(Tag):
            Tag = 1317
            Type = "CHAR"

        class DerivativePriceQuoteMethod(Tag):
            Tag = 1318
            Type = "STRING"

        class DerivativeValuationMethod(Tag):
            Tag = 1319
            Type = "STRING"

        class DerivativeListMethod(Tag):
            Tag = 1320
            Type = "INT"

        class DerivativeCapPrice(Tag):
            Tag = 1321
            Type = "PRICE"

        class DerivativeFloorPrice(Tag):
            Tag = 1322
            Type = "PRICE"

        class DerivativePutOrCall(Tag):
            Tag = 1323
            Type = "INT"

        class ListUpdateAction(Tag):
            Tag = 1324
            Type = "CHAR"

        class ParentMktSegmID(Tag):
            Tag = 1325
            Type = "STRING"

        class TradingSessionDesc(Tag):
            Tag = 1326
            Type = "STRING"

        class TradSesUpdateAction(Tag):
            Tag = 1327
            Type = "CHAR"

        class RejectText(Tag):
            Tag = 1328
            Type = "STRING"

        class FeeMultiplier(Tag):
            Tag = 1329
            Type = "FLOAT"

        class UnderlyingLegSymbol(Tag):
            Tag = 1330
            Type = "STRING"

        class UnderlyingLegSymbolSfx(Tag):
            Tag = 1331
            Type = "STRING"

        class UnderlyingLegSecurityID(Tag):
            Tag = 1332
            Type = "STRING"

        class UnderlyingLegSecurityIDSource(Tag):
            Tag = 1333
            Type = "STRING"

        class NoUnderlyingLegSecurityAltID(Tag):
            Tag = 1334
            Type = "NUMINGROUP"

        class UnderlyingLegSecurityAltID(Tag):
            Tag = 1335
            Type = "STRING"

        class UnderlyingLegSecurityAltIDSource(Tag):
            Tag = 1336
            Type = "STRING"

        class UnderlyingLegSecurityType(Tag):
            Tag = 1337
            Type = "STRING"

        class UnderlyingLegSecuritySubType(Tag):
            Tag = 1338
            Type = "STRING"

        class UnderlyingLegMaturityMonthYear(Tag):
            Tag = 1339
            Type = "MONTHYEAR"

        class UnderlyingLegStrikePrice(Tag):
            Tag = 1340
            Type = "PRICE"

        class UnderlyingLegSecurityExchange(Tag):
            Tag = 1341
            Type = "STRING"

        class NoOfLegUnderlyings(Tag):
            Tag = 1342
            Type = "NUMINGROUP"

        class UnderlyingLegPutOrCall(Tag):
            Tag = 1343
            Type = "INT"

        class UnderlyingLegCFICode(Tag):
            Tag = 1344
            Type = "STRING"

        class UnderlyingLegMaturityDate(Tag):
            Tag = 1345
            Type = "LOCALMKTDATE"

        class ApplReqID(Tag):
            Tag = 1346
            Type = "STRING"

        class ApplReqType(Tag):
            Tag = 1347
            Type = "INT"
            class Values:
                RETRANSMISSION_OF_APPLICATION_MESSAGES_FOR_THE_SPECIFIED_APPLICATIONS = 0
                SUBSCRIPTION_TO_THE_SPECIFIED_APPLICATIONS = 1
                REQUEST_FOR_THE_LAST_APPLLASTSEQNUM_PUBLISHED_FOR_THE_SPECIFIED_APPLICATIONS = 2
                REQUEST_VALID_SET_OF_APPLICATIONS = 3
                UNSUBSCRIBE_TO_THE_SPECIFIED_APPLICATIONS = 4
                CANCEL_RETRANSMISSION = 5
                CANCEL_RETRANSMISSION_AND_UNSUBSCRIBE_TO_THE_SPECIFIED_APPLICATIONS = 6

        class ApplResponseType(Tag):
            Tag = 1348
            Type = "INT"
            class Values:
                REQUEST_SUCCESSFULLY_PROCESSED = 0
                APPLICATION_DOES_NOT_EXIST = 1
                MESSAGES_NOT_AVAILABLE = 2

        class ApplTotalMessageCount(Tag):
            Tag = 1349
            Type = "INT"

        class ApplLastSeqNum(Tag):
            Tag = 1350
            Type = "SEQNUM"

        class NoApplIDs(Tag):
            Tag = 1351
            Type = "NUMINGROUP"

        class ApplResendFlag(Tag):
            Tag = 1352
            Type = "BOOLEAN"

        class ApplResponseID(Tag):
            Tag = 1353
            Type = "STRING"

        class ApplResponseError(Tag):
            Tag = 1354
            Type = "INT"
            class Values:
                APPLICATION_DOES_NOT_EXIST = 0
                MESSAGES_REQUESTED_ARE_NOT_AVAILABLE = 1
                USER_NOT_AUTHORIZED_FOR_APPLICATION = 2

        class RefApplID(Tag):
            Tag = 1355
            Type = "STRING"

        class ApplReportID(Tag):
            Tag = 1356
            Type = "STRING"

        class RefApplLastSeqNum(Tag):
            Tag = 1357
            Type = "SEQNUM"

        class LegPutOrCall(Tag):
            Tag = 1358
            Type = "INT"

        class TotNoFills(Tag):
            Tag = 1361
            Type = "INT"

        class NoFills(Tag):
            Tag = 1362
            Type = "NUMINGROUP"

        class FillExecID(Tag):
            Tag = 1363
            Type = "STRING"

        class FillPx(Tag):
            Tag = 1364
            Type = "PRICE"

        class FillQty(Tag):
            Tag = 1365
            Type = "QTY"

        class LegAllocID(Tag):
            Tag = 1366
            Type = "STRING"

        class LegAllocSettlCurrency(Tag):
            Tag = 1367
            Type = "CURRENCY"

        class TradSesEvent(Tag):
            Tag = 1368
            Type = "INT"
            class Values:
                TRADING_RESUMES = 0
                CHANGE_OF_TRADING_SESSION = 1
                CHANGE_OF_TRADING_SUBSESSION = 2
                CHANGE_OF_TRADING_STATUS = 3

        class MassActionReportID(Tag):
            Tag = 1369
            Type = "STRING"

        class NoNotAffectedOrders(Tag):
            Tag = 1370
            Type = "NUMINGROUP"

        class NotAffectedOrderID(Tag):
            Tag = 1371
            Type = "STRING"

        class NotAffOrigClOrdID(Tag):
            Tag = 1372
            Type = "STRING"

        class MassActionType(Tag):
            Tag = 1373
            Type = "INT"
            class Values:
                SUSPEND_ORDERS = 1
                RELEASE_ORDERS_FROM_SUSPENSION = 2
                CANCEL_ORDERS = 3

        class MassActionScope(Tag):
            Tag = 1374
            Type = "INT"
            class Values:
                ALL_ORDERS_FOR_A_SECURITY = 1
                ALL_ORDERS_FOR_AN_UNDERLYING_SECURITY = 2
                ALL_ORDERS_FOR_A_PRODUCT = 3
                ALL_ORDERS_FOR_A_CFICODE = 4
                ALL_ORDERS_FOR_A_SECURITYTYPE = 5
                ALL_ORDERS_FOR_A_TRADING_SESSION = 6
                ALL_ORDERS = 7
                ALL_ORDERS_FOR_A_MARKET = 8
                ALL_ORDERS_FOR_A_MARKET_SEGMENT = 9
                ALL_ORDERS_FOR_A_SECURITY_GROUP = 10
                CANCEL_FOR_SECURITY_ISSUER = 11
                CANCEL_FOR_ISSUER_OF_UNDERLYING_SECURITY = 12

        class MassActionResponse(Tag):
            Tag = 1375
            Type = "INT"
            class Values:
                REJECTED = 0
                ACCEPTED = 1

        class MassActionRejectReason(Tag):
            Tag = 1376
            Type = "INT"
            class Values:
                MASS_ACTION_NOT_SUPPORTED = 0
                INVALID_OR_UNKNOWN_SECURITY = 1
                INVALID_OR_UNKNOWN_UNDERLYING_SECURITY = 2
                INVALID_OR_UNKNOWN_PRODUCT = 3
                INVALID_OR_UNKNOWN_CFICODE = 4
                INVALID_OR_UNKNOWN_SECURITYTYPE = 5
                INVALID_OR_UNKNOWN_TRADING_SESSION = 6
                INVALID_OR_UNKNOWN_MARKET = 7
                INVALID_OR_UNKNOWN_MARKET_SEGMENT = 8
                INVALID_OR_UNKNOWN_SECURITY_GROUP = 9
                OTHER = 99
                INVALID_OR_UNKNOWN_SECURITY_ISSUER = 10
                INVALID_OR_UNKNOWN_ISSUER_OF_UNDERLYING_SECURITY = 11

        class MultilegModel(Tag):
            Tag = 1377
            Type = "INT"
            class Values:
                PREDEFINED_MULTILEG_SECURITY = 0
                USER_DEFINED_MULTLEG_SECURITY = 1
                USER_DEFINED_NON_SECURITIZED_MULTILEG = 2

        class MultilegPriceMethod(Tag):
            Tag = 1378
            Type = "INT"
            class Values:
                NET_PRICE = 0
                REVERSED_NET_PRICE = 1
                YIELD_DIFFERENCE = 2
                INDIVIDUAL = 3
                CONTRACT_WEIGHTED_AVERAGE_PRICE = 4
                MULTIPLIED_PRICE = 5

        class LegVolatility(Tag):
            Tag = 1379
            Type = "FLOAT"

        class DividendYield(Tag):
            Tag = 1380
            Type = "PERCENTAGE"

        class LegDividendYield(Tag):
            Tag = 1381
            Type = "PERCENTAGE"

        class CurrencyRatio(Tag):
            Tag = 1382
            Type = "FLOAT"

        class LegCurrencyRatio(Tag):
            Tag = 1383
            Type = "FLOAT"

        class LegExecInst(Tag):
            Tag = 1384
            Type = "MULTIPLECHARVALUE"

        class ContingencyType(Tag):
            Tag = 1385
            Type = "INT"
            class Values:
                ONE_CANCELS_THE_OTHER = 1
                ONE_TRIGGERS_THE_OTHER = 2
                ONE_UPDATES_THE_OTHER_3 = 3
                ONE_UPDATES_THE_OTHER_4 = 4

        class ListRejectReason(Tag):
            Tag = 1386
            Type = "INT"
            class Values:
                BROKER = 0
                EXCHANGE_CLOSED = 2
                TOO_LATE_TO_ENTER = 4
                UNKNOWN_ORDER = 5
                DUPLICATE_ORDER = 6
                UNSUPPORTED_ORDER_CHARACTERISTIC = 11
                OTHER = 99

        class NoTrdRepIndicators(Tag):
            Tag = 1387
            Type = "NUMINGROUP"

        class TrdRepPartyRole(Tag):
            Tag = 1388
            Type = "INT"

        class TrdRepIndicator(Tag):
            Tag = 1389
            Type = "BOOLEAN"

        class TradePublishIndicator(Tag):
            Tag = 1390
            Type = "INT"
            class Values:
                DO_NOT_PUBLISH_TRADE = 0
                PUBLISH_TRADE = 1
                DEFERRED_PUBLICATION = 2

        class UnderlyingLegOptAttribute(Tag):
            Tag = 1391
            Type = "CHAR"

        class UnderlyingLegSecurityDesc(Tag):
            Tag = 1392
            Type = "STRING"

        class MarketReqID(Tag):
            Tag = 1393
            Type = "STRING"

        class MarketReportID(Tag):
            Tag = 1394
            Type = "STRING"

        class MarketUpdateAction(Tag):
            Tag = 1395
            Type = "CHAR"
            class Values:
                ADD = "A"
                DELETE = "D"
                MODIFY = "M"

        class MarketSegmentDesc(Tag):
            Tag = 1396
            Type = "STRING"

        class EncodedMktSegmDescLen(Tag):
            Tag = 1397
            Type = "LENGTH"

        class EncodedMktSegmDesc(Tag):
            Tag = 1398
            Type = "DATA"

        class ApplNewSeqNum(Tag):
            Tag = 1399
            Type = "SEQNUM"

        class EncryptedPasswordMethod(Tag):
            Tag = 1400
            Type = "INT"

        class EncryptedPasswordLen(Tag):
            Tag = 1401
            Type = "LENGTH"

        class EncryptedPassword(Tag):
            Tag = 1402
            Type = "DATA"

        class EncryptedNewPasswordLen(Tag):
            Tag = 1403
            Type = "LENGTH"

        class EncryptedNewPassword(Tag):
            Tag = 1404
            Type = "DATA"

        class UnderlyingLegMaturityTime(Tag):
            Tag = 1405
            Type = "TZTIMEONLY"

        class RefApplExtID(Tag):
            Tag = 1406
            Type = "INT"

        class DefaultApplExtID(Tag):
            Tag = 1407
            Type = "INT"

        class DefaultCstmApplVerID(Tag):
            Tag = 1408
            Type = "STRING"

        class SessionStatus(Tag):
            Tag = 1409
            Type = "INT"
            class Values:
                SESSION_ACTIVE = 0
                SESSION_PASSWORD_CHANGED = 1
                SESSION_PASSWORD_DUE_TO_EXPIRE = 2
                NEW_SESSION_PASSWORD_DOES_NOT_COMPLY_WITH_POLICY = 3
                SESSION_LOGOUT_COMPLETE = 4
                INVALID_USERNAME_OR_PASSWORD = 5
                ACCOUNT_LOCKED = 6
                LOGONS_ARE_NOT_ALLOWED_AT_THIS_TIME = 7
                PASSWORD_EXPIRED = 8

        class DefaultVerIndicator(Tag):
            Tag = 1410
            Type = "BOOLEAN"

        class Nested4PartySubIDType(Tag):
            Tag = 1411
            Type = "INT"

        class Nested4PartySubID(Tag):
            Tag = 1412
            Type = "STRING"

        class NoNested4PartySubIDs(Tag):
            Tag = 1413
            Type = "NUMINGROUP"

        class NoNested4PartyIDs(Tag):
            Tag = 1414
            Type = "NUMINGROUP"

        class Nested4PartyID(Tag):
            Tag = 1415
            Type = "STRING"

        class Nested4PartyIDSource(Tag):
            Tag = 1416
            Type = "CHAR"

        class Nested4PartyRole(Tag):
            Tag = 1417
            Type = "INT"

        class LegLastQty(Tag):
            Tag = 1418
            Type = "QTY"

        class UnderlyingExerciseStyle(Tag):
            Tag = 1419
            Type = "INT"

        class LegExerciseStyle(Tag):
            Tag = 1420
            Type = "INT"

        class LegPriceUnitOfMeasure(Tag):
            Tag = 1421
            Type = "STRING"

        class LegPriceUnitOfMeasureQty(Tag):
            Tag = 1422
            Type = "QTY"

        class UnderlyingUnitOfMeasureQty(Tag):
            Tag = 1423
            Type = "QTY"

        class UnderlyingPriceUnitOfMeasure(Tag):
            Tag = 1424
            Type = "STRING"

        class UnderlyingPriceUnitOfMeasureQty(Tag):
            Tag = 1425
            Type = "QTY"

        class ApplReportType(Tag):
            Tag = 1426
            Type = "INT"
            class Values:
                RESET_APPLSEQNUM_TO_NEW_VALUE_SPECIFIED_IN_APPLNEWSEQNUM = 0
                REPORTS_THAT_THE_LAST_MESSAGE_HAS_BEEN_SENT_FOR_THE_APPLIDS_REFER_TO_REFAPPLLASTSEQNUM = 1
                HEARTBEAT_MESSAGE_INDICATING_THAT_APPLICATION_IDENTIFIED_BY_REFAPPLID = 2
                APPLICATION_MESSAGE_RE_SEND_COMPLETED = 3

        class SideExecID(Tag):
            Tag = 1427
            Type = "STRING"

        class OrderDelay(Tag):
            Tag = 1428
            Type = "INT"

        class OrderDelayUnit(Tag):
            Tag = 1429
            Type = "INT"
            class Values:
                SECONDS = 0
                TENTHS_OF_A_SECOND = 1
                HUNDREDTHS_OF_A_SECOND = 2
                MILLISECONDS = 3
                MICROSECONDS = 4
                NANOSECONDS = 5
                MINUTES = 10
                HOURS = 11
                DAYS = 12
                WEEKS = 13
                MONTHS = 14
                YEARS = 15

        class VenueType(Tag):
            Tag = 1430
            Type = "CHAR"
            class Values:
                ELECTRONIC = "E"
                PIT = "P"
                EX_PIT = "X"

        class RefOrdIDReason(Tag):
            Tag = 1431
            Type = "INT"
            class Values:
                GTC_FROM_PREVIOUS_DAY = 0
                PARTIAL_FILL_REMAINING = 1
                ORDER_CHANGED = 2

        class OrigCustOrderCapacity(Tag):
            Tag = 1432
            Type = "INT"
            class Values:
                MEMBER_TRADING_FOR_THEIR_OWN_ACCOUNT = 1
                CLEARING_FIRM_TRADING_FOR_ITS_PROPRIETARY_ACCOUNT = 2
                MEMBER_TRADING_FOR_ANOTHER_MEMBER = 3
                ALL_OTHER = 4

        class RefApplReqID(Tag):
            Tag = 1433
            Type = "STRING"

        class ModelType(Tag):
            Tag = 1434
            Type = "INT"
            class Values:
                UTILITY_PROVIDED_STANDARD_MODEL = 0
                PROPRIETARY = 1

        class ContractMultiplierUnit(Tag):
            Tag = 1435
            Type = "INT"
            class Values:
                SHARES = 0
                HOURS = 1
                DAYS = 2

        class LegContractMultiplierUnit(Tag):
            Tag = 1436
            Type = "INT"

        class UnderlyingContractMultiplierUnit(Tag):
            Tag = 1437
            Type = "INT"

        class DerivativeContractMultiplierUnit(Tag):
            Tag = 1438
            Type = "INT"

        class FlowScheduleType(Tag):
            Tag = 1439
            Type = "INT"
            class Values:
                NERC_EASTERN_OFF_PEAK = 0
                NERC_WESTERN_OFF_PEAK = 1
                NERC_CALENDAR_ALL_DAYS_IN_MONTH = 2
                NERC_EASTERN_PEAK = 3
                NERC_WESTERN_PEAK = 4

        class LegFlowScheduleType(Tag):
            Tag = 1440
            Type = "INT"

        class UnderlyingFlowScheduleType(Tag):
            Tag = 1441
            Type = "INT"

        class DerivativeFlowScheduleType(Tag):
            Tag = 1442
            Type = "INT"

        class FillLiquidityInd(Tag):
            Tag = 1443
            Type = "INT"

        class SideLiquidityInd(Tag):
            Tag = 1444
            Type = "INT"

        class NoRateSources(Tag):
            Tag = 1445
            Type = "NUMINGROUP"

        class RateSource(Tag):
            Tag = 1446
            Type = "INT"
            class Values:
                BLOOMBERG = 0
                REUTERS = 1
                TELERATE = 2
                OTHER = 99

        class RateSourceType(Tag):
            Tag = 1447
            Type = "INT"
            class Values:
                PRIMARY = 0
                SECONDARY = 1

        class ReferencePage(Tag):
            Tag = 1448
            Type = "STRING"

        class RestructuringType(Tag):
            Tag = 1449
            Type = "STRING"
            class Values:
                FULL_RESTRUCTURING = "FR"
                MODIFIED_RESTRUCTURING = "MR"
                MODIFIED_MOD_RESTRUCTURING = "MM"
                NO_RESTRUCTURING_SPECIFIED = "XR"

        class Seniority(Tag):
            Tag = 1450
            Type = "STRING"
            class Values:
                SENIOR_SECURED = "SD"
                SENIOR = "SR"
                SUBORDINATED = "SB"

        class NotionalPercentageOutstanding(Tag):
            Tag = 1451
            Type = "PERCENTAGE"

        class OriginalNotionalPercentageOutstanding(Tag):
            Tag = 1452
            Type = "PERCENTAGE"

        class UnderlyingRestructuringType(Tag):
            Tag = 1453
            Type = "STRING"

        class UnderlyingSeniority(Tag):
            Tag = 1454
            Type = "STRING"

        class UnderlyingNotionalPercentageOutstanding(Tag):
            Tag = 1455
            Type = "PERCENTAGE"

        class UnderlyingOriginalNotionalPercentageOutstanding(Tag):
            Tag = 1456
            Type = "PERCENTAGE"

        class AttachmentPoint(Tag):
            Tag = 1457
            Type = "PERCENTAGE"

        class DetachmentPoint(Tag):
            Tag = 1458
            Type = "PERCENTAGE"

        class UnderlyingAttachmentPoint(Tag):
            Tag = 1459
            Type = "PERCENTAGE"

        class UnderlyingDetachmentPoint(Tag):
            Tag = 1460
            Type = "PERCENTAGE"

        class NoTargetPartyIDs(Tag):
            Tag = 1461
            Type = "NUMINGROUP"

        class TargetPartyID(Tag):
            Tag = 1462
            Type = "STRING"

        class TargetPartyIDSource(Tag):
            Tag = 1463
            Type = "CHAR"

        class TargetPartyRole(Tag):
            Tag = 1464
            Type = "INT"

        class SecurityListID(Tag):
            Tag = 1465
            Type = "STRING"

        class SecurityListRefID(Tag):
            Tag = 1466
            Type = "STRING"

        class SecurityListDesc(Tag):
            Tag = 1467
            Type = "STRING"

        class EncodedSecurityListDescLen(Tag):
            Tag = 1468
            Type = "LENGTH"

        class EncodedSecurityListDesc(Tag):
            Tag = 1469
            Type = "DATA"

        class SecurityListType(Tag):
            Tag = 1470
            Type = "INT"
            class Values:
                INDUSTRY_CLASSIFICATION = 1
                TRADING_LIST = 2
                MARKET = 3
                NEWSPAPER_LIST = 4

        class SecurityListTypeSource(Tag):
            Tag = 1471
            Type = "INT"
            class Values:
                ICB = 1
                NAICS = 2
                GICS = 3

        class NewsID(Tag):
            Tag = 1472
            Type = "STRING"

        class NewsCategory(Tag):
            Tag = 1473
            Type = "INT"
            class Values:
                COMPANY_NEWS = 0
                MARKETPLACE_NEWS = 1
                FINANCIAL_MARKET_NEWS = 2
                TECHNICAL_NEWS = 3
                OTHER_NEWS = 99

        class LanguageCode(Tag):
            Tag = 1474
            Type = "LANGUAGE"

        class NoNewsRefIDs(Tag):
            Tag = 1475
            Type = "NUMINGROUP"

        class NewsRefID(Tag):
            Tag = 1476
            Type = "STRING"

        class NewsRefType(Tag):
            Tag = 1477
            Type = "INT"
            class Values:
                REPLACEMENT = 0
                OTHER_LANGUAGE = 1
                COMPLIMENTARY = 2

        class StrikePriceDeterminationMethod(Tag):
            Tag = 1478
            Type = "INT"
            class Values:
                FIXED_STRIKE = 1
                STRIKE_SET_AT_EXPIRATION_TO_UNDERLYING_OR_OTHER_VALUE = 2
                STRIKE_SET_TO_AVERAGE_OF_UNDERLYING_SETTLEMENT_PRICE_ACROSS_THE_LIFE_OF_THE_OPTION = 3
                STRIKE_SET_TO_OPTIMAL_VALUE = 4

        class StrikePriceBoundaryMethod(Tag):
            Tag = 1479
            Type = "INT"
            class Values:
                LESS_THAN_UNDERLYING_PRICE_IS_IN_THE_MONEY = 1
                LESS_THAN_OR_EQUAL_TO_THE_UNDERLYING_PRICE_IS_IN_THE_MONEY = 2
                EQUAL_TO_THE_UNDERLYING_PRICE_IS_IN_THE_MONEY = 3
                GREATER_THAN_OR_EQUAL_TO_UNDERLYING_PRICE_IS_IN_THE_MONEY = 4
                GREATER_THAN_UNDERLYING_IS_IN_THE_MONEY = 5

        class StrikePriceBoundaryPrecision(Tag):
            Tag = 1480
            Type = "PERCENTAGE"

        class UnderlyingPriceDeterminationMethod(Tag):
            Tag = 1481
            Type = "INT"
            class Values:
                REGULAR = 1
                SPECIAL_REFERENCE = 2
                OPTIMAL_VALUE = 3
                AVERAGE_VALUE = 4

        class OptPayoutType(Tag):
            Tag = 1482
            Type = "INT"
            class Values:
                VANILLA = 1
                CAPPED = 2
                BINARY = 3

        class NoComplexEvents(Tag):
            Tag = 1483
            Type = "NUMINGROUP"

        class ComplexEventType(Tag):
            Tag = 1484
            Type = "INT"
            class Values:
                CAPPED = 1
                TRIGGER = 2
                KNOCK_IN_UP = 3
                KOCK_IN_DOWN = 4
                KNOCK_OUT_UP = 5
                KNOCK_OUT_DOWN = 6
                UNDERLYING = 7
                RESET_BARRIER = 8
                ROLLING_BARRIER = 9

        class ComplexOptPayoutAmount(Tag):
            Tag = 1485
            Type = "AMT"

        class ComplexEventPrice(Tag):
            Tag = 1486
            Type = "PRICE"

        class ComplexEventPriceBoundaryMethod(Tag):
            Tag = 1487
            Type = "INT"
            class Values:
                LESS_THAN_COMPLEXEVENTPRICE = 1
                LESS_THAN_OR_EQUAL_TO_COMPLEXEVENTPRICE = 2
                EQUAL_TO_COMPLEXEVENTPRICE = 3
                GREATER_THAN_OR_EQUAL_TO_COMPLEXEVENTPRICE = 4
                GREATER_THAN_COMPLEXEVENTPRICE = 5

        class ComplexEventPriceBoundaryPrecision(Tag):
            Tag = 1488
            Type = "PERCENTAGE"

        class ComplexEventPriceTimeType(Tag):
            Tag = 1489
            Type = "INT"
            class Values:
                EXPIRATION = 1
                IMMEDIATE = 2
                SPECIFIED_DATE_TIME = 3

        class ComplexEventCondition(Tag):
            Tag = 1490
            Type = "INT"
            class Values:
                AND = 1
                OR = 2

        class NoComplexEventDates(Tag):
            Tag = 1491
            Type = "NUMINGROUP"

        class ComplexEventStartDate(Tag):
            Tag = 1492
            Type = "UTCTIMESTAMP"

        class ComplexEventEndDate(Tag):
            Tag = 1493
            Type = "UTCTIMESTAMP"

        class NoComplexEventTimes(Tag):
            Tag = 1494
            Type = "NUMINGROUP"

        class ComplexEventStartTime(Tag):
            Tag = 1495
            Type = "UTCTIMEONLY"

        class ComplexEventEndTime(Tag):
            Tag = 1496
            Type = "UTCTIMEONLY"

        class StreamAsgnReqID(Tag):
            Tag = 1497
            Type = "STRING"

        class StreamAsgnReqType(Tag):
            Tag = 1498
            Type = "INT"
            class Values:
                STREAM_ASSIGNMENT_FOR_NEW_CUSTOMER = 1
                STREAM_ASSIGNMENT_FOR_EXISTING_CUSTOMER = 2

        class NoAsgnReqs(Tag):
            Tag = 1499
            Type = "NUMINGROUP"

        class MDStreamID(Tag):
            Tag = 1500
            Type = "STRING"

        class StreamAsgnRptID(Tag):
            Tag = 1501
            Type = "STRING"

        class StreamAsgnRejReason(Tag):
            Tag = 1502
            Type = "INT"
            class Values:
                UNKNOWN_CLIENT = 0
                EXCEEDS_MAXIMUM_SIZE = 1
                UNKNOWN_OR_INVALID_CURRENCY_PAIR = 2
                NO_AVAILABLE_STREAM = 3
                OTHER = 99

        class StreamAsgnAckType(Tag):
            Tag = 1503
            Type = "INT"
            class Values:
                ASSIGNMENT_ACCEPTED = 0
                ASSIGNMENT_REJECTED = 1

        class RelSymTransactTime(Tag):
            Tag = 1504
            Type = "UTCTIMESTAMP"

        class StreamAsgnType(Tag):
            Tag = 1617
            Type = "INT"
            class Values:
                ASSIGNMENT = 1
                REJECTED = 2
                TERMINATE_UNASSIGN = 3


    class Components:
        class CommissionData(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.Commission = FIX50SP2.Tags.Commission(required=False)
                self.CommType = FIX50SP2.Tags.CommType(required=False)
                self.CommCurrency = FIX50SP2.Tags.CommCurrency(required=False)
                self.FundRenewWaiv = FIX50SP2.Tags.FundRenewWaiv(required=False)

        class DiscretionInstructions(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.DiscretionInst = FIX50SP2.Tags.DiscretionInst(required=False)
                self.DiscretionOffsetValue = FIX50SP2.Tags.DiscretionOffsetValue(required=False)
                self.DiscretionMoveType = FIX50SP2.Tags.DiscretionMoveType(required=False)
                self.DiscretionOffsetType = FIX50SP2.Tags.DiscretionOffsetType(required=False)
                self.DiscretionLimitType = FIX50SP2.Tags.DiscretionLimitType(required=False)
                self.DiscretionRoundDirection = FIX50SP2.Tags.DiscretionRoundDirection(required=False)
                self.DiscretionScope = FIX50SP2.Tags.DiscretionScope(required=False)

        class FinancingDetails(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.AgreementDesc = FIX50SP2.Tags.AgreementDesc(required=False)
                self.AgreementID = FIX50SP2.Tags.AgreementID(required=False)
                self.AgreementDate = FIX50SP2.Tags.AgreementDate(required=False)
                self.AgreementCurrency = FIX50SP2.Tags.AgreementCurrency(required=False)
                self.TerminationType = FIX50SP2.Tags.TerminationType(required=False)
                self.StartDate = FIX50SP2.Tags.StartDate(required=False)
                self.EndDate = FIX50SP2.Tags.EndDate(required=False)
                self.DeliveryType = FIX50SP2.Tags.DeliveryType(required=False)
                self.MarginRatio = FIX50SP2.Tags.MarginRatio(required=False)

        class LegBenchmarkCurveData(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.LegBenchmarkCurveCurrency = FIX50SP2.Tags.LegBenchmarkCurveCurrency(required=False)
                self.LegBenchmarkCurveName = FIX50SP2.Tags.LegBenchmarkCurveName(required=False)
                self.LegBenchmarkCurvePoint = FIX50SP2.Tags.LegBenchmarkCurvePoint(required=False)
                self.LegBenchmarkPrice = FIX50SP2.Tags.LegBenchmarkPrice(required=False)
                self.LegBenchmarkPriceType = FIX50SP2.Tags.LegBenchmarkPriceType(required=False)

        class LegStipulations(RepeatingGroup):
            class NoLegStipulations(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.LegStipulationType = FIX50SP2.Tags.LegStipulationType(required=False)
                    self.LegStipulationValue = FIX50SP2.Tags.LegStipulationValue(required=False)

        class OrderQtyData(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.OrderQty = FIX50SP2.Tags.OrderQty(required=False)
                self.CashOrderQty = FIX50SP2.Tags.CashOrderQty(required=False)
                self.OrderPercent = FIX50SP2.Tags.OrderPercent(required=False)
                self.RoundingDirection = FIX50SP2.Tags.RoundingDirection(required=False)
                self.RoundingModulus = FIX50SP2.Tags.RoundingModulus(required=False)

        class PegInstructions(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.PegOffsetValue = FIX50SP2.Tags.PegOffsetValue(required=False)
                self.PegPriceType = FIX50SP2.Tags.PegPriceType(required=False)
                self.PegMoveType = FIX50SP2.Tags.PegMoveType(required=False)
                self.PegOffsetType = FIX50SP2.Tags.PegOffsetType(required=False)
                self.PegLimitType = FIX50SP2.Tags.PegLimitType(required=False)
                self.PegRoundDirection = FIX50SP2.Tags.PegRoundDirection(required=False)
                self.PegScope = FIX50SP2.Tags.PegScope(required=False)
                self.PegSecurityIDSource = FIX50SP2.Tags.PegSecurityIDSource(required=False)
                self.PegSecurityID = FIX50SP2.Tags.PegSecurityID(required=False)
                self.PegSymbol = FIX50SP2.Tags.PegSymbol(required=False)
                self.PegSecurityDesc = FIX50SP2.Tags.PegSecurityDesc(required=False)

        class PositionAmountData(RepeatingGroup):
            class NoPosAmt(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.PosAmtType = FIX50SP2.Tags.PosAmtType(required=False)
                    self.PosAmt = FIX50SP2.Tags.PosAmt(required=False)
                    self.PositionCurrency = FIX50SP2.Tags.PositionCurrency(required=False)

        class SpreadOrBenchmarkCurveData(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.Spread = FIX50SP2.Tags.Spread(required=False)
                self.BenchmarkCurveCurrency = FIX50SP2.Tags.BenchmarkCurveCurrency(required=False)
                self.BenchmarkCurveName = FIX50SP2.Tags.BenchmarkCurveName(required=False)
                self.BenchmarkCurvePoint = FIX50SP2.Tags.BenchmarkCurvePoint(required=False)
                self.BenchmarkPrice = FIX50SP2.Tags.BenchmarkPrice(required=False)
                self.BenchmarkPriceType = FIX50SP2.Tags.BenchmarkPriceType(required=False)
                self.BenchmarkSecurityID = FIX50SP2.Tags.BenchmarkSecurityID(required=False)
                self.BenchmarkSecurityIDSource = FIX50SP2.Tags.BenchmarkSecurityIDSource(required=False)

        class Stipulations(RepeatingGroup):
            class NoStipulations(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.StipulationType = FIX50SP2.Tags.StipulationType(required=False)
                    self.StipulationValue = FIX50SP2.Tags.StipulationValue(required=False)

        class TrdRegTimestamps(RepeatingGroup):
            class NoTrdRegTimestamps(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.TrdRegTimestamp = FIX50SP2.Tags.TrdRegTimestamp(required=False)
                    self.TrdRegTimestampType = FIX50SP2.Tags.TrdRegTimestampType(required=False)
                    self.TrdRegTimestampOrigin = FIX50SP2.Tags.TrdRegTimestampOrigin(required=False)
                    self.DeskType = FIX50SP2.Tags.DeskType(required=False)
                    self.DeskTypeSource = FIX50SP2.Tags.DeskTypeSource(required=False)
                    self.DeskOrderHandlingInst = FIX50SP2.Tags.DeskOrderHandlingInst(required=False)

        class YieldData(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.YieldType = FIX50SP2.Tags.YieldType(required=False)
                self.Yield = FIX50SP2.Tags.Yield(required=False)
                self.YieldCalcDate = FIX50SP2.Tags.YieldCalcDate(required=False)
                self.YieldRedemptionDate = FIX50SP2.Tags.YieldRedemptionDate(required=False)
                self.YieldRedemptionPrice = FIX50SP2.Tags.YieldRedemptionPrice(required=False)
                self.YieldRedemptionPriceType = FIX50SP2.Tags.YieldRedemptionPriceType(required=False)

        class UnderlyingStipulations(RepeatingGroup):
            class NoUnderlyingStips(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.UnderlyingStipType = FIX50SP2.Tags.UnderlyingStipType(required=False)
                    self.UnderlyingStipValue = FIX50SP2.Tags.UnderlyingStipValue(required=False)

        class AffectedOrdGrp(RepeatingGroup):
            class NoAffectedOrders(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.OrigClOrdID = FIX50SP2.Tags.OrigClOrdID(required=False)
                    self.AffectedOrderID = FIX50SP2.Tags.AffectedOrderID(required=False)
                    self.AffectedSecondaryOrderID = FIX50SP2.Tags.AffectedSecondaryOrderID(required=False)

        class BidCompReqGrp(RepeatingGroup):
            class NoBidComponents(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.ListID = FIX50SP2.Tags.ListID(required=False)
                    self.Side = FIX50SP2.Tags.Side(required=False)
                    self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                    self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                    self.NetGrossInd = FIX50SP2.Tags.NetGrossInd(required=False)
                    self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                    self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                    self.Account = FIX50SP2.Tags.Account(required=False)
                    self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)

        class BidDescReqGrp(RepeatingGroup):
            class NoBidDescriptors(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.BidDescriptorType = FIX50SP2.Tags.BidDescriptorType(required=False)
                    self.BidDescriptor = FIX50SP2.Tags.BidDescriptor(required=False)
                    self.SideValueInd = FIX50SP2.Tags.SideValueInd(required=False)
                    self.LiquidityValue = FIX50SP2.Tags.LiquidityValue(required=False)
                    self.LiquidityNumSecurities = FIX50SP2.Tags.LiquidityNumSecurities(required=False)
                    self.LiquidityPctLow = FIX50SP2.Tags.LiquidityPctLow(required=False)
                    self.LiquidityPctHigh = FIX50SP2.Tags.LiquidityPctHigh(required=False)
                    self.EFPTrackingError = FIX50SP2.Tags.EFPTrackingError(required=False)
                    self.FairValue = FIX50SP2.Tags.FairValue(required=False)
                    self.OutsideIndexPct = FIX50SP2.Tags.OutsideIndexPct(required=False)
                    self.ValueOfFutures = FIX50SP2.Tags.ValueOfFutures(required=False)

        class ClrInstGrp(RepeatingGroup):
            class NoClearingInstructions(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.ClearingInstruction = FIX50SP2.Tags.ClearingInstruction(required=False)

        class CollInqQualGrp(RepeatingGroup):
            class NoCollInquiryQualifier(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.CollInquiryQualifier = FIX50SP2.Tags.CollInquiryQualifier(required=False)

        class CompIDReqGrp(RepeatingGroup):
            class NoCompIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.RefCompID = FIX50SP2.Tags.RefCompID(required=False)
                    self.RefSubID = FIX50SP2.Tags.RefSubID(required=False)
                    self.LocationID = FIX50SP2.Tags.LocationID(required=False)
                    self.DeskID = FIX50SP2.Tags.DeskID(required=False)

        class CompIDStatGrp(RepeatingGroup):
            class NoCompIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.RefCompID = FIX50SP2.Tags.RefCompID(required=True)
                    self.RefSubID = FIX50SP2.Tags.RefSubID(required=False)
                    self.LocationID = FIX50SP2.Tags.LocationID(required=False)
                    self.DeskID = FIX50SP2.Tags.DeskID(required=False)
                    self.StatusValue = FIX50SP2.Tags.StatusValue(required=True)
                    self.StatusText = FIX50SP2.Tags.StatusText(required=False)

        class ContAmtGrp(RepeatingGroup):
            class NoContAmts(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.ContAmtType = FIX50SP2.Tags.ContAmtType(required=False)
                    self.ContAmtValue = FIX50SP2.Tags.ContAmtValue(required=False)
                    self.ContAmtCurr = FIX50SP2.Tags.ContAmtCurr(required=False)

        class ContraGrp(RepeatingGroup):
            class NoContraBrokers(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.ContraBroker = FIX50SP2.Tags.ContraBroker(required=False)
                    self.ContraTrader = FIX50SP2.Tags.ContraTrader(required=False)
                    self.ContraTradeQty = FIX50SP2.Tags.ContraTradeQty(required=False)
                    self.ContraTradeTime = FIX50SP2.Tags.ContraTradeTime(required=False)
                    self.ContraLegRefID = FIX50SP2.Tags.ContraLegRefID(required=False)

        class CpctyConfGrp(RepeatingGroup):
            class NoCapacities(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.OrderCapacity = FIX50SP2.Tags.OrderCapacity(required=True)
                    self.OrderRestrictions = FIX50SP2.Tags.OrderRestrictions(required=False)
                    self.OrderCapacityQty = FIX50SP2.Tags.OrderCapacityQty(required=True)

        class ExecAllocGrp(RepeatingGroup):
            class NoExecs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.LastQty = FIX50SP2.Tags.LastQty(required=False)
                    self.ExecID = FIX50SP2.Tags.ExecID(required=False)
                    self.SecondaryExecID = FIX50SP2.Tags.SecondaryExecID(required=False)
                    self.LastPx = FIX50SP2.Tags.LastPx(required=False)
                    self.LastParPx = FIX50SP2.Tags.LastParPx(required=False)
                    self.LastCapacity = FIX50SP2.Tags.LastCapacity(required=False)
                    self.TradeID = FIX50SP2.Tags.TradeID(required=False)
                    self.FirmTradeID = FIX50SP2.Tags.FirmTradeID(required=False)

        class ExecCollGrp(RepeatingGroup):
            class NoExecs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.ExecID = FIX50SP2.Tags.ExecID(required=False)

        class IOIQualGrp(RepeatingGroup):
            class NoIOIQualifiers(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.IOIQualifier = FIX50SP2.Tags.IOIQualifier(required=False)

        class LinesOfTextGrp(RepeatingGroup):
            class NoLinesOfText(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Text = FIX50SP2.Tags.Text(required=True)
                    self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                    self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)

        class MDReqGrp(RepeatingGroup):
            class NoMDEntryTypes(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.MDEntryType = FIX50SP2.Tags.MDEntryType(required=True)

        class MDRjctGrp(RepeatingGroup):
            class NoAltMDSource(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.AltMDSourceID = FIX50SP2.Tags.AltMDSourceID(required=False)

        class MiscFeesGrp(RepeatingGroup):
            class NoMiscFees(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.MiscFeeAmt = FIX50SP2.Tags.MiscFeeAmt(required=False)
                    self.MiscFeeCurr = FIX50SP2.Tags.MiscFeeCurr(required=False)
                    self.MiscFeeType = FIX50SP2.Tags.MiscFeeType(required=False)
                    self.MiscFeeBasis = FIX50SP2.Tags.MiscFeeBasis(required=False)

        class OrdListStatGrp(RepeatingGroup):
            class NoOrders(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                    self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                    self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                    self.CumQty = FIX50SP2.Tags.CumQty(required=True)
                    self.OrdStatus = FIX50SP2.Tags.OrdStatus(required=True)
                    self.WorkingIndicator = FIX50SP2.Tags.WorkingIndicator(required=False)
                    self.LeavesQty = FIX50SP2.Tags.LeavesQty(required=True)
                    self.CxlQty = FIX50SP2.Tags.CxlQty(required=True)
                    self.AvgPx = FIX50SP2.Tags.AvgPx(required=True)
                    self.OrdRejReason = FIX50SP2.Tags.OrdRejReason(required=False)
                    self.Text = FIX50SP2.Tags.Text(required=False)
                    self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                    self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)

        class QuotQualGrp(RepeatingGroup):
            class NoQuoteQualifiers(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.QuoteQualifier = FIX50SP2.Tags.QuoteQualifier(required=False)

        class RgstDistInstGrp(RepeatingGroup):
            class NoDistribInsts(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.DistribPaymentMethod = FIX50SP2.Tags.DistribPaymentMethod(required=False)
                    self.DistribPercentage = FIX50SP2.Tags.DistribPercentage(required=False)
                    self.CashDistribCurr = FIX50SP2.Tags.CashDistribCurr(required=False)
                    self.CashDistribAgentName = FIX50SP2.Tags.CashDistribAgentName(required=False)
                    self.CashDistribAgentCode = FIX50SP2.Tags.CashDistribAgentCode(required=False)
                    self.CashDistribAgentAcctNumber = FIX50SP2.Tags.CashDistribAgentAcctNumber(required=False)
                    self.CashDistribPayRef = FIX50SP2.Tags.CashDistribPayRef(required=False)
                    self.CashDistribAgentAcctName = FIX50SP2.Tags.CashDistribAgentAcctName(required=False)

        class RoutingGrp(RepeatingGroup):
            class NoRoutingIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.RoutingType = FIX50SP2.Tags.RoutingType(required=False)
                    self.RoutingID = FIX50SP2.Tags.RoutingID(required=False)

        class SecTypesGrp(RepeatingGroup):
            class NoSecurityTypes(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.SecurityType = FIX50SP2.Tags.SecurityType(required=False)
                    self.SecuritySubType = FIX50SP2.Tags.SecuritySubType(required=False)
                    self.Product = FIX50SP2.Tags.Product(required=False)
                    self.CFICode = FIX50SP2.Tags.CFICode(required=False)
                    self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)

        class TrdCollGrp(RepeatingGroup):
            class NoTrades(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.TradeReportID = FIX50SP2.Tags.TradeReportID(required=False)
                    self.SecondaryTradeReportID = FIX50SP2.Tags.SecondaryTradeReportID(required=False)

        class TrdgSesGrp(RepeatingGroup):
            class NoTradingSessions(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                    self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)

        class TrdCapDtGrp(RepeatingGroup):
            class NoDates(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                    self.LastUpdateTime = FIX50SP2.Tags.LastUpdateTime(required=False)
                    self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)

        class EvntGrp(RepeatingGroup):
            class NoEvents(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.EventType = FIX50SP2.Tags.EventType(required=False)
                    self.EventDate = FIX50SP2.Tags.EventDate(required=False)
                    self.EventTime = FIX50SP2.Tags.EventTime(required=False)
                    self.EventPx = FIX50SP2.Tags.EventPx(required=False)
                    self.EventText = FIX50SP2.Tags.EventText(required=False)

        class SecAltIDGrp(RepeatingGroup):
            class NoSecurityAltID(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.SecurityAltID = FIX50SP2.Tags.SecurityAltID(required=False)
                    self.SecurityAltIDSource = FIX50SP2.Tags.SecurityAltIDSource(required=False)

        class LegSecAltIDGrp(RepeatingGroup):
            class NoLegSecurityAltID(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.LegSecurityAltID = FIX50SP2.Tags.LegSecurityAltID(required=False)
                    self.LegSecurityAltIDSource = FIX50SP2.Tags.LegSecurityAltIDSource(required=False)

        class UndSecAltIDGrp(RepeatingGroup):
            class NoUnderlyingSecurityAltID(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.UnderlyingSecurityAltID = FIX50SP2.Tags.UnderlyingSecurityAltID(required=False)
                    self.UnderlyingSecurityAltIDSource = FIX50SP2.Tags.UnderlyingSecurityAltIDSource(required=False)

        class AttrbGrp(RepeatingGroup):
            class NoInstrAttrib(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.InstrAttribType = FIX50SP2.Tags.InstrAttribType(required=False)
                    self.InstrAttribValue = FIX50SP2.Tags.InstrAttribValue(required=False)

        class SettlPtysSubGrp(RepeatingGroup):
            class NoSettlPartySubIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.SettlPartySubID = FIX50SP2.Tags.SettlPartySubID(required=False)
                    self.SettlPartySubIDType = FIX50SP2.Tags.SettlPartySubIDType(required=False)

        class PtysSubGrp(RepeatingGroup):
            class NoPartySubIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.PartySubID = FIX50SP2.Tags.PartySubID(required=False)
                    self.PartySubIDType = FIX50SP2.Tags.PartySubIDType(required=False)

        class NstdPtysSubGrp(RepeatingGroup):
            class NoNestedPartySubIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.NestedPartySubID = FIX50SP2.Tags.NestedPartySubID(required=False)
                    self.NestedPartySubIDType = FIX50SP2.Tags.NestedPartySubIDType(required=False)

        class HopGrp(RepeatingGroup):
            class NoHops(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.HopCompID = FIX50SP2.Tags.HopCompID(required=False)
                    self.HopSendingTime = FIX50SP2.Tags.HopSendingTime(required=False)
                    self.HopRefID = FIX50SP2.Tags.HopRefID(required=False)

        class NstdPtys2SubGrp(RepeatingGroup):
            class NoNested2PartySubIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Nested2PartySubID = FIX50SP2.Tags.Nested2PartySubID(required=False)
                    self.Nested2PartySubIDType = FIX50SP2.Tags.Nested2PartySubIDType(required=False)

        class NstdPtys3SubGrp(RepeatingGroup):
            class NoNested3PartySubIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Nested3PartySubID = FIX50SP2.Tags.Nested3PartySubID(required=False)
                    self.Nested3PartySubIDType = FIX50SP2.Tags.Nested3PartySubIDType(required=False)

        class StrategyParametersGrp(RepeatingGroup):
            class NoStrategyParameters(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.StrategyParameterName = FIX50SP2.Tags.StrategyParameterName(required=False)
                    self.StrategyParameterType = FIX50SP2.Tags.StrategyParameterType(required=False)
                    self.StrategyParameterValue = FIX50SP2.Tags.StrategyParameterValue(required=False)

        class UnderlyingAmount(RepeatingGroup):
            class NoUnderlyingAmounts(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.UnderlyingPayAmount = FIX50SP2.Tags.UnderlyingPayAmount(required=False)
                    self.UnderlyingCollectAmount = FIX50SP2.Tags.UnderlyingCollectAmount(required=False)
                    self.UnderlyingSettlementDate = FIX50SP2.Tags.UnderlyingSettlementDate(required=False)
                    self.UnderlyingSettlementStatus = FIX50SP2.Tags.UnderlyingSettlementStatus(required=False)

        class ExpirationQty(RepeatingGroup):
            class NoExpiration(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.ExpirationQtyType = FIX50SP2.Tags.ExpirationQtyType(required=False)
                    self.ExpQty = FIX50SP2.Tags.ExpQty(required=False)

        class InstrumentPtysSubGrp(RepeatingGroup):
            class NoInstrumentPartySubIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.InstrumentPartySubID = FIX50SP2.Tags.InstrumentPartySubID(required=False)
                    self.InstrumentPartySubIDType = FIX50SP2.Tags.InstrumentPartySubIDType(required=False)

        class SideTrdRegTS(RepeatingGroup):
            class NoSideTrdRegTS(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.SideTrdRegTimestamp = FIX50SP2.Tags.SideTrdRegTimestamp(required=False)
                    self.SideTrdRegTimestampType = FIX50SP2.Tags.SideTrdRegTimestampType(required=False)
                    self.SideTrdRegTimestampSrc = FIX50SP2.Tags.SideTrdRegTimestampSrc(required=False)

        class UndlyInstrumentPtysSubGrp(RepeatingGroup):
            class NoUndlyInstrumentPartySubIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.UnderlyingInstrumentPartySubID = FIX50SP2.Tags.UnderlyingInstrumentPartySubID(required=False)
                    self.UnderlyingInstrumentPartySubIDType = FIX50SP2.Tags.UnderlyingInstrumentPartySubIDType(required=False)

        class DisplayInstruction(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.DisplayQty = FIX50SP2.Tags.DisplayQty(required=False)
                self.SecondaryDisplayQty = FIX50SP2.Tags.SecondaryDisplayQty(required=False)
                self.DisplayWhen = FIX50SP2.Tags.DisplayWhen(required=False)
                self.DisplayMethod = FIX50SP2.Tags.DisplayMethod(required=False)
                self.DisplayLowQty = FIX50SP2.Tags.DisplayLowQty(required=False)
                self.DisplayHighQty = FIX50SP2.Tags.DisplayHighQty(required=False)
                self.DisplayMinIncr = FIX50SP2.Tags.DisplayMinIncr(required=False)
                self.RefreshQty = FIX50SP2.Tags.RefreshQty(required=False)

        class TriggeringInstruction(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.TriggerType = FIX50SP2.Tags.TriggerType(required=False)
                self.TriggerAction = FIX50SP2.Tags.TriggerAction(required=False)
                self.TriggerPrice = FIX50SP2.Tags.TriggerPrice(required=False)
                self.TriggerSymbol = FIX50SP2.Tags.TriggerSymbol(required=False)
                self.TriggerSecurityID = FIX50SP2.Tags.TriggerSecurityID(required=False)
                self.TriggerSecurityIDSource = FIX50SP2.Tags.TriggerSecurityIDSource(required=False)
                self.TriggerSecurityDesc = FIX50SP2.Tags.TriggerSecurityDesc(required=False)
                self.TriggerPriceType = FIX50SP2.Tags.TriggerPriceType(required=False)
                self.TriggerPriceTypeScope = FIX50SP2.Tags.TriggerPriceTypeScope(required=False)
                self.TriggerPriceDirection = FIX50SP2.Tags.TriggerPriceDirection(required=False)
                self.TriggerNewPrice = FIX50SP2.Tags.TriggerNewPrice(required=False)
                self.TriggerOrderType = FIX50SP2.Tags.TriggerOrderType(required=False)
                self.TriggerNewQty = FIX50SP2.Tags.TriggerNewQty(required=False)
                self.TriggerTradingSessionID = FIX50SP2.Tags.TriggerTradingSessionID(required=False)
                self.TriggerTradingSessionSubID = FIX50SP2.Tags.TriggerTradingSessionSubID(required=False)

        class RootSubParties(RepeatingGroup):
            class NoRootPartySubIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.RootPartySubID = FIX50SP2.Tags.RootPartySubID(required=False)
                    self.RootPartySubIDType = FIX50SP2.Tags.RootPartySubIDType(required=False)

        class MsgTypeGrp(RepeatingGroup):
            class NoMsgTypes(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.RefMsgType = FIX50SP2.Tags.RefMsgType(required=False)
                    self.MsgDirection = FIX50SP2.Tags.MsgDirection(required=False)
                    self.RefApplVerID = FIX50SP2.Tags.RefApplVerID(required=False)
                    self.RefApplExtID = FIX50SP2.Tags.RefApplExtID(required=False)
                    self.RefCstmApplVerID = FIX50SP2.Tags.RefCstmApplVerID(required=False)
                    self.DefaultVerIndicator = FIX50SP2.Tags.DefaultVerIndicator(required=False)

        class SecSizesGrp(RepeatingGroup):
            class NoOfSecSizes(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.MDSecSizeType = FIX50SP2.Tags.MDSecSizeType(required=False)
                    self.MDSecSize = FIX50SP2.Tags.MDSecSize(required=False)

        class StatsIndGrp(RepeatingGroup):
            class NoStatsIndicators(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.StatsType = FIX50SP2.Tags.StatsType(required=False)

        class SecurityXML(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.SecurityXMLLen = FIX50SP2.Tags.SecurityXMLLen(required=False)
                self.SecurityXML = FIX50SP2.Tags.SecurityXML(required=False)
                self.SecurityXMLSchema = FIX50SP2.Tags.SecurityXMLSchema(required=False)

        class TickRules(RepeatingGroup):
            class NoTickRules(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.StartTickPriceRange = FIX50SP2.Tags.StartTickPriceRange(required=False)
                    self.EndTickPriceRange = FIX50SP2.Tags.EndTickPriceRange(required=False)
                    self.TickIncrement = FIX50SP2.Tags.TickIncrement(required=False)
                    self.TickRuleType = FIX50SP2.Tags.TickRuleType(required=False)

        class MaturityRules(RepeatingGroup):
            class NoMaturityRules(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.MaturityRuleID = FIX50SP2.Tags.MaturityRuleID(required=False)
                    self.MaturityMonthYearFormat = FIX50SP2.Tags.MaturityMonthYearFormat(required=False)
                    self.MaturityMonthYearIncrementUnits = FIX50SP2.Tags.MaturityMonthYearIncrementUnits(required=False)
                    self.StartMaturityMonthYear = FIX50SP2.Tags.StartMaturityMonthYear(required=False)
                    self.EndMaturityMonthYear = FIX50SP2.Tags.EndMaturityMonthYear(required=False)
                    self.MaturityMonthYearIncrement = FIX50SP2.Tags.MaturityMonthYearIncrement(required=False)

        class SecondaryPriceLimits(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.SecondaryPriceLimitType = FIX50SP2.Tags.SecondaryPriceLimitType(required=False)
                self.SecondaryLowLimitPrice = FIX50SP2.Tags.SecondaryLowLimitPrice(required=False)
                self.SecondaryHighLimitPrice = FIX50SP2.Tags.SecondaryHighLimitPrice(required=False)
                self.SecondaryTradingReferencePrice = FIX50SP2.Tags.SecondaryTradingReferencePrice(required=False)

        class PriceLimits(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.PriceLimitType = FIX50SP2.Tags.PriceLimitType(required=False)
                self.LowLimitPrice = FIX50SP2.Tags.LowLimitPrice(required=False)
                self.HighLimitPrice = FIX50SP2.Tags.HighLimitPrice(required=False)
                self.TradingReferencePrice = FIX50SP2.Tags.TradingReferencePrice(required=False)

        class MarketDataFeedTypes(RepeatingGroup):
            class NoMDFeedTypes(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.MDFeedType = FIX50SP2.Tags.MDFeedType(required=False)
                    self.MarketDepth = FIX50SP2.Tags.MarketDepth(required=False)
                    self.MDBookType = FIX50SP2.Tags.MDBookType(required=False)

        class LotTypeRules(RepeatingGroup):
            class NoLotTypeRules(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.LotType = FIX50SP2.Tags.LotType(required=False)
                    self.MinLotSize = FIX50SP2.Tags.MinLotSize(required=False)

        class MatchRules(RepeatingGroup):
            class NoMatchRules(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.MatchAlgorithm = FIX50SP2.Tags.MatchAlgorithm(required=False)
                    self.MatchType = FIX50SP2.Tags.MatchType(required=False)

        class ExecInstRules(RepeatingGroup):
            class NoExecInstRules(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.ExecInstValue = FIX50SP2.Tags.ExecInstValue(required=False)

        class TimeInForceRules(RepeatingGroup):
            class NoTimeInForceRules(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.TimeInForce = FIX50SP2.Tags.TimeInForce(required=False)

        class OrdTypeRules(RepeatingGroup):
            class NoOrdTypeRules(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.OrdType = FIX50SP2.Tags.OrdType(required=False)

        class DerivativeInstrumentPartySubIDsGrp(RepeatingGroup):
            class NoDerivativeInstrumentPartySubIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.DerivativeInstrumentPartySubID = FIX50SP2.Tags.DerivativeInstrumentPartySubID(required=False)
                    self.DerivativeInstrumentPartySubIDType = FIX50SP2.Tags.DerivativeInstrumentPartySubIDType(required=False)

        class DerivativeInstrumentAttribute(RepeatingGroup):
            class NoDerivativeInstrAttrib(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.DerivativeInstrAttribType = FIX50SP2.Tags.DerivativeInstrAttribType(required=False)
                    self.DerivativeInstrAttribValue = FIX50SP2.Tags.DerivativeInstrAttribValue(required=False)

        class NestedInstrumentAttribute(RepeatingGroup):
            class NoNestedInstrAttrib(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.NestedInstrAttribType = FIX50SP2.Tags.NestedInstrAttribType(required=False)
                    self.NestedInstrAttribValue = FIX50SP2.Tags.NestedInstrAttribValue(required=False)

        class DerivativeSecurityAltIDGrp(RepeatingGroup):
            class NoDerivativeSecurityAltID(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.DerivativeSecurityAltID = FIX50SP2.Tags.DerivativeSecurityAltID(required=False)
                    self.DerivativeSecurityAltIDSource = FIX50SP2.Tags.DerivativeSecurityAltIDSource(required=False)

        class DerivativeEventsGrp(RepeatingGroup):
            class NoDerivativeEvents(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.DerivativeEventType = FIX50SP2.Tags.DerivativeEventType(required=False)
                    self.DerivativeEventDate = FIX50SP2.Tags.DerivativeEventDate(required=False)
                    self.DerivativeEventTime = FIX50SP2.Tags.DerivativeEventTime(required=False)
                    self.DerivativeEventPx = FIX50SP2.Tags.DerivativeEventPx(required=False)
                    self.DerivativeEventText = FIX50SP2.Tags.DerivativeEventText(required=False)

        class DerivativeSecurityXML(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.DerivativeSecurityXMLLen = FIX50SP2.Tags.DerivativeSecurityXMLLen(required=False)
                self.DerivativeSecurityXML = FIX50SP2.Tags.DerivativeSecurityXML(required=False)
                self.DerivativeSecurityXMLSchema = FIX50SP2.Tags.DerivativeSecurityXMLSchema(required=False)

        class UnderlyingLegSecurityAltIDGrp(RepeatingGroup):
            class NoUnderlyingLegSecurityAltID(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.UnderlyingLegSecurityAltID = FIX50SP2.Tags.UnderlyingLegSecurityAltID(required=False)
                    self.UnderlyingLegSecurityAltIDSource = FIX50SP2.Tags.UnderlyingLegSecurityAltIDSource(required=False)

        class UsernameGrp(RepeatingGroup):
            class NoUsernames(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Username = FIX50SP2.Tags.Username(required=False)

        class NotAffectedOrdersGrp(RepeatingGroup):
            class NoNotAffectedOrders(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.NotAffOrigClOrdID = FIX50SP2.Tags.NotAffOrigClOrdID(required=False)
                    self.NotAffectedOrderID = FIX50SP2.Tags.NotAffectedOrderID(required=False)

        class TrdRepIndicatorsGrp(RepeatingGroup):
            class NoTrdRepIndicators(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.TrdRepPartyRole = FIX50SP2.Tags.TrdRepPartyRole(required=False)
                    self.TrdRepIndicator = FIX50SP2.Tags.TrdRepIndicator(required=False)

        class ApplicationSequenceControl(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.ApplID = FIX50SP2.Tags.ApplID(required=False)
                self.ApplSeqNum = FIX50SP2.Tags.ApplSeqNum(required=False)
                self.ApplLastSeqNum = FIX50SP2.Tags.ApplLastSeqNum(required=False)
                self.ApplResendFlag = FIX50SP2.Tags.ApplResendFlag(required=False)

        class ApplIDReportGrp(RepeatingGroup):
            class NoApplIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.RefApplID = FIX50SP2.Tags.RefApplID(required=False)
                    self.ApplNewSeqNum = FIX50SP2.Tags.ApplNewSeqNum(required=False)
                    self.RefApplLastSeqNum = FIX50SP2.Tags.RefApplLastSeqNum(required=False)

        class NstdPtys4SubGrp(RepeatingGroup):
            class NoNested4PartySubIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Nested4PartySubID = FIX50SP2.Tags.Nested4PartySubID(required=False)
                    self.Nested4PartySubIDType = FIX50SP2.Tags.Nested4PartySubIDType(required=False)

        class RateSource(RepeatingGroup):
            class NoRateSources(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.RateSource = FIX50SP2.Tags.RateSource(required=False)
                    self.RateSourceType = FIX50SP2.Tags.RateSourceType(required=False)
                    self.ReferencePage = FIX50SP2.Tags.ReferencePage(required=False)

        class TargetParties(RepeatingGroup):
            class NoTargetPartyIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.TargetPartyID = FIX50SP2.Tags.TargetPartyID(required=False)
                    self.TargetPartyIDSource = FIX50SP2.Tags.TargetPartyIDSource(required=False)
                    self.TargetPartyRole = FIX50SP2.Tags.TargetPartyRole(required=False)

        class NewsRefGrp(RepeatingGroup):
            class NoNewsRefIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.NewsRefID = FIX50SP2.Tags.NewsRefID(required=False)
                    self.NewsRefType = FIX50SP2.Tags.NewsRefType(required=False)

        class ComplexEventTimes(RepeatingGroup):
            class NoComplexEventTimes(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.ComplexEventStartTime = FIX50SP2.Tags.ComplexEventStartTime(required=False)
                    self.ComplexEventEndTime = FIX50SP2.Tags.ComplexEventEndTime(required=False)

        class InstrumentExtension(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.DeliveryForm = FIX50SP2.Tags.DeliveryForm(required=False)
                self.PctAtRisk = FIX50SP2.Tags.PctAtRisk(required=False)
                self.AttrbGrp = FIX50SP2.Components.AttrbGrp(required=False)

        class InstrumentLeg(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.LegSymbol = FIX50SP2.Tags.LegSymbol(required=False)
                self.LegSymbolSfx = FIX50SP2.Tags.LegSymbolSfx(required=False)
                self.LegSecurityID = FIX50SP2.Tags.LegSecurityID(required=False)
                self.LegSecurityIDSource = FIX50SP2.Tags.LegSecurityIDSource(required=False)
                self.LegProduct = FIX50SP2.Tags.LegProduct(required=False)
                self.LegCFICode = FIX50SP2.Tags.LegCFICode(required=False)
                self.LegSecurityType = FIX50SP2.Tags.LegSecurityType(required=False)
                self.LegSecuritySubType = FIX50SP2.Tags.LegSecuritySubType(required=False)
                self.LegMaturityMonthYear = FIX50SP2.Tags.LegMaturityMonthYear(required=False)
                self.LegMaturityDate = FIX50SP2.Tags.LegMaturityDate(required=False)
                self.LegMaturityTime = FIX50SP2.Tags.LegMaturityTime(required=False)
                self.LegCouponPaymentDate = FIX50SP2.Tags.LegCouponPaymentDate(required=False)
                self.LegIssueDate = FIX50SP2.Tags.LegIssueDate(required=False)
                self.LegRepoCollateralSecurityType = FIX50SP2.Tags.LegRepoCollateralSecurityType(required=False)
                self.LegRepurchaseTerm = FIX50SP2.Tags.LegRepurchaseTerm(required=False)
                self.LegRepurchaseRate = FIX50SP2.Tags.LegRepurchaseRate(required=False)
                self.LegFactor = FIX50SP2.Tags.LegFactor(required=False)
                self.LegCreditRating = FIX50SP2.Tags.LegCreditRating(required=False)
                self.LegInstrRegistry = FIX50SP2.Tags.LegInstrRegistry(required=False)
                self.LegCountryOfIssue = FIX50SP2.Tags.LegCountryOfIssue(required=False)
                self.LegStateOrProvinceOfIssue = FIX50SP2.Tags.LegStateOrProvinceOfIssue(required=False)
                self.LegLocaleOfIssue = FIX50SP2.Tags.LegLocaleOfIssue(required=False)
                self.LegRedemptionDate = FIX50SP2.Tags.LegRedemptionDate(required=False)
                self.LegStrikePrice = FIX50SP2.Tags.LegStrikePrice(required=False)
                self.LegStrikeCurrency = FIX50SP2.Tags.LegStrikeCurrency(required=False)
                self.LegOptAttribute = FIX50SP2.Tags.LegOptAttribute(required=False)
                self.LegContractMultiplier = FIX50SP2.Tags.LegContractMultiplier(required=False)
                self.LegUnitOfMeasure = FIX50SP2.Tags.LegUnitOfMeasure(required=False)
                self.LegUnitOfMeasureQty = FIX50SP2.Tags.LegUnitOfMeasureQty(required=False)
                self.LegPriceUnitOfMeasure = FIX50SP2.Tags.LegPriceUnitOfMeasure(required=False)
                self.LegPriceUnitOfMeasureQty = FIX50SP2.Tags.LegPriceUnitOfMeasureQty(required=False)
                self.LegTimeUnit = FIX50SP2.Tags.LegTimeUnit(required=False)
                self.LegExerciseStyle = FIX50SP2.Tags.LegExerciseStyle(required=False)
                self.LegCouponRate = FIX50SP2.Tags.LegCouponRate(required=False)
                self.LegSecurityExchange = FIX50SP2.Tags.LegSecurityExchange(required=False)
                self.LegIssuer = FIX50SP2.Tags.LegIssuer(required=False)
                self.EncodedLegIssuerLen = FIX50SP2.Tags.EncodedLegIssuerLen(required=False)
                self.EncodedLegIssuer = FIX50SP2.Tags.EncodedLegIssuer(required=False)
                self.LegSecurityDesc = FIX50SP2.Tags.LegSecurityDesc(required=False)
                self.EncodedLegSecurityDescLen = FIX50SP2.Tags.EncodedLegSecurityDescLen(required=False)
                self.EncodedLegSecurityDesc = FIX50SP2.Tags.EncodedLegSecurityDesc(required=False)
                self.LegRatioQty = FIX50SP2.Tags.LegRatioQty(required=False)
                self.LegSide = FIX50SP2.Tags.LegSide(required=False)
                self.LegCurrency = FIX50SP2.Tags.LegCurrency(required=False)
                self.LegPool = FIX50SP2.Tags.LegPool(required=False)
                self.LegDatedDate = FIX50SP2.Tags.LegDatedDate(required=False)
                self.LegContractSettlMonth = FIX50SP2.Tags.LegContractSettlMonth(required=False)
                self.LegInterestAccrualDate = FIX50SP2.Tags.LegInterestAccrualDate(required=False)
                self.LegPutOrCall = FIX50SP2.Tags.LegPutOrCall(required=False)
                self.LegOptionRatio = FIX50SP2.Tags.LegOptionRatio(required=False)
                self.LegContractMultiplierUnit = FIX50SP2.Tags.LegContractMultiplierUnit(required=False)
                self.LegFlowScheduleType = FIX50SP2.Tags.LegFlowScheduleType(required=False)
                self.LegSecAltIDGrp = FIX50SP2.Components.LegSecAltIDGrp(required=False)

        class NestedParties(RepeatingGroup):
            class NoNestedPartyIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.NestedPartyID = FIX50SP2.Tags.NestedPartyID(required=False)
                    self.NestedPartyIDSource = FIX50SP2.Tags.NestedPartyIDSource(required=False)
                    self.NestedPartyRole = FIX50SP2.Tags.NestedPartyRole(required=False)
                    self.NstdPtysSubGrp = FIX50SP2.Components.NstdPtysSubGrp(required=False)

        class Parties(RepeatingGroup):
            class NoPartyIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.PartyID = FIX50SP2.Tags.PartyID(required=False)
                    self.PartyIDSource = FIX50SP2.Tags.PartyIDSource(required=False)
                    self.PartyRole = FIX50SP2.Tags.PartyRole(required=False)
                    self.PtysSubGrp = FIX50SP2.Components.PtysSubGrp(required=False)

        class PositionQty(RepeatingGroup):
            class NoPositions(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.PosType = FIX50SP2.Tags.PosType(required=False)
                    self.LongQty = FIX50SP2.Tags.LongQty(required=False)
                    self.ShortQty = FIX50SP2.Tags.ShortQty(required=False)
                    self.PosQtyStatus = FIX50SP2.Tags.PosQtyStatus(required=False)
                    self.QuantityDate = FIX50SP2.Tags.QuantityDate(required=False)
                    self.NestedParties = FIX50SP2.Components.NestedParties(required=False)

        class SettlInstructionsData(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.SettlDeliveryType = FIX50SP2.Tags.SettlDeliveryType(required=False)
                self.StandInstDbType = FIX50SP2.Tags.StandInstDbType(required=False)
                self.StandInstDbName = FIX50SP2.Tags.StandInstDbName(required=False)
                self.StandInstDbID = FIX50SP2.Tags.StandInstDbID(required=False)
                self.DlvyInstGrp = FIX50SP2.Components.DlvyInstGrp(required=False)

        class SettlParties(RepeatingGroup):
            class NoSettlPartyIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.SettlPartyID = FIX50SP2.Tags.SettlPartyID(required=False)
                    self.SettlPartyIDSource = FIX50SP2.Tags.SettlPartyIDSource(required=False)
                    self.SettlPartyRole = FIX50SP2.Tags.SettlPartyRole(required=False)
                    self.SettlPtysSubGrp = FIX50SP2.Components.SettlPtysSubGrp(required=False)

        class NestedParties2(RepeatingGroup):
            class NoNested2PartyIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Nested2PartyID = FIX50SP2.Tags.Nested2PartyID(required=False)
                    self.Nested2PartyIDSource = FIX50SP2.Tags.Nested2PartyIDSource(required=False)
                    self.Nested2PartyRole = FIX50SP2.Tags.Nested2PartyRole(required=False)
                    self.NstdPtys2SubGrp = FIX50SP2.Components.NstdPtys2SubGrp(required=False)

        class NestedParties3(RepeatingGroup):
            class NoNested3PartyIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Nested3PartyID = FIX50SP2.Tags.Nested3PartyID(required=False)
                    self.Nested3PartyIDSource = FIX50SP2.Tags.Nested3PartyIDSource(required=False)
                    self.Nested3PartyRole = FIX50SP2.Tags.Nested3PartyRole(required=False)
                    self.NstdPtys3SubGrp = FIX50SP2.Components.NstdPtys3SubGrp(required=False)

        class AllocAckGrp(RepeatingGroup):
            class NoAllocs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.AllocAccount = FIX50SP2.Tags.AllocAccount(required=False)
                    self.AllocAcctIDSource = FIX50SP2.Tags.AllocAcctIDSource(required=False)
                    self.AllocPrice = FIX50SP2.Tags.AllocPrice(required=False)
                    self.AllocPositionEffect = FIX50SP2.Tags.AllocPositionEffect(required=False)
                    self.IndividualAllocID = FIX50SP2.Tags.IndividualAllocID(required=False)
                    self.IndividualAllocRejCode = FIX50SP2.Tags.IndividualAllocRejCode(required=False)
                    self.AllocText = FIX50SP2.Tags.AllocText(required=False)
                    self.EncodedAllocTextLen = FIX50SP2.Tags.EncodedAllocTextLen(required=False)
                    self.EncodedAllocText = FIX50SP2.Tags.EncodedAllocText(required=False)
                    self.SecondaryIndividualAllocID = FIX50SP2.Tags.SecondaryIndividualAllocID(required=False)
                    self.AllocCustomerCapacity = FIX50SP2.Tags.AllocCustomerCapacity(required=False)
                    self.IndividualAllocType = FIX50SP2.Tags.IndividualAllocType(required=False)
                    self.AllocQty = FIX50SP2.Tags.AllocQty(required=False)
                    self.NestedParties = FIX50SP2.Components.NestedParties(required=False)

        class BidCompRspGrp(RepeatingGroup):
            class NoBidComponents(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.ListID = FIX50SP2.Tags.ListID(required=False)
                    self.Country = FIX50SP2.Tags.Country(required=False)
                    self.Side = FIX50SP2.Tags.Side(required=False)
                    self.Price = FIX50SP2.Tags.Price(required=False)
                    self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                    self.FairValue = FIX50SP2.Tags.FairValue(required=False)
                    self.NetGrossInd = FIX50SP2.Tags.NetGrossInd(required=False)
                    self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                    self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                    self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                    self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                    self.Text = FIX50SP2.Tags.Text(required=False)
                    self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                    self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                    self.CommissionData = FIX50SP2.Components.CommissionData(required=True)

        class InstrmtGrp(RepeatingGroup):
            class NoRelatedSym(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Instrument = FIX50SP2.Components.Instrument(required=False)

        class InstrmtLegGrp(RepeatingGroup):
            class NoLegs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.InstrumentLeg = FIX50SP2.Components.InstrumentLeg(required=False)

        class LegPreAllocGrp(RepeatingGroup):
            class NoLegAllocs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.LegAllocAccount = FIX50SP2.Tags.LegAllocAccount(required=False)
                    self.LegIndividualAllocID = FIX50SP2.Tags.LegIndividualAllocID(required=False)
                    self.LegAllocQty = FIX50SP2.Tags.LegAllocQty(required=False)
                    self.LegAllocAcctIDSource = FIX50SP2.Tags.LegAllocAcctIDSource(required=False)
                    self.LegAllocSettlCurrency = FIX50SP2.Tags.LegAllocSettlCurrency(required=False)
                    self.NestedParties2 = FIX50SP2.Components.NestedParties2(required=False)

        class OrdAllocGrp(RepeatingGroup):
            class NoOrders(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                    self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                    self.SecondaryOrderID = FIX50SP2.Tags.SecondaryOrderID(required=False)
                    self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                    self.ListID = FIX50SP2.Tags.ListID(required=False)
                    self.OrderQty = FIX50SP2.Tags.OrderQty(required=False)
                    self.OrderAvgPx = FIX50SP2.Tags.OrderAvgPx(required=False)
                    self.OrderBookingQty = FIX50SP2.Tags.OrderBookingQty(required=False)
                    self.NestedParties2 = FIX50SP2.Components.NestedParties2(required=False)

        class PreAllocGrp(RepeatingGroup):
            class NoAllocs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.AllocAccount = FIX50SP2.Tags.AllocAccount(required=False)
                    self.AllocAcctIDSource = FIX50SP2.Tags.AllocAcctIDSource(required=False)
                    self.AllocSettlCurrency = FIX50SP2.Tags.AllocSettlCurrency(required=False)
                    self.IndividualAllocID = FIX50SP2.Tags.IndividualAllocID(required=False)
                    self.AllocQty = FIX50SP2.Tags.AllocQty(required=False)
                    self.NestedParties = FIX50SP2.Components.NestedParties(required=False)

        class PreAllocMlegGrp(RepeatingGroup):
            class NoAllocs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.AllocAccount = FIX50SP2.Tags.AllocAccount(required=False)
                    self.AllocAcctIDSource = FIX50SP2.Tags.AllocAcctIDSource(required=False)
                    self.AllocSettlCurrency = FIX50SP2.Tags.AllocSettlCurrency(required=False)
                    self.IndividualAllocID = FIX50SP2.Tags.IndividualAllocID(required=False)
                    self.AllocQty = FIX50SP2.Tags.AllocQty(required=False)
                    self.NestedParties3 = FIX50SP2.Components.NestedParties3(required=False)

        class RgstDtlsGrp(RepeatingGroup):
            class NoRegistDtls(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.RegistDtls = FIX50SP2.Tags.RegistDtls(required=False)
                    self.RegistEmail = FIX50SP2.Tags.RegistEmail(required=False)
                    self.MailingDtls = FIX50SP2.Tags.MailingDtls(required=False)
                    self.MailingInst = FIX50SP2.Tags.MailingInst(required=False)
                    self.OwnerType = FIX50SP2.Tags.OwnerType(required=False)
                    self.DateOfBirth = FIX50SP2.Tags.DateOfBirth(required=False)
                    self.InvestorCountryOfResidence = FIX50SP2.Tags.InvestorCountryOfResidence(required=False)
                    self.NestedParties = FIX50SP2.Components.NestedParties(required=False)

        class TrdAllocGrp(RepeatingGroup):
            class NoAllocs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.AllocAccount = FIX50SP2.Tags.AllocAccount(required=False)
                    self.AllocAcctIDSource = FIX50SP2.Tags.AllocAcctIDSource(required=False)
                    self.AllocSettlCurrency = FIX50SP2.Tags.AllocSettlCurrency(required=False)
                    self.IndividualAllocID = FIX50SP2.Tags.IndividualAllocID(required=False)
                    self.AllocQty = FIX50SP2.Tags.AllocQty(required=False)
                    self.AllocCustomerCapacity = FIX50SP2.Tags.AllocCustomerCapacity(required=False)
                    self.AllocMethod = FIX50SP2.Tags.AllocMethod(required=False)
                    self.SecondaryIndividualAllocID = FIX50SP2.Tags.SecondaryIndividualAllocID(required=False)
                    self.AllocClearingFeeIndicator = FIX50SP2.Tags.AllocClearingFeeIndicator(required=False)
                    self.NestedParties2 = FIX50SP2.Components.NestedParties2(required=False)

        class UndInstrmtCollGrp(RepeatingGroup):
            class NoUnderlyings(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.CollAction = FIX50SP2.Tags.CollAction(required=False)
                    self.UnderlyingInstrument = FIX50SP2.Components.UnderlyingInstrument(required=False)

        class UndInstrmtGrp(RepeatingGroup):
            class NoUnderlyings(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.UnderlyingInstrument = FIX50SP2.Components.UnderlyingInstrument(required=False)

        class DlvyInstGrp(RepeatingGroup):
            class NoDlvyInst(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.SettlInstSource = FIX50SP2.Tags.SettlInstSource(required=False)
                    self.DlvyInstType = FIX50SP2.Tags.DlvyInstType(required=False)
                    self.SettlParties = FIX50SP2.Components.SettlParties(required=False)

        class InstrumentParties(RepeatingGroup):
            class NoInstrumentParties(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.InstrumentPartyID = FIX50SP2.Tags.InstrumentPartyID(required=False)
                    self.InstrumentPartyIDSource = FIX50SP2.Tags.InstrumentPartyIDSource(required=False)
                    self.InstrumentPartyRole = FIX50SP2.Tags.InstrumentPartyRole(required=False)
                    self.InstrumentPtysSubGrp = FIX50SP2.Components.InstrumentPtysSubGrp(required=False)

        class UndlyInstrumentParties(RepeatingGroup):
            class NoUndlyInstrumentParties(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.UnderlyingInstrumentPartyID = FIX50SP2.Tags.UnderlyingInstrumentPartyID(required=False)
                    self.UnderlyingInstrumentPartyIDSource = FIX50SP2.Tags.UnderlyingInstrumentPartyIDSource(required=False)
                    self.UnderlyingInstrumentPartyRole = FIX50SP2.Tags.UnderlyingInstrumentPartyRole(required=False)
                    self.UndlyInstrumentPtysSubGrp = FIX50SP2.Components.UndlyInstrumentPtysSubGrp(required=False)

        class RootParties(RepeatingGroup):
            class NoRootPartyIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.RootPartyID = FIX50SP2.Tags.RootPartyID(required=False)
                    self.RootPartyIDSource = FIX50SP2.Tags.RootPartyIDSource(required=False)
                    self.RootPartyRole = FIX50SP2.Tags.RootPartyRole(required=False)
                    self.RootSubParties = FIX50SP2.Components.RootSubParties(required=False)

        class TrdSessLstGrp(RepeatingGroup):
            class NoTradingSessions(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=True)
                    self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                    self.SecurityExchange = FIX50SP2.Tags.SecurityExchange(required=False)
                    self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                    self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                    self.TradingSessionDesc = FIX50SP2.Tags.TradingSessionDesc(required=False)
                    self.TradSesMethod = FIX50SP2.Tags.TradSesMethod(required=False)
                    self.TradSesMode = FIX50SP2.Tags.TradSesMode(required=False)
                    self.UnsolicitedIndicator = FIX50SP2.Tags.UnsolicitedIndicator(required=False)
                    self.TradSesStatus = FIX50SP2.Tags.TradSesStatus(required=True)
                    self.TradSesStatusRejReason = FIX50SP2.Tags.TradSesStatusRejReason(required=False)
                    self.TradSesStartTime = FIX50SP2.Tags.TradSesStartTime(required=False)
                    self.TradSesOpenTime = FIX50SP2.Tags.TradSesOpenTime(required=False)
                    self.TradSesPreCloseTime = FIX50SP2.Tags.TradSesPreCloseTime(required=False)
                    self.TradSesCloseTime = FIX50SP2.Tags.TradSesCloseTime(required=False)
                    self.TradSesEndTime = FIX50SP2.Tags.TradSesEndTime(required=False)
                    self.TotalVolumeTraded = FIX50SP2.Tags.TotalVolumeTraded(required=False)
                    self.Text = FIX50SP2.Tags.Text(required=False)
                    self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                    self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                    self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                    self.TradSesUpdateAction = FIX50SP2.Tags.TradSesUpdateAction(required=False)
                    self.TradingSessionRules = FIX50SP2.Components.TradingSessionRules(required=False)

        class SettlDetails(RepeatingGroup):
            class NoSettlDetails(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.SettlObligSource = FIX50SP2.Tags.SettlObligSource(required=False)
                    self.SettlParties = FIX50SP2.Components.SettlParties(required=False)

        class StrikeRules(RepeatingGroup):
            class NoStrikeRules(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.StrikeRuleID = FIX50SP2.Tags.StrikeRuleID(required=False)
                    self.StartStrikePxRange = FIX50SP2.Tags.StartStrikePxRange(required=False)
                    self.EndStrikePxRange = FIX50SP2.Tags.EndStrikePxRange(required=False)
                    self.StrikeIncrement = FIX50SP2.Tags.StrikeIncrement(required=False)
                    self.StrikeExerciseStyle = FIX50SP2.Tags.StrikeExerciseStyle(required=False)
                    self.MaturityRules = FIX50SP2.Components.MaturityRules(required=False)

        class TradingSessionRulesGrp(RepeatingGroup):
            class NoTradingSessionRules(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                    self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                    self.TradingSessionRules = FIX50SP2.Components.TradingSessionRules(required=False)

        class DerivativeInstrumentParties(RepeatingGroup):
            class NoDerivativeInstrumentParties(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.DerivativeInstrumentPartyID = FIX50SP2.Tags.DerivativeInstrumentPartyID(required=False)
                    self.DerivativeInstrumentPartyIDSource = FIX50SP2.Tags.DerivativeInstrumentPartyIDSource(required=False)
                    self.DerivativeInstrumentPartyRole = FIX50SP2.Tags.DerivativeInstrumentPartyRole(required=False)
                    self.DerivativeInstrumentPartySubIDsGrp = FIX50SP2.Components.DerivativeInstrumentPartySubIDsGrp(required=False)

        class UnderlyingLegInstrument(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.UnderlyingLegSymbol = FIX50SP2.Tags.UnderlyingLegSymbol(required=False)
                self.UnderlyingLegSymbolSfx = FIX50SP2.Tags.UnderlyingLegSymbolSfx(required=False)
                self.UnderlyingLegSecurityID = FIX50SP2.Tags.UnderlyingLegSecurityID(required=False)
                self.UnderlyingLegSecurityIDSource = FIX50SP2.Tags.UnderlyingLegSecurityIDSource(required=False)
                self.UnderlyingLegCFICode = FIX50SP2.Tags.UnderlyingLegCFICode(required=False)
                self.UnderlyingLegSecurityType = FIX50SP2.Tags.UnderlyingLegSecurityType(required=False)
                self.UnderlyingLegSecuritySubType = FIX50SP2.Tags.UnderlyingLegSecuritySubType(required=False)
                self.UnderlyingLegMaturityMonthYear = FIX50SP2.Tags.UnderlyingLegMaturityMonthYear(required=False)
                self.UnderlyingLegMaturityDate = FIX50SP2.Tags.UnderlyingLegMaturityDate(required=False)
                self.UnderlyingLegMaturityTime = FIX50SP2.Tags.UnderlyingLegMaturityTime(required=False)
                self.UnderlyingLegStrikePrice = FIX50SP2.Tags.UnderlyingLegStrikePrice(required=False)
                self.UnderlyingLegOptAttribute = FIX50SP2.Tags.UnderlyingLegOptAttribute(required=False)
                self.UnderlyingLegPutOrCall = FIX50SP2.Tags.UnderlyingLegPutOrCall(required=False)
                self.UnderlyingLegSecurityExchange = FIX50SP2.Tags.UnderlyingLegSecurityExchange(required=False)
                self.UnderlyingLegSecurityDesc = FIX50SP2.Tags.UnderlyingLegSecurityDesc(required=False)
                self.UnderlyingLegSecurityAltIDGrp = FIX50SP2.Components.UnderlyingLegSecurityAltIDGrp(required=False)

        class TradeCapLegUnderlyingsGrp(RepeatingGroup):
            class NoOfLegUnderlyings(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.UnderlyingLegInstrument = FIX50SP2.Components.UnderlyingLegInstrument(required=False)

        class FillsGrp(RepeatingGroup):
            class NoFills(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.FillExecID = FIX50SP2.Tags.FillExecID(required=False)
                    self.FillPx = FIX50SP2.Tags.FillPx(required=False)
                    self.FillQty = FIX50SP2.Tags.FillQty(required=False)
                    self.FillLiquidityInd = FIX50SP2.Tags.FillLiquidityInd(required=False)
                    self.NestedParties4 = FIX50SP2.Components.NestedParties4(required=False)

        class ApplIDRequestGrp(RepeatingGroup):
            class NoApplIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.RefApplID = FIX50SP2.Tags.RefApplID(required=False)
                    self.ApplBegSeqNum = FIX50SP2.Tags.ApplBegSeqNum(required=False)
                    self.ApplEndSeqNum = FIX50SP2.Tags.ApplEndSeqNum(required=False)
                    self.RefApplReqID = FIX50SP2.Tags.RefApplReqID(required=False)
                    self.NestedParties = FIX50SP2.Components.NestedParties(required=False)

        class ApplIDRequestAckGrp(RepeatingGroup):
            class NoApplIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.RefApplID = FIX50SP2.Tags.RefApplID(required=False)
                    self.ApplBegSeqNum = FIX50SP2.Tags.ApplBegSeqNum(required=False)
                    self.ApplEndSeqNum = FIX50SP2.Tags.ApplEndSeqNum(required=False)
                    self.RefApplLastSeqNum = FIX50SP2.Tags.RefApplLastSeqNum(required=False)
                    self.ApplResponseError = FIX50SP2.Tags.ApplResponseError(required=False)
                    self.RefApplReqID = FIX50SP2.Tags.RefApplReqID(required=False)
                    self.NestedParties = FIX50SP2.Components.NestedParties(required=False)

        class NestedParties4(RepeatingGroup):
            class NoNested4PartyIDs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Nested4PartyID = FIX50SP2.Tags.Nested4PartyID(required=False)
                    self.Nested4PartyIDSource = FIX50SP2.Tags.Nested4PartyIDSource(required=False)
                    self.Nested4PartyRole = FIX50SP2.Tags.Nested4PartyRole(required=False)
                    self.NstdPtys4SubGrp = FIX50SP2.Components.NstdPtys4SubGrp(required=False)

        class ComplexEvents(RepeatingGroup):
            class NoComplexEvents(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.ComplexEventType = FIX50SP2.Tags.ComplexEventType(required=False)
                    self.ComplexOptPayoutAmount = FIX50SP2.Tags.ComplexOptPayoutAmount(required=False)
                    self.ComplexEventPrice = FIX50SP2.Tags.ComplexEventPrice(required=False)
                    self.ComplexEventPriceBoundaryMethod = FIX50SP2.Tags.ComplexEventPriceBoundaryMethod(required=False)
                    self.ComplexEventPriceBoundaryPrecision = FIX50SP2.Tags.ComplexEventPriceBoundaryPrecision(required=False)
                    self.ComplexEventPriceTimeType = FIX50SP2.Tags.ComplexEventPriceTimeType(required=False)
                    self.ComplexEventCondition = FIX50SP2.Tags.ComplexEventCondition(required=False)
                    self.ComplexEventDates = FIX50SP2.Components.ComplexEventDates(required=False)

        class ComplexEventDates(RepeatingGroup):
            class NoComplexEventDates(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.ComplexEventStartDate = FIX50SP2.Tags.ComplexEventStartDate(required=False)
                    self.ComplexEventEndDate = FIX50SP2.Tags.ComplexEventEndDate(required=False)
                    self.ComplexEventTimes = FIX50SP2.Components.ComplexEventTimes(required=False)

        class StrmAsgnReqInstrmtGrp(RepeatingGroup):
            class NoRelatedSym(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                    self.MDEntrySize = FIX50SP2.Tags.MDEntrySize(required=False)
                    self.MDStreamID = FIX50SP2.Tags.MDStreamID(required=False)
                    self.Instrument = FIX50SP2.Components.Instrument(required=False)

        class StrmAsgnRptInstrmtGrp(RepeatingGroup):
            class NoRelatedSym(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                    self.StreamAsgnType = FIX50SP2.Tags.StreamAsgnType(required=False)
                    self.MDStreamID = FIX50SP2.Tags.MDStreamID(required=False)
                    self.StreamAsgnRejReason = FIX50SP2.Tags.StreamAsgnRejReason(required=False)
                    self.Text = FIX50SP2.Tags.Text(required=False)
                    self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                    self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                    self.Instrument = FIX50SP2.Components.Instrument(required=False)

        class InstrmtLegIOIGrp(RepeatingGroup):
            class NoLegs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.LegIOIQty = FIX50SP2.Tags.LegIOIQty(required=False)
                    self.InstrumentLeg = FIX50SP2.Components.InstrumentLeg(required=False)
                    self.LegStipulations = FIX50SP2.Components.LegStipulations(required=False)

        class InstrmtStrkPxGrp(RepeatingGroup):
            class NoStrikes(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.PrevClosePx = FIX50SP2.Tags.PrevClosePx(required=False)
                    self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                    self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                    self.Side = FIX50SP2.Tags.Side(required=False)
                    self.Price = FIX50SP2.Tags.Price(required=False)
                    self.Currency = FIX50SP2.Tags.Currency(required=False)
                    self.Text = FIX50SP2.Tags.Text(required=False)
                    self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                    self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                    self.Instrument = FIX50SP2.Components.Instrument(required=True)
                    self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)

        class PosUndInstrmtGrp(RepeatingGroup):
            class NoUnderlyings(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.UnderlyingSettlPrice = FIX50SP2.Tags.UnderlyingSettlPrice(required=False)
                    self.UnderlyingSettlPriceType = FIX50SP2.Tags.UnderlyingSettlPriceType(required=False)
                    self.UnderlyingDeliveryAmount = FIX50SP2.Tags.UnderlyingDeliveryAmount(required=False)
                    self.UnderlyingInstrument = FIX50SP2.Components.UnderlyingInstrument(required=False)
                    self.UnderlyingAmount = FIX50SP2.Components.UnderlyingAmount(required=False)

        class QuotEntryAckGrp(RepeatingGroup):
            class NoQuoteEntries(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.QuoteEntryID = FIX50SP2.Tags.QuoteEntryID(required=False)
                    self.BidPx = FIX50SP2.Tags.BidPx(required=False)
                    self.OfferPx = FIX50SP2.Tags.OfferPx(required=False)
                    self.BidSize = FIX50SP2.Tags.BidSize(required=False)
                    self.OfferSize = FIX50SP2.Tags.OfferSize(required=False)
                    self.ValidUntilTime = FIX50SP2.Tags.ValidUntilTime(required=False)
                    self.BidSpotRate = FIX50SP2.Tags.BidSpotRate(required=False)
                    self.OfferSpotRate = FIX50SP2.Tags.OfferSpotRate(required=False)
                    self.BidForwardPoints = FIX50SP2.Tags.BidForwardPoints(required=False)
                    self.OfferForwardPoints = FIX50SP2.Tags.OfferForwardPoints(required=False)
                    self.MidPx = FIX50SP2.Tags.MidPx(required=False)
                    self.BidYield = FIX50SP2.Tags.BidYield(required=False)
                    self.MidYield = FIX50SP2.Tags.MidYield(required=False)
                    self.OfferYield = FIX50SP2.Tags.OfferYield(required=False)
                    self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                    self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                    self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                    self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                    self.OrdType = FIX50SP2.Tags.OrdType(required=False)
                    self.SettlDate2 = FIX50SP2.Tags.SettlDate2(required=False)
                    self.OrderQty2 = FIX50SP2.Tags.OrderQty2(required=False)
                    self.BidForwardPoints2 = FIX50SP2.Tags.BidForwardPoints2(required=False)
                    self.OfferForwardPoints2 = FIX50SP2.Tags.OfferForwardPoints2(required=False)
                    self.Currency = FIX50SP2.Tags.Currency(required=False)
                    self.QuoteEntryStatus = FIX50SP2.Tags.QuoteEntryStatus(required=False)
                    self.QuoteEntryRejectReason = FIX50SP2.Tags.QuoteEntryRejectReason(required=False)
                    self.BookingType = FIX50SP2.Tags.BookingType(required=False)
                    self.OrderCapacity = FIX50SP2.Tags.OrderCapacity(required=False)
                    self.OrderRestrictions = FIX50SP2.Tags.OrderRestrictions(required=False)
                    self.Instrument = FIX50SP2.Components.Instrument(required=False)
                    self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)

        class QuotEntryGrp(RepeatingGroup):
            class NoQuoteEntries(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.QuoteEntryID = FIX50SP2.Tags.QuoteEntryID(required=True)
                    self.BidPx = FIX50SP2.Tags.BidPx(required=False)
                    self.OfferPx = FIX50SP2.Tags.OfferPx(required=False)
                    self.BidSize = FIX50SP2.Tags.BidSize(required=False)
                    self.OfferSize = FIX50SP2.Tags.OfferSize(required=False)
                    self.ValidUntilTime = FIX50SP2.Tags.ValidUntilTime(required=False)
                    self.BidSpotRate = FIX50SP2.Tags.BidSpotRate(required=False)
                    self.OfferSpotRate = FIX50SP2.Tags.OfferSpotRate(required=False)
                    self.BidForwardPoints = FIX50SP2.Tags.BidForwardPoints(required=False)
                    self.OfferForwardPoints = FIX50SP2.Tags.OfferForwardPoints(required=False)
                    self.MidPx = FIX50SP2.Tags.MidPx(required=False)
                    self.BidYield = FIX50SP2.Tags.BidYield(required=False)
                    self.MidYield = FIX50SP2.Tags.MidYield(required=False)
                    self.OfferYield = FIX50SP2.Tags.OfferYield(required=False)
                    self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                    self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                    self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                    self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                    self.OrdType = FIX50SP2.Tags.OrdType(required=False)
                    self.SettlDate2 = FIX50SP2.Tags.SettlDate2(required=False)
                    self.OrderQty2 = FIX50SP2.Tags.OrderQty2(required=False)
                    self.BidForwardPoints2 = FIX50SP2.Tags.BidForwardPoints2(required=False)
                    self.OfferForwardPoints2 = FIX50SP2.Tags.OfferForwardPoints2(required=False)
                    self.Currency = FIX50SP2.Tags.Currency(required=False)
                    self.BookingType = FIX50SP2.Tags.BookingType(required=False)
                    self.OrderCapacity = FIX50SP2.Tags.OrderCapacity(required=False)
                    self.OrderRestrictions = FIX50SP2.Tags.OrderRestrictions(required=False)
                    self.Instrument = FIX50SP2.Components.Instrument(required=False)
                    self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)

        class QuotSetAckGrp(RepeatingGroup):
            class NoQuoteSets(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.QuoteSetID = FIX50SP2.Tags.QuoteSetID(required=False)
                    self.TotNoQuoteEntries = FIX50SP2.Tags.TotNoQuoteEntries(required=False)
                    self.TotNoCxldQuotes = FIX50SP2.Tags.TotNoCxldQuotes(required=False)
                    self.TotNoAccQuotes = FIX50SP2.Tags.TotNoAccQuotes(required=False)
                    self.TotNoRejQuotes = FIX50SP2.Tags.TotNoRejQuotes(required=False)
                    self.LastFragment = FIX50SP2.Tags.LastFragment(required=False)
                    self.QuoteSetValidUntilTime = FIX50SP2.Tags.QuoteSetValidUntilTime(required=False)
                    self.UnderlyingInstrument = FIX50SP2.Components.UnderlyingInstrument(required=False)
                    self.QuotEntryAckGrp = FIX50SP2.Components.QuotEntryAckGrp(required=False)

        class QuotSetGrp(RepeatingGroup):
            class NoQuoteSets(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.QuoteSetID = FIX50SP2.Tags.QuoteSetID(required=True)
                    self.QuoteSetValidUntilTime = FIX50SP2.Tags.QuoteSetValidUntilTime(required=False)
                    self.TotNoQuoteEntries = FIX50SP2.Tags.TotNoQuoteEntries(required=True)
                    self.LastFragment = FIX50SP2.Tags.LastFragment(required=False)
                    self.UnderlyingInstrument = FIX50SP2.Components.UnderlyingInstrument(required=False)
                    self.QuotEntryGrp = FIX50SP2.Components.QuotEntryGrp(required=True)

        class SettlInstGrp(RepeatingGroup):
            class NoSettlInst(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.SettlInstID = FIX50SP2.Tags.SettlInstID(required=False)
                    self.SettlInstTransType = FIX50SP2.Tags.SettlInstTransType(required=False)
                    self.SettlInstRefID = FIX50SP2.Tags.SettlInstRefID(required=False)
                    self.Side = FIX50SP2.Tags.Side(required=False)
                    self.Product = FIX50SP2.Tags.Product(required=False)
                    self.SecurityType = FIX50SP2.Tags.SecurityType(required=False)
                    self.CFICode = FIX50SP2.Tags.CFICode(required=False)
                    self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                    self.EffectiveTime = FIX50SP2.Tags.EffectiveTime(required=False)
                    self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                    self.LastUpdateTime = FIX50SP2.Tags.LastUpdateTime(required=False)
                    self.PaymentMethod = FIX50SP2.Tags.PaymentMethod(required=False)
                    self.PaymentRef = FIX50SP2.Tags.PaymentRef(required=False)
                    self.CardHolderName = FIX50SP2.Tags.CardHolderName(required=False)
                    self.CardNumber = FIX50SP2.Tags.CardNumber(required=False)
                    self.CardStartDate = FIX50SP2.Tags.CardStartDate(required=False)
                    self.CardExpDate = FIX50SP2.Tags.CardExpDate(required=False)
                    self.CardIssNum = FIX50SP2.Tags.CardIssNum(required=False)
                    self.PaymentDate = FIX50SP2.Tags.PaymentDate(required=False)
                    self.PaymentRemitterID = FIX50SP2.Tags.PaymentRemitterID(required=False)
                    self.Parties = FIX50SP2.Components.Parties(required=False)
                    self.SettlInstructionsData = FIX50SP2.Components.SettlInstructionsData(required=False)

        class SideCrossOrdCxlGrp(RepeatingGroup):
            class NoSides(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Side = FIX50SP2.Tags.Side(required=True)
                    self.OrigClOrdID = FIX50SP2.Tags.OrigClOrdID(required=False)
                    self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=True)
                    self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                    self.ClOrdLinkID = FIX50SP2.Tags.ClOrdLinkID(required=False)
                    self.OrigOrdModTime = FIX50SP2.Tags.OrigOrdModTime(required=False)
                    self.TradeOriginationDate = FIX50SP2.Tags.TradeOriginationDate(required=False)
                    self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                    self.ComplianceID = FIX50SP2.Tags.ComplianceID(required=False)
                    self.Text = FIX50SP2.Tags.Text(required=False)
                    self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                    self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                    self.Parties = FIX50SP2.Components.Parties(required=False)
                    self.OrderQtyData = FIX50SP2.Components.OrderQtyData(required=True)

        class MarketSegmentGrp(RepeatingGroup):
            class NoMarketSegments(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                    self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                    self.SecurityTradingRules = FIX50SP2.Components.SecurityTradingRules(required=False)
                    self.StrikeRules = FIX50SP2.Components.StrikeRules(required=False)

        class TradeReportOrderDetail(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                self.SecondaryOrderID = FIX50SP2.Tags.SecondaryOrderID(required=False)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.ListID = FIX50SP2.Tags.ListID(required=False)
                self.RefOrderID = FIX50SP2.Tags.RefOrderID(required=False)
                self.RefOrderIDSource = FIX50SP2.Tags.RefOrderIDSource(required=False)
                self.RefOrdIDReason = FIX50SP2.Tags.RefOrdIDReason(required=False)
                self.OrdType = FIX50SP2.Tags.OrdType(required=False)
                self.Price = FIX50SP2.Tags.Price(required=False)
                self.StopPx = FIX50SP2.Tags.StopPx(required=False)
                self.ExecInst = FIX50SP2.Tags.ExecInst(required=False)
                self.OrdStatus = FIX50SP2.Tags.OrdStatus(required=False)
                self.LeavesQty = FIX50SP2.Tags.LeavesQty(required=False)
                self.CumQty = FIX50SP2.Tags.CumQty(required=False)
                self.TimeInForce = FIX50SP2.Tags.TimeInForce(required=False)
                self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                self.OrderCapacity = FIX50SP2.Tags.OrderCapacity(required=False)
                self.OrderRestrictions = FIX50SP2.Tags.OrderRestrictions(required=False)
                self.OrigCustOrderCapacity = FIX50SP2.Tags.OrigCustOrderCapacity(required=False)
                self.OrderInputDevice = FIX50SP2.Tags.OrderInputDevice(required=False)
                self.LotType = FIX50SP2.Tags.LotType(required=False)
                self.TransBkdTime = FIX50SP2.Tags.TransBkdTime(required=False)
                self.OrigOrdModTime = FIX50SP2.Tags.OrigOrdModTime(required=False)
                self.BookingType = FIX50SP2.Tags.BookingType(required=False)
                self.OrderQtyData = FIX50SP2.Components.OrderQtyData(required=False)
                self.DisplayInstruction = FIX50SP2.Components.DisplayInstruction(required=False)

        class StrmAsgnReqGrp(RepeatingGroup):
            class NoAsgnReqs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Parties = FIX50SP2.Components.Parties(required=False)
                    self.StrmAsgnReqInstrmtGrp = FIX50SP2.Components.StrmAsgnReqInstrmtGrp(required=False)

        class StrmAsgnRptGrp(RepeatingGroup):
            class NoAsgnReqs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Parties = FIX50SP2.Components.Parties(required=False)
                    self.StrmAsgnRptInstrmtGrp = FIX50SP2.Components.StrmAsgnRptInstrmtGrp(required=False)

        class UnderlyingInstrument(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.UnderlyingSymbol = FIX50SP2.Tags.UnderlyingSymbol(required=False)
                self.UnderlyingSymbolSfx = FIX50SP2.Tags.UnderlyingSymbolSfx(required=False)
                self.UnderlyingSecurityID = FIX50SP2.Tags.UnderlyingSecurityID(required=False)
                self.UnderlyingSecurityIDSource = FIX50SP2.Tags.UnderlyingSecurityIDSource(required=False)
                self.UnderlyingProduct = FIX50SP2.Tags.UnderlyingProduct(required=False)
                self.UnderlyingCFICode = FIX50SP2.Tags.UnderlyingCFICode(required=False)
                self.UnderlyingSecurityType = FIX50SP2.Tags.UnderlyingSecurityType(required=False)
                self.UnderlyingSecuritySubType = FIX50SP2.Tags.UnderlyingSecuritySubType(required=False)
                self.UnderlyingMaturityMonthYear = FIX50SP2.Tags.UnderlyingMaturityMonthYear(required=False)
                self.UnderlyingMaturityDate = FIX50SP2.Tags.UnderlyingMaturityDate(required=False)
                self.UnderlyingMaturityTime = FIX50SP2.Tags.UnderlyingMaturityTime(required=False)
                self.UnderlyingCouponPaymentDate = FIX50SP2.Tags.UnderlyingCouponPaymentDate(required=False)
                self.UnderlyingIssueDate = FIX50SP2.Tags.UnderlyingIssueDate(required=False)
                self.UnderlyingRepoCollateralSecurityType = FIX50SP2.Tags.UnderlyingRepoCollateralSecurityType(required=False)
                self.UnderlyingRepurchaseTerm = FIX50SP2.Tags.UnderlyingRepurchaseTerm(required=False)
                self.UnderlyingRepurchaseRate = FIX50SP2.Tags.UnderlyingRepurchaseRate(required=False)
                self.UnderlyingFactor = FIX50SP2.Tags.UnderlyingFactor(required=False)
                self.UnderlyingCreditRating = FIX50SP2.Tags.UnderlyingCreditRating(required=False)
                self.UnderlyingInstrRegistry = FIX50SP2.Tags.UnderlyingInstrRegistry(required=False)
                self.UnderlyingCountryOfIssue = FIX50SP2.Tags.UnderlyingCountryOfIssue(required=False)
                self.UnderlyingStateOrProvinceOfIssue = FIX50SP2.Tags.UnderlyingStateOrProvinceOfIssue(required=False)
                self.UnderlyingLocaleOfIssue = FIX50SP2.Tags.UnderlyingLocaleOfIssue(required=False)
                self.UnderlyingRedemptionDate = FIX50SP2.Tags.UnderlyingRedemptionDate(required=False)
                self.UnderlyingStrikePrice = FIX50SP2.Tags.UnderlyingStrikePrice(required=False)
                self.UnderlyingStrikeCurrency = FIX50SP2.Tags.UnderlyingStrikeCurrency(required=False)
                self.UnderlyingOptAttribute = FIX50SP2.Tags.UnderlyingOptAttribute(required=False)
                self.UnderlyingContractMultiplier = FIX50SP2.Tags.UnderlyingContractMultiplier(required=False)
                self.UnderlyingUnitOfMeasure = FIX50SP2.Tags.UnderlyingUnitOfMeasure(required=False)
                self.UnderlyingUnitOfMeasureQty = FIX50SP2.Tags.UnderlyingUnitOfMeasureQty(required=False)
                self.UnderlyingPriceUnitOfMeasure = FIX50SP2.Tags.UnderlyingPriceUnitOfMeasure(required=False)
                self.UnderlyingPriceUnitOfMeasureQty = FIX50SP2.Tags.UnderlyingPriceUnitOfMeasureQty(required=False)
                self.UnderlyingTimeUnit = FIX50SP2.Tags.UnderlyingTimeUnit(required=False)
                self.UnderlyingExerciseStyle = FIX50SP2.Tags.UnderlyingExerciseStyle(required=False)
                self.UnderlyingCouponRate = FIX50SP2.Tags.UnderlyingCouponRate(required=False)
                self.UnderlyingSecurityExchange = FIX50SP2.Tags.UnderlyingSecurityExchange(required=False)
                self.UnderlyingIssuer = FIX50SP2.Tags.UnderlyingIssuer(required=False)
                self.EncodedUnderlyingIssuerLen = FIX50SP2.Tags.EncodedUnderlyingIssuerLen(required=False)
                self.EncodedUnderlyingIssuer = FIX50SP2.Tags.EncodedUnderlyingIssuer(required=False)
                self.UnderlyingSecurityDesc = FIX50SP2.Tags.UnderlyingSecurityDesc(required=False)
                self.EncodedUnderlyingSecurityDescLen = FIX50SP2.Tags.EncodedUnderlyingSecurityDescLen(required=False)
                self.EncodedUnderlyingSecurityDesc = FIX50SP2.Tags.EncodedUnderlyingSecurityDesc(required=False)
                self.UnderlyingCPProgram = FIX50SP2.Tags.UnderlyingCPProgram(required=False)
                self.UnderlyingCPRegType = FIX50SP2.Tags.UnderlyingCPRegType(required=False)
                self.UnderlyingAllocationPercent = FIX50SP2.Tags.UnderlyingAllocationPercent(required=False)
                self.UnderlyingCurrency = FIX50SP2.Tags.UnderlyingCurrency(required=False)
                self.UnderlyingQty = FIX50SP2.Tags.UnderlyingQty(required=False)
                self.UnderlyingSettlementType = FIX50SP2.Tags.UnderlyingSettlementType(required=False)
                self.UnderlyingCashAmount = FIX50SP2.Tags.UnderlyingCashAmount(required=False)
                self.UnderlyingCashType = FIX50SP2.Tags.UnderlyingCashType(required=False)
                self.UnderlyingPx = FIX50SP2.Tags.UnderlyingPx(required=False)
                self.UnderlyingDirtyPrice = FIX50SP2.Tags.UnderlyingDirtyPrice(required=False)
                self.UnderlyingEndPrice = FIX50SP2.Tags.UnderlyingEndPrice(required=False)
                self.UnderlyingStartValue = FIX50SP2.Tags.UnderlyingStartValue(required=False)
                self.UnderlyingCurrentValue = FIX50SP2.Tags.UnderlyingCurrentValue(required=False)
                self.UnderlyingEndValue = FIX50SP2.Tags.UnderlyingEndValue(required=False)
                self.UnderlyingAdjustedQuantity = FIX50SP2.Tags.UnderlyingAdjustedQuantity(required=False)
                self.UnderlyingFXRate = FIX50SP2.Tags.UnderlyingFXRate(required=False)
                self.UnderlyingFXRateCalc = FIX50SP2.Tags.UnderlyingFXRateCalc(required=False)
                self.UnderlyingCapValue = FIX50SP2.Tags.UnderlyingCapValue(required=False)
                self.UnderlyingSettlMethod = FIX50SP2.Tags.UnderlyingSettlMethod(required=False)
                self.UnderlyingPutOrCall = FIX50SP2.Tags.UnderlyingPutOrCall(required=False)
                self.UnderlyingContractMultiplierUnit = FIX50SP2.Tags.UnderlyingContractMultiplierUnit(required=False)
                self.UnderlyingFlowScheduleType = FIX50SP2.Tags.UnderlyingFlowScheduleType(required=False)
                self.UnderlyingRestructuringType = FIX50SP2.Tags.UnderlyingRestructuringType(required=False)
                self.UnderlyingSeniority = FIX50SP2.Tags.UnderlyingSeniority(required=False)
                self.UnderlyingNotionalPercentageOutstanding = FIX50SP2.Tags.UnderlyingNotionalPercentageOutstanding(required=False)
                self.UnderlyingOriginalNotionalPercentageOutstanding = FIX50SP2.Tags.UnderlyingOriginalNotionalPercentageOutstanding(required=False)
                self.UnderlyingAttachmentPoint = FIX50SP2.Tags.UnderlyingAttachmentPoint(required=False)
                self.UnderlyingDetachmentPoint = FIX50SP2.Tags.UnderlyingDetachmentPoint(required=False)
                self.UndSecAltIDGrp = FIX50SP2.Components.UndSecAltIDGrp(required=False)
                self.UnderlyingStipulations = FIX50SP2.Components.UnderlyingStipulations(required=False)
                self.UndlyInstrumentParties = FIX50SP2.Components.UndlyInstrumentParties(required=False)

        class InstrmtLegSecListGrp(RepeatingGroup):
            class NoLegs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.LegSwapType = FIX50SP2.Tags.LegSwapType(required=False)
                    self.LegSettlType = FIX50SP2.Tags.LegSettlType(required=False)
                    self.InstrumentLeg = FIX50SP2.Components.InstrumentLeg(required=False)
                    self.LegStipulations = FIX50SP2.Components.LegStipulations(required=False)
                    self.LegBenchmarkCurveData = FIX50SP2.Components.LegBenchmarkCurveData(required=False)

        class InstrmtMDReqGrp(RepeatingGroup):
            class NoRelatedSym(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Currency = FIX50SP2.Tags.Currency(required=False)
                    self.QuoteType = FIX50SP2.Tags.QuoteType(required=False)
                    self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                    self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                    self.MDEntrySize = FIX50SP2.Tags.MDEntrySize(required=False)
                    self.MDStreamID = FIX50SP2.Tags.MDStreamID(required=False)
                    self.Instrument = FIX50SP2.Components.Instrument(required=True)
                    self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                    self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)

        class LegQuotStatGrp(RepeatingGroup):
            class NoLegs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.LegQty = FIX50SP2.Tags.LegQty(required=False)
                    self.LegOrderQty = FIX50SP2.Tags.LegOrderQty(required=False)
                    self.LegSwapType = FIX50SP2.Tags.LegSwapType(required=False)
                    self.LegSettlType = FIX50SP2.Tags.LegSettlType(required=False)
                    self.LegSettlDate = FIX50SP2.Tags.LegSettlDate(required=False)
                    self.InstrumentLeg = FIX50SP2.Components.InstrumentLeg(required=False)
                    self.LegStipulations = FIX50SP2.Components.LegStipulations(required=False)
                    self.NestedParties = FIX50SP2.Components.NestedParties(required=False)

        class RFQReqGrp(RepeatingGroup):
            class NoRelatedSym(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.PrevClosePx = FIX50SP2.Tags.PrevClosePx(required=False)
                    self.QuoteRequestType = FIX50SP2.Tags.QuoteRequestType(required=False)
                    self.QuoteType = FIX50SP2.Tags.QuoteType(required=False)
                    self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                    self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                    self.Instrument = FIX50SP2.Components.Instrument(required=True)
                    self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                    self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)

        class SecLstUpdRelSymsLegGrp(RepeatingGroup):
            class NoLegs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.LegSwapType = FIX50SP2.Tags.LegSwapType(required=False)
                    self.LegSettlType = FIX50SP2.Tags.LegSettlType(required=False)
                    self.InstrumentLeg = FIX50SP2.Components.InstrumentLeg(required=False)
                    self.LegStipulations = FIX50SP2.Components.LegStipulations(required=False)
                    self.LegBenchmarkCurveData = FIX50SP2.Components.LegBenchmarkCurveData(required=False)

        class SecurityTradingRules(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.BaseTradingRules = FIX50SP2.Components.BaseTradingRules(required=False)
                self.TradingSessionRulesGrp = FIX50SP2.Components.TradingSessionRulesGrp(required=False)
                self.NestedInstrumentAttribute = FIX50SP2.Components.NestedInstrumentAttribute(required=False)

        class SettlObligationInstructions(RepeatingGroup):
            class NoSettlOblig(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.NetGrossInd = FIX50SP2.Tags.NetGrossInd(required=False)
                    self.SettlObligID = FIX50SP2.Tags.SettlObligID(required=False)
                    self.SettlObligTransType = FIX50SP2.Tags.SettlObligTransType(required=False)
                    self.SettlObligRefID = FIX50SP2.Tags.SettlObligRefID(required=False)
                    self.CcyAmt = FIX50SP2.Tags.CcyAmt(required=False)
                    self.SettlCurrAmt = FIX50SP2.Tags.SettlCurrAmt(required=False)
                    self.Currency = FIX50SP2.Tags.Currency(required=False)
                    self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                    self.SettlCurrFxRate = FIX50SP2.Tags.SettlCurrFxRate(required=False)
                    self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                    self.EffectiveTime = FIX50SP2.Tags.EffectiveTime(required=False)
                    self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                    self.LastUpdateTime = FIX50SP2.Tags.LastUpdateTime(required=False)
                    self.Instrument = FIX50SP2.Components.Instrument(required=False)
                    self.Parties = FIX50SP2.Components.Parties(required=False)
                    self.SettlDetails = FIX50SP2.Components.SettlDetails(required=False)

        class BaseTradingRules(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.ExpirationCycle = FIX50SP2.Tags.ExpirationCycle(required=False)
                self.MinTradeVol = FIX50SP2.Tags.MinTradeVol(required=False)
                self.MaxTradeVol = FIX50SP2.Tags.MaxTradeVol(required=False)
                self.MaxPriceVariation = FIX50SP2.Tags.MaxPriceVariation(required=False)
                self.ImpliedMarketIndicator = FIX50SP2.Tags.ImpliedMarketIndicator(required=False)
                self.TradingCurrency = FIX50SP2.Tags.TradingCurrency(required=False)
                self.RoundLot = FIX50SP2.Tags.RoundLot(required=False)
                self.MultilegModel = FIX50SP2.Tags.MultilegModel(required=False)
                self.MultilegPriceMethod = FIX50SP2.Tags.MultilegPriceMethod(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.TickRules = FIX50SP2.Components.TickRules(required=False)
                self.LotTypeRules = FIX50SP2.Components.LotTypeRules(required=False)
                self.PriceLimits = FIX50SP2.Components.PriceLimits(required=False)

        class DerivativeSecurityDefinition(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.DerivativeInstrument = FIX50SP2.Components.DerivativeInstrument(required=False)
                self.DerivativeInstrumentAttribute = FIX50SP2.Components.DerivativeInstrumentAttribute(required=False)
                self.MarketSegmentGrp = FIX50SP2.Components.MarketSegmentGrp(required=False)

        class InstrmtLegExecGrp(RepeatingGroup):
            class NoLegs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.LegQty = FIX50SP2.Tags.LegQty(required=False)
                    self.LegOrderQty = FIX50SP2.Tags.LegOrderQty(required=False)
                    self.LegSwapType = FIX50SP2.Tags.LegSwapType(required=False)
                    self.LegAllocID = FIX50SP2.Tags.LegAllocID(required=False)
                    self.LegPositionEffect = FIX50SP2.Tags.LegPositionEffect(required=False)
                    self.LegCoveredOrUncovered = FIX50SP2.Tags.LegCoveredOrUncovered(required=False)
                    self.LegRefID = FIX50SP2.Tags.LegRefID(required=False)
                    self.LegSettlType = FIX50SP2.Tags.LegSettlType(required=False)
                    self.LegSettlDate = FIX50SP2.Tags.LegSettlDate(required=False)
                    self.LegLastPx = FIX50SP2.Tags.LegLastPx(required=False)
                    self.LegSettlCurrency = FIX50SP2.Tags.LegSettlCurrency(required=False)
                    self.LegLastForwardPoints = FIX50SP2.Tags.LegLastForwardPoints(required=False)
                    self.LegCalculatedCcyLastQty = FIX50SP2.Tags.LegCalculatedCcyLastQty(required=False)
                    self.LegGrossTradeAmt = FIX50SP2.Tags.LegGrossTradeAmt(required=False)
                    self.LegVolatility = FIX50SP2.Tags.LegVolatility(required=False)
                    self.LegDividendYield = FIX50SP2.Tags.LegDividendYield(required=False)
                    self.LegCurrencyRatio = FIX50SP2.Tags.LegCurrencyRatio(required=False)
                    self.LegExecInst = FIX50SP2.Tags.LegExecInst(required=False)
                    self.LegLastQty = FIX50SP2.Tags.LegLastQty(required=False)
                    self.InstrumentLeg = FIX50SP2.Components.InstrumentLeg(required=False)
                    self.LegStipulations = FIX50SP2.Components.LegStipulations(required=False)
                    self.LegPreAllocGrp = FIX50SP2.Components.LegPreAllocGrp(required=False)
                    self.NestedParties3 = FIX50SP2.Components.NestedParties3(required=False)

        class LegOrdGrp(RepeatingGroup):
            class NoLegs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.LegQty = FIX50SP2.Tags.LegQty(required=False)
                    self.LegSwapType = FIX50SP2.Tags.LegSwapType(required=False)
                    self.LegAllocID = FIX50SP2.Tags.LegAllocID(required=False)
                    self.LegPositionEffect = FIX50SP2.Tags.LegPositionEffect(required=False)
                    self.LegCoveredOrUncovered = FIX50SP2.Tags.LegCoveredOrUncovered(required=False)
                    self.LegRefID = FIX50SP2.Tags.LegRefID(required=False)
                    self.LegSettlType = FIX50SP2.Tags.LegSettlType(required=False)
                    self.LegSettlDate = FIX50SP2.Tags.LegSettlDate(required=False)
                    self.LegSettlCurrency = FIX50SP2.Tags.LegSettlCurrency(required=False)
                    self.LegOrderQty = FIX50SP2.Tags.LegOrderQty(required=False)
                    self.LegVolatility = FIX50SP2.Tags.LegVolatility(required=False)
                    self.LegDividendYield = FIX50SP2.Tags.LegDividendYield(required=False)
                    self.LegCurrencyRatio = FIX50SP2.Tags.LegCurrencyRatio(required=False)
                    self.LegExecInst = FIX50SP2.Tags.LegExecInst(required=False)
                    self.InstrumentLeg = FIX50SP2.Components.InstrumentLeg(required=False)
                    self.LegStipulations = FIX50SP2.Components.LegStipulations(required=False)
                    self.LegPreAllocGrp = FIX50SP2.Components.LegPreAllocGrp(required=False)
                    self.NestedParties = FIX50SP2.Components.NestedParties(required=False)

        class LegQuotGrp(RepeatingGroup):
            class NoLegs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.LegQty = FIX50SP2.Tags.LegQty(required=False)
                    self.LegOrderQty = FIX50SP2.Tags.LegOrderQty(required=False)
                    self.LegSwapType = FIX50SP2.Tags.LegSwapType(required=False)
                    self.LegSettlType = FIX50SP2.Tags.LegSettlType(required=False)
                    self.LegSettlDate = FIX50SP2.Tags.LegSettlDate(required=False)
                    self.LegPriceType = FIX50SP2.Tags.LegPriceType(required=False)
                    self.LegBidPx = FIX50SP2.Tags.LegBidPx(required=False)
                    self.LegOfferPx = FIX50SP2.Tags.LegOfferPx(required=False)
                    self.LegRefID = FIX50SP2.Tags.LegRefID(required=False)
                    self.LegBidForwardPoints = FIX50SP2.Tags.LegBidForwardPoints(required=False)
                    self.LegOfferForwardPoints = FIX50SP2.Tags.LegOfferForwardPoints(required=False)
                    self.InstrumentLeg = FIX50SP2.Components.InstrumentLeg(required=False)
                    self.LegStipulations = FIX50SP2.Components.LegStipulations(required=False)
                    self.NestedParties = FIX50SP2.Components.NestedParties(required=False)
                    self.LegBenchmarkCurveData = FIX50SP2.Components.LegBenchmarkCurveData(required=False)

        class QuotCxlEntriesGrp(RepeatingGroup):
            class NoQuoteEntries(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Instrument = FIX50SP2.Components.Instrument(required=False)
                    self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                    self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                    self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)

        class QuotReqLegsGrp(RepeatingGroup):
            class NoLegs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.LegQty = FIX50SP2.Tags.LegQty(required=False)
                    self.LegOrderQty = FIX50SP2.Tags.LegOrderQty(required=False)
                    self.LegSwapType = FIX50SP2.Tags.LegSwapType(required=False)
                    self.LegSettlType = FIX50SP2.Tags.LegSettlType(required=False)
                    self.LegSettlDate = FIX50SP2.Tags.LegSettlDate(required=False)
                    self.LegRefID = FIX50SP2.Tags.LegRefID(required=False)
                    self.InstrumentLeg = FIX50SP2.Components.InstrumentLeg(required=False)
                    self.LegStipulations = FIX50SP2.Components.LegStipulations(required=False)
                    self.NestedParties = FIX50SP2.Components.NestedParties(required=False)
                    self.LegBenchmarkCurveData = FIX50SP2.Components.LegBenchmarkCurveData(required=False)

        class RelSymDerivSecGrp(RepeatingGroup):
            class NoRelatedSym(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Currency = FIX50SP2.Tags.Currency(required=False)
                    self.CorporateAction = FIX50SP2.Tags.CorporateAction(required=False)
                    self.Text = FIX50SP2.Tags.Text(required=False)
                    self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                    self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                    self.RelSymTransactTime = FIX50SP2.Tags.RelSymTransactTime(required=False)
                    self.Instrument = FIX50SP2.Components.Instrument(required=False)
                    self.SecondaryPriceLimits = FIX50SP2.Components.SecondaryPriceLimits(required=False)
                    self.InstrumentExtension = FIX50SP2.Components.InstrumentExtension(required=False)
                    self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)

        class SideCrossOrdModGrp(RepeatingGroup):
            class NoSides(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Side = FIX50SP2.Tags.Side(required=True)
                    self.OrigClOrdID = FIX50SP2.Tags.OrigClOrdID(required=False)
                    self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=True)
                    self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                    self.ClOrdLinkID = FIX50SP2.Tags.ClOrdLinkID(required=False)
                    self.TradeOriginationDate = FIX50SP2.Tags.TradeOriginationDate(required=False)
                    self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                    self.Account = FIX50SP2.Tags.Account(required=False)
                    self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                    self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                    self.DayBookingInst = FIX50SP2.Tags.DayBookingInst(required=False)
                    self.BookingUnit = FIX50SP2.Tags.BookingUnit(required=False)
                    self.PreallocMethod = FIX50SP2.Tags.PreallocMethod(required=False)
                    self.AllocID = FIX50SP2.Tags.AllocID(required=False)
                    self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                    self.OrderCapacity = FIX50SP2.Tags.OrderCapacity(required=False)
                    self.OrderRestrictions = FIX50SP2.Tags.OrderRestrictions(required=False)
                    self.PreTradeAnonymity = FIX50SP2.Tags.PreTradeAnonymity(required=False)
                    self.CustOrderCapacity = FIX50SP2.Tags.CustOrderCapacity(required=False)
                    self.ForexReq = FIX50SP2.Tags.ForexReq(required=False)
                    self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                    self.BookingType = FIX50SP2.Tags.BookingType(required=False)
                    self.Text = FIX50SP2.Tags.Text(required=False)
                    self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                    self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                    self.PositionEffect = FIX50SP2.Tags.PositionEffect(required=False)
                    self.CoveredOrUncovered = FIX50SP2.Tags.CoveredOrUncovered(required=False)
                    self.CashMargin = FIX50SP2.Tags.CashMargin(required=False)
                    self.ClearingFeeIndicator = FIX50SP2.Tags.ClearingFeeIndicator(required=False)
                    self.SolicitedFlag = FIX50SP2.Tags.SolicitedFlag(required=False)
                    self.SideComplianceID = FIX50SP2.Tags.SideComplianceID(required=False)
                    self.SideTimeInForce = FIX50SP2.Tags.SideTimeInForce(required=False)
                    self.Parties = FIX50SP2.Components.Parties(required=False)
                    self.PreAllocGrp = FIX50SP2.Components.PreAllocGrp(required=False)
                    self.OrderQtyData = FIX50SP2.Components.OrderQtyData(required=True)
                    self.CommissionData = FIX50SP2.Components.CommissionData(required=False)

        class TrdInstrmtLegGrp(RepeatingGroup):
            class NoLegs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.LegQty = FIX50SP2.Tags.LegQty(required=False)
                    self.LegSwapType = FIX50SP2.Tags.LegSwapType(required=False)
                    self.LegReportID = FIX50SP2.Tags.LegReportID(required=False)
                    self.LegNumber = FIX50SP2.Tags.LegNumber(required=False)
                    self.LegPositionEffect = FIX50SP2.Tags.LegPositionEffect(required=False)
                    self.LegCoveredOrUncovered = FIX50SP2.Tags.LegCoveredOrUncovered(required=False)
                    self.LegRefID = FIX50SP2.Tags.LegRefID(required=False)
                    self.LegSettlType = FIX50SP2.Tags.LegSettlType(required=False)
                    self.LegSettlDate = FIX50SP2.Tags.LegSettlDate(required=False)
                    self.LegLastPx = FIX50SP2.Tags.LegLastPx(required=False)
                    self.LegSettlCurrency = FIX50SP2.Tags.LegSettlCurrency(required=False)
                    self.LegLastForwardPoints = FIX50SP2.Tags.LegLastForwardPoints(required=False)
                    self.LegCalculatedCcyLastQty = FIX50SP2.Tags.LegCalculatedCcyLastQty(required=False)
                    self.LegGrossTradeAmt = FIX50SP2.Tags.LegGrossTradeAmt(required=False)
                    self.LegVolatility = FIX50SP2.Tags.LegVolatility(required=False)
                    self.LegDividendYield = FIX50SP2.Tags.LegDividendYield(required=False)
                    self.LegCurrencyRatio = FIX50SP2.Tags.LegCurrencyRatio(required=False)
                    self.LegExecInst = FIX50SP2.Tags.LegExecInst(required=False)
                    self.LegLastQty = FIX50SP2.Tags.LegLastQty(required=False)
                    self.InstrumentLeg = FIX50SP2.Components.InstrumentLeg(required=False)
                    self.LegStipulations = FIX50SP2.Components.LegStipulations(required=False)
                    self.NestedParties = FIX50SP2.Components.NestedParties(required=False)
                    self.TradeCapLegUnderlyingsGrp = FIX50SP2.Components.TradeCapLegUnderlyingsGrp(required=False)

        class DerivativeInstrument(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.DerivativeSymbol = FIX50SP2.Tags.DerivativeSymbol(required=False)
                self.DerivativeSymbolSfx = FIX50SP2.Tags.DerivativeSymbolSfx(required=False)
                self.DerivativeSecurityID = FIX50SP2.Tags.DerivativeSecurityID(required=False)
                self.DerivativeSecurityIDSource = FIX50SP2.Tags.DerivativeSecurityIDSource(required=False)
                self.DerivativeProduct = FIX50SP2.Tags.DerivativeProduct(required=False)
                self.DerivativeProductComplex = FIX50SP2.Tags.DerivativeProductComplex(required=False)
                self.DerivFlexProductEligibilityIndicator = FIX50SP2.Tags.DerivFlexProductEligibilityIndicator(required=False)
                self.DerivativeSecurityGroup = FIX50SP2.Tags.DerivativeSecurityGroup(required=False)
                self.DerivativeCFICode = FIX50SP2.Tags.DerivativeCFICode(required=False)
                self.DerivativeSecurityType = FIX50SP2.Tags.DerivativeSecurityType(required=False)
                self.DerivativeSecuritySubType = FIX50SP2.Tags.DerivativeSecuritySubType(required=False)
                self.DerivativeMaturityMonthYear = FIX50SP2.Tags.DerivativeMaturityMonthYear(required=False)
                self.DerivativeMaturityDate = FIX50SP2.Tags.DerivativeMaturityDate(required=False)
                self.DerivativeMaturityTime = FIX50SP2.Tags.DerivativeMaturityTime(required=False)
                self.DerivativeSettleOnOpenFlag = FIX50SP2.Tags.DerivativeSettleOnOpenFlag(required=False)
                self.DerivativeInstrmtAssignmentMethod = FIX50SP2.Tags.DerivativeInstrmtAssignmentMethod(required=False)
                self.DerivativeSecurityStatus = FIX50SP2.Tags.DerivativeSecurityStatus(required=False)
                self.DerivativeIssueDate = FIX50SP2.Tags.DerivativeIssueDate(required=False)
                self.DerivativeInstrRegistry = FIX50SP2.Tags.DerivativeInstrRegistry(required=False)
                self.DerivativeCountryOfIssue = FIX50SP2.Tags.DerivativeCountryOfIssue(required=False)
                self.DerivativeStateOrProvinceOfIssue = FIX50SP2.Tags.DerivativeStateOrProvinceOfIssue(required=False)
                self.DerivativeLocaleOfIssue = FIX50SP2.Tags.DerivativeLocaleOfIssue(required=False)
                self.DerivativeStrikePrice = FIX50SP2.Tags.DerivativeStrikePrice(required=False)
                self.DerivativeStrikeCurrency = FIX50SP2.Tags.DerivativeStrikeCurrency(required=False)
                self.DerivativeStrikeMultiplier = FIX50SP2.Tags.DerivativeStrikeMultiplier(required=False)
                self.DerivativeStrikeValue = FIX50SP2.Tags.DerivativeStrikeValue(required=False)
                self.DerivativeOptAttribute = FIX50SP2.Tags.DerivativeOptAttribute(required=False)
                self.DerivativeContractMultiplier = FIX50SP2.Tags.DerivativeContractMultiplier(required=False)
                self.DerivativeMinPriceIncrement = FIX50SP2.Tags.DerivativeMinPriceIncrement(required=False)
                self.DerivativeMinPriceIncrementAmount = FIX50SP2.Tags.DerivativeMinPriceIncrementAmount(required=False)
                self.DerivativeUnitOfMeasure = FIX50SP2.Tags.DerivativeUnitOfMeasure(required=False)
                self.DerivativeUnitOfMeasureQty = FIX50SP2.Tags.DerivativeUnitOfMeasureQty(required=False)
                self.DerivativePriceUnitOfMeasure = FIX50SP2.Tags.DerivativePriceUnitOfMeasure(required=False)
                self.DerivativePriceUnitOfMeasureQty = FIX50SP2.Tags.DerivativePriceUnitOfMeasureQty(required=False)
                self.DerivativeSettlMethod = FIX50SP2.Tags.DerivativeSettlMethod(required=False)
                self.DerivativePriceQuoteMethod = FIX50SP2.Tags.DerivativePriceQuoteMethod(required=False)
                self.DerivativeValuationMethod = FIX50SP2.Tags.DerivativeValuationMethod(required=False)
                self.DerivativeListMethod = FIX50SP2.Tags.DerivativeListMethod(required=False)
                self.DerivativeCapPrice = FIX50SP2.Tags.DerivativeCapPrice(required=False)
                self.DerivativeFloorPrice = FIX50SP2.Tags.DerivativeFloorPrice(required=False)
                self.DerivativePutOrCall = FIX50SP2.Tags.DerivativePutOrCall(required=False)
                self.DerivativeExerciseStyle = FIX50SP2.Tags.DerivativeExerciseStyle(required=False)
                self.DerivativeOptPayAmount = FIX50SP2.Tags.DerivativeOptPayAmount(required=False)
                self.DerivativeTimeUnit = FIX50SP2.Tags.DerivativeTimeUnit(required=False)
                self.DerivativeSecurityExchange = FIX50SP2.Tags.DerivativeSecurityExchange(required=False)
                self.DerivativePositionLimit = FIX50SP2.Tags.DerivativePositionLimit(required=False)
                self.DerivativeNTPositionLimit = FIX50SP2.Tags.DerivativeNTPositionLimit(required=False)
                self.DerivativeIssuer = FIX50SP2.Tags.DerivativeIssuer(required=False)
                self.DerivativeEncodedIssuerLen = FIX50SP2.Tags.DerivativeEncodedIssuerLen(required=False)
                self.DerivativeEncodedIssuer = FIX50SP2.Tags.DerivativeEncodedIssuer(required=False)
                self.DerivativeSecurityDesc = FIX50SP2.Tags.DerivativeSecurityDesc(required=False)
                self.DerivativeEncodedSecurityDescLen = FIX50SP2.Tags.DerivativeEncodedSecurityDescLen(required=False)
                self.DerivativeEncodedSecurityDesc = FIX50SP2.Tags.DerivativeEncodedSecurityDesc(required=False)
                self.DerivativeContractSettlMonth = FIX50SP2.Tags.DerivativeContractSettlMonth(required=False)
                self.DerivativeContractMultiplierUnit = FIX50SP2.Tags.DerivativeContractMultiplierUnit(required=False)
                self.DerivativeFlowScheduleType = FIX50SP2.Tags.DerivativeFlowScheduleType(required=False)
                self.DerivativeSecurityAltIDGrp = FIX50SP2.Components.DerivativeSecurityAltIDGrp(required=False)
                self.DerivativeSecurityXML = FIX50SP2.Components.DerivativeSecurityXML(required=False)
                self.DerivativeEventsGrp = FIX50SP2.Components.DerivativeEventsGrp(required=False)
                self.DerivativeInstrumentParties = FIX50SP2.Components.DerivativeInstrumentParties(required=False)

        class RelSymDerivSecUpdGrp(RepeatingGroup):
            class NoRelatedSym(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.ListUpdateAction = FIX50SP2.Tags.ListUpdateAction(required=False)
                    self.CorporateAction = FIX50SP2.Tags.CorporateAction(required=False)
                    self.Currency = FIX50SP2.Tags.Currency(required=False)
                    self.Text = FIX50SP2.Tags.Text(required=False)
                    self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                    self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                    self.RelSymTransactTime = FIX50SP2.Tags.RelSymTransactTime(required=False)
                    self.Instrument = FIX50SP2.Components.Instrument(required=False)
                    self.InstrumentExtension = FIX50SP2.Components.InstrumentExtension(required=False)
                    self.SecondaryPriceLimits = FIX50SP2.Components.SecondaryPriceLimits(required=False)
                    self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)

        class Instrument(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.Symbol = FIX50SP2.Tags.Symbol(required=False)
                self.SymbolSfx = FIX50SP2.Tags.SymbolSfx(required=False)
                self.SecurityID = FIX50SP2.Tags.SecurityID(required=False)
                self.SecurityIDSource = FIX50SP2.Tags.SecurityIDSource(required=False)
                self.Product = FIX50SP2.Tags.Product(required=False)
                self.ProductComplex = FIX50SP2.Tags.ProductComplex(required=False)
                self.SecurityGroup = FIX50SP2.Tags.SecurityGroup(required=False)
                self.CFICode = FIX50SP2.Tags.CFICode(required=False)
                self.SecurityType = FIX50SP2.Tags.SecurityType(required=False)
                self.SecuritySubType = FIX50SP2.Tags.SecuritySubType(required=False)
                self.MaturityMonthYear = FIX50SP2.Tags.MaturityMonthYear(required=False)
                self.MaturityDate = FIX50SP2.Tags.MaturityDate(required=False)
                self.MaturityTime = FIX50SP2.Tags.MaturityTime(required=False)
                self.SettleOnOpenFlag = FIX50SP2.Tags.SettleOnOpenFlag(required=False)
                self.InstrmtAssignmentMethod = FIX50SP2.Tags.InstrmtAssignmentMethod(required=False)
                self.SecurityStatus = FIX50SP2.Tags.SecurityStatus(required=False)
                self.CouponPaymentDate = FIX50SP2.Tags.CouponPaymentDate(required=False)
                self.IssueDate = FIX50SP2.Tags.IssueDate(required=False)
                self.RepoCollateralSecurityType = FIX50SP2.Tags.RepoCollateralSecurityType(required=False)
                self.RepurchaseTerm = FIX50SP2.Tags.RepurchaseTerm(required=False)
                self.RepurchaseRate = FIX50SP2.Tags.RepurchaseRate(required=False)
                self.Factor = FIX50SP2.Tags.Factor(required=False)
                self.CreditRating = FIX50SP2.Tags.CreditRating(required=False)
                self.InstrRegistry = FIX50SP2.Tags.InstrRegistry(required=False)
                self.CountryOfIssue = FIX50SP2.Tags.CountryOfIssue(required=False)
                self.StateOrProvinceOfIssue = FIX50SP2.Tags.StateOrProvinceOfIssue(required=False)
                self.LocaleOfIssue = FIX50SP2.Tags.LocaleOfIssue(required=False)
                self.RedemptionDate = FIX50SP2.Tags.RedemptionDate(required=False)
                self.StrikePrice = FIX50SP2.Tags.StrikePrice(required=False)
                self.StrikeCurrency = FIX50SP2.Tags.StrikeCurrency(required=False)
                self.StrikeMultiplier = FIX50SP2.Tags.StrikeMultiplier(required=False)
                self.StrikeValue = FIX50SP2.Tags.StrikeValue(required=False)
                self.OptAttribute = FIX50SP2.Tags.OptAttribute(required=False)
                self.ContractMultiplier = FIX50SP2.Tags.ContractMultiplier(required=False)
                self.MinPriceIncrement = FIX50SP2.Tags.MinPriceIncrement(required=False)
                self.MinPriceIncrementAmount = FIX50SP2.Tags.MinPriceIncrementAmount(required=False)
                self.UnitOfMeasure = FIX50SP2.Tags.UnitOfMeasure(required=False)
                self.UnitOfMeasureQty = FIX50SP2.Tags.UnitOfMeasureQty(required=False)
                self.PriceUnitOfMeasure = FIX50SP2.Tags.PriceUnitOfMeasure(required=False)
                self.PriceUnitOfMeasureQty = FIX50SP2.Tags.PriceUnitOfMeasureQty(required=False)
                self.SettlMethod = FIX50SP2.Tags.SettlMethod(required=False)
                self.ExerciseStyle = FIX50SP2.Tags.ExerciseStyle(required=False)
                self.OptPayoutAmount = FIX50SP2.Tags.OptPayoutAmount(required=False)
                self.PriceQuoteMethod = FIX50SP2.Tags.PriceQuoteMethod(required=False)
                self.ValuationMethod = FIX50SP2.Tags.ValuationMethod(required=False)
                self.ListMethod = FIX50SP2.Tags.ListMethod(required=False)
                self.CapPrice = FIX50SP2.Tags.CapPrice(required=False)
                self.FloorPrice = FIX50SP2.Tags.FloorPrice(required=False)
                self.PutOrCall = FIX50SP2.Tags.PutOrCall(required=False)
                self.FlexibleIndicator = FIX50SP2.Tags.FlexibleIndicator(required=False)
                self.FlexProductEligibilityIndicator = FIX50SP2.Tags.FlexProductEligibilityIndicator(required=False)
                self.TimeUnit = FIX50SP2.Tags.TimeUnit(required=False)
                self.CouponRate = FIX50SP2.Tags.CouponRate(required=False)
                self.SecurityExchange = FIX50SP2.Tags.SecurityExchange(required=False)
                self.PositionLimit = FIX50SP2.Tags.PositionLimit(required=False)
                self.NTPositionLimit = FIX50SP2.Tags.NTPositionLimit(required=False)
                self.Issuer = FIX50SP2.Tags.Issuer(required=False)
                self.EncodedIssuerLen = FIX50SP2.Tags.EncodedIssuerLen(required=False)
                self.EncodedIssuer = FIX50SP2.Tags.EncodedIssuer(required=False)
                self.SecurityDesc = FIX50SP2.Tags.SecurityDesc(required=False)
                self.EncodedSecurityDescLen = FIX50SP2.Tags.EncodedSecurityDescLen(required=False)
                self.EncodedSecurityDesc = FIX50SP2.Tags.EncodedSecurityDesc(required=False)
                self.Pool = FIX50SP2.Tags.Pool(required=False)
                self.ContractSettlMonth = FIX50SP2.Tags.ContractSettlMonth(required=False)
                self.CPProgram = FIX50SP2.Tags.CPProgram(required=False)
                self.CPRegType = FIX50SP2.Tags.CPRegType(required=False)
                self.DatedDate = FIX50SP2.Tags.DatedDate(required=False)
                self.InterestAccrualDate = FIX50SP2.Tags.InterestAccrualDate(required=False)
                self.ContractMultiplierUnit = FIX50SP2.Tags.ContractMultiplierUnit(required=False)
                self.FlowScheduleType = FIX50SP2.Tags.FlowScheduleType(required=False)
                self.RestructuringType = FIX50SP2.Tags.RestructuringType(required=False)
                self.Seniority = FIX50SP2.Tags.Seniority(required=False)
                self.NotionalPercentageOutstanding = FIX50SP2.Tags.NotionalPercentageOutstanding(required=False)
                self.OriginalNotionalPercentageOutstanding = FIX50SP2.Tags.OriginalNotionalPercentageOutstanding(required=False)
                self.AttachmentPoint = FIX50SP2.Tags.AttachmentPoint(required=False)
                self.DetachmentPoint = FIX50SP2.Tags.DetachmentPoint(required=False)
                self.StrikePriceDeterminationMethod = FIX50SP2.Tags.StrikePriceDeterminationMethod(required=False)
                self.StrikePriceBoundaryMethod = FIX50SP2.Tags.StrikePriceBoundaryMethod(required=False)
                self.StrikePriceBoundaryPrecision = FIX50SP2.Tags.StrikePriceBoundaryPrecision(required=False)
                self.UnderlyingPriceDeterminationMethod = FIX50SP2.Tags.UnderlyingPriceDeterminationMethod(required=False)
                self.OptPayoutType = FIX50SP2.Tags.OptPayoutType(required=False)
                self.SecAltIDGrp = FIX50SP2.Components.SecAltIDGrp(required=False)
                self.SecurityXML = FIX50SP2.Components.SecurityXML(required=False)
                self.EvntGrp = FIX50SP2.Components.EvntGrp(required=False)
                self.InstrumentParties = FIX50SP2.Components.InstrumentParties(required=False)
                self.ComplexEvents = FIX50SP2.Components.ComplexEvents(required=False)

        class AllocGrp(RepeatingGroup):
            class NoAllocs(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.AllocAccount = FIX50SP2.Tags.AllocAccount(required=False)
                    self.AllocAcctIDSource = FIX50SP2.Tags.AllocAcctIDSource(required=False)
                    self.MatchStatus = FIX50SP2.Tags.MatchStatus(required=False)
                    self.AllocPrice = FIX50SP2.Tags.AllocPrice(required=False)
                    self.AllocQty = FIX50SP2.Tags.AllocQty(required=False)
                    self.IndividualAllocID = FIX50SP2.Tags.IndividualAllocID(required=False)
                    self.ProcessCode = FIX50SP2.Tags.ProcessCode(required=False)
                    self.SecondaryIndividualAllocID = FIX50SP2.Tags.SecondaryIndividualAllocID(required=False)
                    self.AllocMethod = FIX50SP2.Tags.AllocMethod(required=False)
                    self.AllocCustomerCapacity = FIX50SP2.Tags.AllocCustomerCapacity(required=False)
                    self.AllocPositionEffect = FIX50SP2.Tags.AllocPositionEffect(required=False)
                    self.IndividualAllocType = FIX50SP2.Tags.IndividualAllocType(required=False)
                    self.NotifyBrokerOfCredit = FIX50SP2.Tags.NotifyBrokerOfCredit(required=False)
                    self.AllocHandlInst = FIX50SP2.Tags.AllocHandlInst(required=False)
                    self.AllocText = FIX50SP2.Tags.AllocText(required=False)
                    self.EncodedAllocTextLen = FIX50SP2.Tags.EncodedAllocTextLen(required=False)
                    self.EncodedAllocText = FIX50SP2.Tags.EncodedAllocText(required=False)
                    self.AllocAvgPx = FIX50SP2.Tags.AllocAvgPx(required=False)
                    self.AllocNetMoney = FIX50SP2.Tags.AllocNetMoney(required=False)
                    self.SettlCurrAmt = FIX50SP2.Tags.SettlCurrAmt(required=False)
                    self.AllocSettlCurrAmt = FIX50SP2.Tags.AllocSettlCurrAmt(required=False)
                    self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                    self.AllocSettlCurrency = FIX50SP2.Tags.AllocSettlCurrency(required=False)
                    self.SettlCurrFxRate = FIX50SP2.Tags.SettlCurrFxRate(required=False)
                    self.SettlCurrFxRateCalc = FIX50SP2.Tags.SettlCurrFxRateCalc(required=False)
                    self.AllocAccruedInterestAmt = FIX50SP2.Tags.AllocAccruedInterestAmt(required=False)
                    self.AllocInterestAtMaturity = FIX50SP2.Tags.AllocInterestAtMaturity(required=False)
                    self.ClearingFeeIndicator = FIX50SP2.Tags.ClearingFeeIndicator(required=False)
                    self.AllocSettlInstType = FIX50SP2.Tags.AllocSettlInstType(required=False)
                    self.NestedParties = FIX50SP2.Components.NestedParties(required=False)
                    self.CommissionData = FIX50SP2.Components.CommissionData(required=False)
                    self.MiscFeesGrp = FIX50SP2.Components.MiscFeesGrp(required=False)
                    self.ClrInstGrp = FIX50SP2.Components.ClrInstGrp(required=False)
                    self.SettlInstructionsData = FIX50SP2.Components.SettlInstructionsData(required=False)

        class MDFullGrp(RepeatingGroup):
            class NoMDEntries(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.MDEntryType = FIX50SP2.Tags.MDEntryType(required=True)
                    self.MDEntryID = FIX50SP2.Tags.MDEntryID(required=False)
                    self.MDEntryPx = FIX50SP2.Tags.MDEntryPx(required=False)
                    self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                    self.OrdType = FIX50SP2.Tags.OrdType(required=False)
                    self.Currency = FIX50SP2.Tags.Currency(required=False)
                    self.MDEntrySize = FIX50SP2.Tags.MDEntrySize(required=False)
                    self.LotType = FIX50SP2.Tags.LotType(required=False)
                    self.MDEntryDate = FIX50SP2.Tags.MDEntryDate(required=False)
                    self.MDEntryTime = FIX50SP2.Tags.MDEntryTime(required=False)
                    self.TickDirection = FIX50SP2.Tags.TickDirection(required=False)
                    self.MDMkt = FIX50SP2.Tags.MDMkt(required=False)
                    self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                    self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                    self.SecurityTradingStatus = FIX50SP2.Tags.SecurityTradingStatus(required=False)
                    self.HaltReasonInt = FIX50SP2.Tags.HaltReasonInt(required=False)
                    self.QuoteCondition = FIX50SP2.Tags.QuoteCondition(required=False)
                    self.TradeCondition = FIX50SP2.Tags.TradeCondition(required=False)
                    self.MDEntryOriginator = FIX50SP2.Tags.MDEntryOriginator(required=False)
                    self.LocationID = FIX50SP2.Tags.LocationID(required=False)
                    self.DeskID = FIX50SP2.Tags.DeskID(required=False)
                    self.OpenCloseSettlFlag = FIX50SP2.Tags.OpenCloseSettlFlag(required=False)
                    self.TimeInForce = FIX50SP2.Tags.TimeInForce(required=False)
                    self.ExpireDate = FIX50SP2.Tags.ExpireDate(required=False)
                    self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                    self.MinQty = FIX50SP2.Tags.MinQty(required=False)
                    self.ExecInst = FIX50SP2.Tags.ExecInst(required=False)
                    self.SellerDays = FIX50SP2.Tags.SellerDays(required=False)
                    self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                    self.SecondaryOrderID = FIX50SP2.Tags.SecondaryOrderID(required=False)
                    self.QuoteEntryID = FIX50SP2.Tags.QuoteEntryID(required=False)
                    self.MDEntryBuyer = FIX50SP2.Tags.MDEntryBuyer(required=False)
                    self.MDEntrySeller = FIX50SP2.Tags.MDEntrySeller(required=False)
                    self.NumberOfOrders = FIX50SP2.Tags.NumberOfOrders(required=False)
                    self.MDEntryPositionNo = FIX50SP2.Tags.MDEntryPositionNo(required=False)
                    self.Scope = FIX50SP2.Tags.Scope(required=False)
                    self.PriceDelta = FIX50SP2.Tags.PriceDelta(required=False)
                    self.Text = FIX50SP2.Tags.Text(required=False)
                    self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                    self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                    self.MDPriceLevel = FIX50SP2.Tags.MDPriceLevel(required=False)
                    self.OrderCapacity = FIX50SP2.Tags.OrderCapacity(required=False)
                    self.MDOriginType = FIX50SP2.Tags.MDOriginType(required=False)
                    self.HighPx = FIX50SP2.Tags.HighPx(required=False)
                    self.LowPx = FIX50SP2.Tags.LowPx(required=False)
                    self.TradeVolume = FIX50SP2.Tags.TradeVolume(required=False)
                    self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                    self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                    self.MDQuoteType = FIX50SP2.Tags.MDQuoteType(required=False)
                    self.RptSeq = FIX50SP2.Tags.RptSeq(required=False)
                    self.DealingCapacity = FIX50SP2.Tags.DealingCapacity(required=False)
                    self.MDEntrySpotRate = FIX50SP2.Tags.MDEntrySpotRate(required=False)
                    self.MDEntryForwardPoints = FIX50SP2.Tags.MDEntryForwardPoints(required=False)
                    self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                    self.TrdType = FIX50SP2.Tags.TrdType(required=False)
                    self.FirstPx = FIX50SP2.Tags.FirstPx(required=False)
                    self.LastPx = FIX50SP2.Tags.LastPx(required=False)
                    self.YieldData = FIX50SP2.Components.YieldData(required=False)
                    self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                    self.SecSizesGrp = FIX50SP2.Components.SecSizesGrp(required=False)
                    self.Parties = FIX50SP2.Components.Parties(required=False)
                    self.RateSource = FIX50SP2.Components.RateSource(required=False)

        class TradingSessionRules(Component):
            def __init__(self, required=False):
                Component.__init__(self, required=required)
                self.OrdTypeRules = FIX50SP2.Components.OrdTypeRules(required=False)
                self.TimeInForceRules = FIX50SP2.Components.TimeInForceRules(required=False)
                self.ExecInstRules = FIX50SP2.Components.ExecInstRules(required=False)
                self.MatchRules = FIX50SP2.Components.MatchRules(required=False)
                self.MarketDataFeedTypes = FIX50SP2.Components.MarketDataFeedTypes(required=False)

        class MDIncGrp(RepeatingGroup):
            class NoMDEntries(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.MDUpdateAction = FIX50SP2.Tags.MDUpdateAction(required=True)
                    self.DeleteReason = FIX50SP2.Tags.DeleteReason(required=False)
                    self.MDSubBookType = FIX50SP2.Tags.MDSubBookType(required=False)
                    self.MarketDepth = FIX50SP2.Tags.MarketDepth(required=False)
                    self.MDEntryType = FIX50SP2.Tags.MDEntryType(required=False)
                    self.MDEntryID = FIX50SP2.Tags.MDEntryID(required=False)
                    self.MDEntryRefID = FIX50SP2.Tags.MDEntryRefID(required=False)
                    self.FinancialStatus = FIX50SP2.Tags.FinancialStatus(required=False)
                    self.CorporateAction = FIX50SP2.Tags.CorporateAction(required=False)
                    self.MDEntryPx = FIX50SP2.Tags.MDEntryPx(required=False)
                    self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                    self.OrdType = FIX50SP2.Tags.OrdType(required=False)
                    self.Currency = FIX50SP2.Tags.Currency(required=False)
                    self.MDEntrySize = FIX50SP2.Tags.MDEntrySize(required=False)
                    self.LotType = FIX50SP2.Tags.LotType(required=False)
                    self.MDEntryDate = FIX50SP2.Tags.MDEntryDate(required=False)
                    self.MDEntryTime = FIX50SP2.Tags.MDEntryTime(required=False)
                    self.TickDirection = FIX50SP2.Tags.TickDirection(required=False)
                    self.MDMkt = FIX50SP2.Tags.MDMkt(required=False)
                    self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                    self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                    self.SecurityTradingStatus = FIX50SP2.Tags.SecurityTradingStatus(required=False)
                    self.HaltReasonInt = FIX50SP2.Tags.HaltReasonInt(required=False)
                    self.QuoteCondition = FIX50SP2.Tags.QuoteCondition(required=False)
                    self.TradeCondition = FIX50SP2.Tags.TradeCondition(required=False)
                    self.TrdType = FIX50SP2.Tags.TrdType(required=False)
                    self.MatchType = FIX50SP2.Tags.MatchType(required=False)
                    self.MDEntryOriginator = FIX50SP2.Tags.MDEntryOriginator(required=False)
                    self.LocationID = FIX50SP2.Tags.LocationID(required=False)
                    self.DeskID = FIX50SP2.Tags.DeskID(required=False)
                    self.OpenCloseSettlFlag = FIX50SP2.Tags.OpenCloseSettlFlag(required=False)
                    self.TimeInForce = FIX50SP2.Tags.TimeInForce(required=False)
                    self.ExpireDate = FIX50SP2.Tags.ExpireDate(required=False)
                    self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                    self.MinQty = FIX50SP2.Tags.MinQty(required=False)
                    self.ExecInst = FIX50SP2.Tags.ExecInst(required=False)
                    self.SellerDays = FIX50SP2.Tags.SellerDays(required=False)
                    self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                    self.SecondaryOrderID = FIX50SP2.Tags.SecondaryOrderID(required=False)
                    self.QuoteEntryID = FIX50SP2.Tags.QuoteEntryID(required=False)
                    self.TradeID = FIX50SP2.Tags.TradeID(required=False)
                    self.MDEntryBuyer = FIX50SP2.Tags.MDEntryBuyer(required=False)
                    self.MDEntrySeller = FIX50SP2.Tags.MDEntrySeller(required=False)
                    self.NumberOfOrders = FIX50SP2.Tags.NumberOfOrders(required=False)
                    self.MDEntryPositionNo = FIX50SP2.Tags.MDEntryPositionNo(required=False)
                    self.Scope = FIX50SP2.Tags.Scope(required=False)
                    self.PriceDelta = FIX50SP2.Tags.PriceDelta(required=False)
                    self.NetChgPrevDay = FIX50SP2.Tags.NetChgPrevDay(required=False)
                    self.Text = FIX50SP2.Tags.Text(required=False)
                    self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                    self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                    self.MDPriceLevel = FIX50SP2.Tags.MDPriceLevel(required=False)
                    self.OrderCapacity = FIX50SP2.Tags.OrderCapacity(required=False)
                    self.MDOriginType = FIX50SP2.Tags.MDOriginType(required=False)
                    self.HighPx = FIX50SP2.Tags.HighPx(required=False)
                    self.LowPx = FIX50SP2.Tags.LowPx(required=False)
                    self.TradeVolume = FIX50SP2.Tags.TradeVolume(required=False)
                    self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                    self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                    self.TransBkdTime = FIX50SP2.Tags.TransBkdTime(required=False)
                    self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                    self.MDQuoteType = FIX50SP2.Tags.MDQuoteType(required=False)
                    self.RptSeq = FIX50SP2.Tags.RptSeq(required=False)
                    self.DealingCapacity = FIX50SP2.Tags.DealingCapacity(required=False)
                    self.MDEntrySpotRate = FIX50SP2.Tags.MDEntrySpotRate(required=False)
                    self.MDEntryForwardPoints = FIX50SP2.Tags.MDEntryForwardPoints(required=False)
                    self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                    self.FirstPx = FIX50SP2.Tags.FirstPx(required=False)
                    self.LastPx = FIX50SP2.Tags.LastPx(required=False)
                    self.MDStreamID = FIX50SP2.Tags.MDStreamID(required=False)
                    self.Instrument = FIX50SP2.Components.Instrument(required=False)
                    self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                    self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                    self.YieldData = FIX50SP2.Components.YieldData(required=False)
                    self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                    self.SecSizesGrp = FIX50SP2.Components.SecSizesGrp(required=False)
                    self.StatsIndGrp = FIX50SP2.Components.StatsIndGrp(required=False)
                    self.Parties = FIX50SP2.Components.Parties(required=False)
                    self.RateSource = FIX50SP2.Components.RateSource(required=False)

        class QuotReqRjctGrp(RepeatingGroup):
            class NoRelatedSym(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.PrevClosePx = FIX50SP2.Tags.PrevClosePx(required=False)
                    self.QuoteRequestType = FIX50SP2.Tags.QuoteRequestType(required=False)
                    self.QuoteType = FIX50SP2.Tags.QuoteType(required=False)
                    self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                    self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                    self.TradeOriginationDate = FIX50SP2.Tags.TradeOriginationDate(required=False)
                    self.Side = FIX50SP2.Tags.Side(required=False)
                    self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                    self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                    self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                    self.SettlDate2 = FIX50SP2.Tags.SettlDate2(required=False)
                    self.OrderQty2 = FIX50SP2.Tags.OrderQty2(required=False)
                    self.Currency = FIX50SP2.Tags.Currency(required=False)
                    self.Account = FIX50SP2.Tags.Account(required=False)
                    self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                    self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                    self.QuotePriceType = FIX50SP2.Tags.QuotePriceType(required=False)
                    self.OrdType = FIX50SP2.Tags.OrdType(required=False)
                    self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                    self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                    self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                    self.Price = FIX50SP2.Tags.Price(required=False)
                    self.Price2 = FIX50SP2.Tags.Price2(required=False)
                    self.Instrument = FIX50SP2.Components.Instrument(required=True)
                    self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                    self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                    self.OrderQtyData = FIX50SP2.Components.OrderQtyData(required=False)
                    self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                    self.QuotReqLegsGrp = FIX50SP2.Components.QuotReqLegsGrp(required=False)
                    self.QuotQualGrp = FIX50SP2.Components.QuotQualGrp(required=False)
                    self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                    self.YieldData = FIX50SP2.Components.YieldData(required=False)
                    self.Parties = FIX50SP2.Components.Parties(required=False)

        class SecListGrp(RepeatingGroup):
            class NoRelatedSym(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Currency = FIX50SP2.Tags.Currency(required=False)
                    self.Text = FIX50SP2.Tags.Text(required=False)
                    self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                    self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                    self.RelSymTransactTime = FIX50SP2.Tags.RelSymTransactTime(required=False)
                    self.Instrument = FIX50SP2.Components.Instrument(required=False)
                    self.InstrumentExtension = FIX50SP2.Components.InstrumentExtension(required=False)
                    self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                    self.SecurityTradingRules = FIX50SP2.Components.SecurityTradingRules(required=False)
                    self.StrikeRules = FIX50SP2.Components.StrikeRules(required=False)
                    self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                    self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                    self.InstrmtLegSecListGrp = FIX50SP2.Components.InstrmtLegSecListGrp(required=False)
                    self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                    self.YieldData = FIX50SP2.Components.YieldData(required=False)

        class TrdCapRptSideGrp(RepeatingGroup):
            class NoSides(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Side = FIX50SP2.Tags.Side(required=True)
                    self.SideLastQty = FIX50SP2.Tags.SideLastQty(required=False)
                    self.SideTradeReportID = FIX50SP2.Tags.SideTradeReportID(required=False)
                    self.SideFillStationCd = FIX50SP2.Tags.SideFillStationCd(required=False)
                    self.SideReasonCd = FIX50SP2.Tags.SideReasonCd(required=False)
                    self.RptSeq = FIX50SP2.Tags.RptSeq(required=False)
                    self.SideTrdSubTyp = FIX50SP2.Tags.SideTrdSubTyp(required=False)
                    self.NetGrossInd = FIX50SP2.Tags.NetGrossInd(required=False)
                    self.SideCurrency = FIX50SP2.Tags.SideCurrency(required=False)
                    self.SideSettlCurrency = FIX50SP2.Tags.SideSettlCurrency(required=False)
                    self.Account = FIX50SP2.Tags.Account(required=False)
                    self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                    self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                    self.ProcessCode = FIX50SP2.Tags.ProcessCode(required=False)
                    self.OddLot = FIX50SP2.Tags.OddLot(required=False)
                    self.TradeInputSource = FIX50SP2.Tags.TradeInputSource(required=False)
                    self.TradeInputDevice = FIX50SP2.Tags.TradeInputDevice(required=False)
                    self.ComplianceID = FIX50SP2.Tags.ComplianceID(required=False)
                    self.SolicitedFlag = FIX50SP2.Tags.SolicitedFlag(required=False)
                    self.CustOrderCapacity = FIX50SP2.Tags.CustOrderCapacity(required=False)
                    self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                    self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                    self.TimeBracket = FIX50SP2.Tags.TimeBracket(required=False)
                    self.NumDaysInterest = FIX50SP2.Tags.NumDaysInterest(required=False)
                    self.ExDate = FIX50SP2.Tags.ExDate(required=False)
                    self.AccruedInterestRate = FIX50SP2.Tags.AccruedInterestRate(required=False)
                    self.AccruedInterestAmt = FIX50SP2.Tags.AccruedInterestAmt(required=False)
                    self.InterestAtMaturity = FIX50SP2.Tags.InterestAtMaturity(required=False)
                    self.EndAccruedInterestAmt = FIX50SP2.Tags.EndAccruedInterestAmt(required=False)
                    self.StartCash = FIX50SP2.Tags.StartCash(required=False)
                    self.EndCash = FIX50SP2.Tags.EndCash(required=False)
                    self.Concession = FIX50SP2.Tags.Concession(required=False)
                    self.TotalTakedown = FIX50SP2.Tags.TotalTakedown(required=False)
                    self.NetMoney = FIX50SP2.Tags.NetMoney(required=False)
                    self.SettlCurrAmt = FIX50SP2.Tags.SettlCurrAmt(required=False)
                    self.SettlCurrFxRate = FIX50SP2.Tags.SettlCurrFxRate(required=False)
                    self.SettlCurrFxRateCalc = FIX50SP2.Tags.SettlCurrFxRateCalc(required=False)
                    self.PositionEffect = FIX50SP2.Tags.PositionEffect(required=False)
                    self.Text = FIX50SP2.Tags.Text(required=False)
                    self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                    self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                    self.SideMultiLegReportingType = FIX50SP2.Tags.SideMultiLegReportingType(required=False)
                    self.ExchangeRule = FIX50SP2.Tags.ExchangeRule(required=False)
                    self.TradeAllocIndicator = FIX50SP2.Tags.TradeAllocIndicator(required=False)
                    self.PreallocMethod = FIX50SP2.Tags.PreallocMethod(required=False)
                    self.AllocID = FIX50SP2.Tags.AllocID(required=False)
                    self.SideGrossTradeAmt = FIX50SP2.Tags.SideGrossTradeAmt(required=False)
                    self.AggressorIndicator = FIX50SP2.Tags.AggressorIndicator(required=False)
                    self.ExchangeSpecialInstructions = FIX50SP2.Tags.ExchangeSpecialInstructions(required=False)
                    self.OrderCategory = FIX50SP2.Tags.OrderCategory(required=False)
                    self.SideExecID = FIX50SP2.Tags.SideExecID(required=False)
                    self.OrderDelay = FIX50SP2.Tags.OrderDelay(required=False)
                    self.OrderDelayUnit = FIX50SP2.Tags.OrderDelayUnit(required=False)
                    self.SideLiquidityInd = FIX50SP2.Tags.SideLiquidityInd(required=False)
                    self.Parties = FIX50SP2.Components.Parties(required=False)
                    self.ClrInstGrp = FIX50SP2.Components.ClrInstGrp(required=False)
                    self.CommissionData = FIX50SP2.Components.CommissionData(required=False)
                    self.ContAmtGrp = FIX50SP2.Components.ContAmtGrp(required=False)
                    self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                    self.MiscFeesGrp = FIX50SP2.Components.MiscFeesGrp(required=False)
                    self.TrdAllocGrp = FIX50SP2.Components.TrdAllocGrp(required=False)
                    self.SideTrdRegTS = FIX50SP2.Components.SideTrdRegTS(required=False)
                    self.SettlDetails = FIX50SP2.Components.SettlDetails(required=False)
                    self.TradeReportOrderDetail = FIX50SP2.Components.TradeReportOrderDetail(required=False)

        class SecLstUpdRelSymGrp(RepeatingGroup):
            class NoRelatedSym(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.ListUpdateAction = FIX50SP2.Tags.ListUpdateAction(required=False)
                    self.Currency = FIX50SP2.Tags.Currency(required=False)
                    self.Text = FIX50SP2.Tags.Text(required=False)
                    self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                    self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                    self.RelSymTransactTime = FIX50SP2.Tags.RelSymTransactTime(required=False)
                    self.Instrument = FIX50SP2.Components.Instrument(required=False)
                    self.InstrumentExtension = FIX50SP2.Components.InstrumentExtension(required=False)
                    self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                    self.SecurityTradingRules = FIX50SP2.Components.SecurityTradingRules(required=False)
                    self.StrikeRules = FIX50SP2.Components.StrikeRules(required=False)
                    self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                    self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                    self.SecLstUpdRelSymsLegGrp = FIX50SP2.Components.SecLstUpdRelSymsLegGrp(required=False)
                    self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                    self.YieldData = FIX50SP2.Components.YieldData(required=False)

        class TrdCapRptAckSideGrp(RepeatingGroup):
            class NoSides(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.Side = FIX50SP2.Tags.Side(required=True)
                    self.Account = FIX50SP2.Tags.Account(required=False)
                    self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                    self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                    self.ProcessCode = FIX50SP2.Tags.ProcessCode(required=False)
                    self.OddLot = FIX50SP2.Tags.OddLot(required=False)
                    self.TradeInputSource = FIX50SP2.Tags.TradeInputSource(required=False)
                    self.TradeInputDevice = FIX50SP2.Tags.TradeInputDevice(required=False)
                    self.ComplianceID = FIX50SP2.Tags.ComplianceID(required=False)
                    self.SolicitedFlag = FIX50SP2.Tags.SolicitedFlag(required=False)
                    self.CustOrderCapacity = FIX50SP2.Tags.CustOrderCapacity(required=False)
                    self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                    self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                    self.TimeBracket = FIX50SP2.Tags.TimeBracket(required=False)
                    self.NetGrossInd = FIX50SP2.Tags.NetGrossInd(required=False)
                    self.SideCurrency = FIX50SP2.Tags.SideCurrency(required=False)
                    self.SideSettlCurrency = FIX50SP2.Tags.SideSettlCurrency(required=False)
                    self.NumDaysInterest = FIX50SP2.Tags.NumDaysInterest(required=False)
                    self.ExDate = FIX50SP2.Tags.ExDate(required=False)
                    self.AccruedInterestRate = FIX50SP2.Tags.AccruedInterestRate(required=False)
                    self.AccruedInterestAmt = FIX50SP2.Tags.AccruedInterestAmt(required=False)
                    self.InterestAtMaturity = FIX50SP2.Tags.InterestAtMaturity(required=False)
                    self.EndAccruedInterestAmt = FIX50SP2.Tags.EndAccruedInterestAmt(required=False)
                    self.StartCash = FIX50SP2.Tags.StartCash(required=False)
                    self.EndCash = FIX50SP2.Tags.EndCash(required=False)
                    self.Concession = FIX50SP2.Tags.Concession(required=False)
                    self.TotalTakedown = FIX50SP2.Tags.TotalTakedown(required=False)
                    self.NetMoney = FIX50SP2.Tags.NetMoney(required=False)
                    self.SettlCurrAmt = FIX50SP2.Tags.SettlCurrAmt(required=False)
                    self.SettlCurrFxRate = FIX50SP2.Tags.SettlCurrFxRate(required=False)
                    self.SettlCurrFxRateCalc = FIX50SP2.Tags.SettlCurrFxRateCalc(required=False)
                    self.PositionEffect = FIX50SP2.Tags.PositionEffect(required=False)
                    self.SideMultiLegReportingType = FIX50SP2.Tags.SideMultiLegReportingType(required=False)
                    self.ExchangeRule = FIX50SP2.Tags.ExchangeRule(required=False)
                    self.TradeAllocIndicator = FIX50SP2.Tags.TradeAllocIndicator(required=False)
                    self.PreallocMethod = FIX50SP2.Tags.PreallocMethod(required=False)
                    self.AllocID = FIX50SP2.Tags.AllocID(required=False)
                    self.SideGrossTradeAmt = FIX50SP2.Tags.SideGrossTradeAmt(required=False)
                    self.AggressorIndicator = FIX50SP2.Tags.AggressorIndicator(required=False)
                    self.SideLastQty = FIX50SP2.Tags.SideLastQty(required=False)
                    self.SideTradeReportID = FIX50SP2.Tags.SideTradeReportID(required=False)
                    self.SideFillStationCd = FIX50SP2.Tags.SideFillStationCd(required=False)
                    self.SideReasonCd = FIX50SP2.Tags.SideReasonCd(required=False)
                    self.RptSeq = FIX50SP2.Tags.RptSeq(required=False)
                    self.SideTrdSubTyp = FIX50SP2.Tags.SideTrdSubTyp(required=False)
                    self.SideExecID = FIX50SP2.Tags.SideExecID(required=False)
                    self.OrderDelay = FIX50SP2.Tags.OrderDelay(required=False)
                    self.OrderDelayUnit = FIX50SP2.Tags.OrderDelayUnit(required=False)
                    self.OrderCategory = FIX50SP2.Tags.OrderCategory(required=False)
                    self.Parties = FIX50SP2.Components.Parties(required=False)
                    self.ClrInstGrp = FIX50SP2.Components.ClrInstGrp(required=False)
                    self.CommissionData = FIX50SP2.Components.CommissionData(required=False)
                    self.ContAmtGrp = FIX50SP2.Components.ContAmtGrp(required=False)
                    self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                    self.MiscFeesGrp = FIX50SP2.Components.MiscFeesGrp(required=False)
                    self.SettlDetails = FIX50SP2.Components.SettlDetails(required=False)
                    self.TrdAllocGrp = FIX50SP2.Components.TrdAllocGrp(required=False)
                    self.SideTrdRegTS = FIX50SP2.Components.SideTrdRegTS(required=False)
                    self.TradeReportOrderDetail = FIX50SP2.Components.TradeReportOrderDetail(required=False)

        class QuotReqGrp(RepeatingGroup):
            class NoRelatedSym(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.PrevClosePx = FIX50SP2.Tags.PrevClosePx(required=False)
                    self.QuoteRequestType = FIX50SP2.Tags.QuoteRequestType(required=False)
                    self.QuoteType = FIX50SP2.Tags.QuoteType(required=False)
                    self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                    self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                    self.TradeOriginationDate = FIX50SP2.Tags.TradeOriginationDate(required=False)
                    self.Side = FIX50SP2.Tags.Side(required=False)
                    self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                    self.MinQty = FIX50SP2.Tags.MinQty(required=False)
                    self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                    self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                    self.SettlDate2 = FIX50SP2.Tags.SettlDate2(required=False)
                    self.OrderQty2 = FIX50SP2.Tags.OrderQty2(required=False)
                    self.Currency = FIX50SP2.Tags.Currency(required=False)
                    self.Account = FIX50SP2.Tags.Account(required=False)
                    self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                    self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                    self.QuotePriceType = FIX50SP2.Tags.QuotePriceType(required=False)
                    self.OrdType = FIX50SP2.Tags.OrdType(required=False)
                    self.ValidUntilTime = FIX50SP2.Tags.ValidUntilTime(required=False)
                    self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                    self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                    self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                    self.Price = FIX50SP2.Tags.Price(required=False)
                    self.Price2 = FIX50SP2.Tags.Price2(required=False)
                    self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                    self.Instrument = FIX50SP2.Components.Instrument(required=True)
                    self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                    self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                    self.OrderQtyData = FIX50SP2.Components.OrderQtyData(required=False)
                    self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                    self.QuotReqLegsGrp = FIX50SP2.Components.QuotReqLegsGrp(required=False)
                    self.QuotQualGrp = FIX50SP2.Components.QuotQualGrp(required=False)
                    self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                    self.YieldData = FIX50SP2.Components.YieldData(required=False)
                    self.Parties = FIX50SP2.Components.Parties(required=False)
                    self.RateSource = FIX50SP2.Components.RateSource(required=False)

        class ListOrdGrp(RepeatingGroup):
            class NoOrders(Group):
                def __init__(self, required=False):
                    Group.__init__(self, required=required)
                    self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=True)
                    self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                    self.ListSeqNo = FIX50SP2.Tags.ListSeqNo(required=True)
                    self.ClOrdLinkID = FIX50SP2.Tags.ClOrdLinkID(required=False)
                    self.SettlInstMode = FIX50SP2.Tags.SettlInstMode(required=False)
                    self.TradeOriginationDate = FIX50SP2.Tags.TradeOriginationDate(required=False)
                    self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                    self.Account = FIX50SP2.Tags.Account(required=False)
                    self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                    self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                    self.DayBookingInst = FIX50SP2.Tags.DayBookingInst(required=False)
                    self.BookingUnit = FIX50SP2.Tags.BookingUnit(required=False)
                    self.AllocID = FIX50SP2.Tags.AllocID(required=False)
                    self.PreallocMethod = FIX50SP2.Tags.PreallocMethod(required=False)
                    self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                    self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                    self.CashMargin = FIX50SP2.Tags.CashMargin(required=False)
                    self.ClearingFeeIndicator = FIX50SP2.Tags.ClearingFeeIndicator(required=False)
                    self.HandlInst = FIX50SP2.Tags.HandlInst(required=False)
                    self.ExecInst = FIX50SP2.Tags.ExecInst(required=False)
                    self.MinQty = FIX50SP2.Tags.MinQty(required=False)
                    self.MatchIncrement = FIX50SP2.Tags.MatchIncrement(required=False)
                    self.MaxPriceLevels = FIX50SP2.Tags.MaxPriceLevels(required=False)
                    self.MaxFloor = FIX50SP2.Tags.MaxFloor(required=False)
                    self.ExDestination = FIX50SP2.Tags.ExDestination(required=False)
                    self.ExDestinationIDSource = FIX50SP2.Tags.ExDestinationIDSource(required=False)
                    self.ProcessCode = FIX50SP2.Tags.ProcessCode(required=False)
                    self.PrevClosePx = FIX50SP2.Tags.PrevClosePx(required=False)
                    self.Side = FIX50SP2.Tags.Side(required=True)
                    self.SideValueInd = FIX50SP2.Tags.SideValueInd(required=False)
                    self.LocateReqd = FIX50SP2.Tags.LocateReqd(required=False)
                    self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                    self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                    self.OrdType = FIX50SP2.Tags.OrdType(required=False)
                    self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                    self.Price = FIX50SP2.Tags.Price(required=False)
                    self.PriceProtectionScope = FIX50SP2.Tags.PriceProtectionScope(required=False)
                    self.StopPx = FIX50SP2.Tags.StopPx(required=False)
                    self.Currency = FIX50SP2.Tags.Currency(required=False)
                    self.ComplianceID = FIX50SP2.Tags.ComplianceID(required=False)
                    self.SolicitedFlag = FIX50SP2.Tags.SolicitedFlag(required=False)
                    self.IOIID = FIX50SP2.Tags.IOIID(required=False)
                    self.QuoteID = FIX50SP2.Tags.QuoteID(required=False)
                    self.RefOrderID = FIX50SP2.Tags.RefOrderID(required=False)
                    self.RefOrderIDSource = FIX50SP2.Tags.RefOrderIDSource(required=False)
                    self.TimeInForce = FIX50SP2.Tags.TimeInForce(required=False)
                    self.EffectiveTime = FIX50SP2.Tags.EffectiveTime(required=False)
                    self.ExpireDate = FIX50SP2.Tags.ExpireDate(required=False)
                    self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                    self.GTBookingInst = FIX50SP2.Tags.GTBookingInst(required=False)
                    self.OrderCapacity = FIX50SP2.Tags.OrderCapacity(required=False)
                    self.OrderRestrictions = FIX50SP2.Tags.OrderRestrictions(required=False)
                    self.PreTradeAnonymity = FIX50SP2.Tags.PreTradeAnonymity(required=False)
                    self.CustOrderCapacity = FIX50SP2.Tags.CustOrderCapacity(required=False)
                    self.ForexReq = FIX50SP2.Tags.ForexReq(required=False)
                    self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                    self.BookingType = FIX50SP2.Tags.BookingType(required=False)
                    self.Text = FIX50SP2.Tags.Text(required=False)
                    self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                    self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                    self.SettlDate2 = FIX50SP2.Tags.SettlDate2(required=False)
                    self.OrderQty2 = FIX50SP2.Tags.OrderQty2(required=False)
                    self.Price2 = FIX50SP2.Tags.Price2(required=False)
                    self.PositionEffect = FIX50SP2.Tags.PositionEffect(required=False)
                    self.CoveredOrUncovered = FIX50SP2.Tags.CoveredOrUncovered(required=False)
                    self.MaxShow = FIX50SP2.Tags.MaxShow(required=False)
                    self.TargetStrategy = FIX50SP2.Tags.TargetStrategy(required=False)
                    self.TargetStrategyParameters = FIX50SP2.Tags.TargetStrategyParameters(required=False)
                    self.ParticipationRate = FIX50SP2.Tags.ParticipationRate(required=False)
                    self.Designation = FIX50SP2.Tags.Designation(required=False)
                    self.Parties = FIX50SP2.Components.Parties(required=False)
                    self.PreAllocGrp = FIX50SP2.Components.PreAllocGrp(required=False)
                    self.DisplayInstruction = FIX50SP2.Components.DisplayInstruction(required=False)
                    self.TrdgSesGrp = FIX50SP2.Components.TrdgSesGrp(required=False)
                    self.Instrument = FIX50SP2.Components.Instrument(required=True)
                    self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                    self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                    self.OrderQtyData = FIX50SP2.Components.OrderQtyData(required=True)
                    self.TriggeringInstruction = FIX50SP2.Components.TriggeringInstruction(required=False)
                    self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                    self.YieldData = FIX50SP2.Components.YieldData(required=False)
                    self.CommissionData = FIX50SP2.Components.CommissionData(required=False)
                    self.PegInstructions = FIX50SP2.Components.PegInstructions(required=False)
                    self.DiscretionInstructions = FIX50SP2.Components.DiscretionInstructions(required=False)
                    self.StrategyParametersGrp = FIX50SP2.Components.StrategyParametersGrp(required=False)


    class Header:
        def __init__(self):
            self.BeginString = FIX50SP2.Tags.BeginString(required=True)
            self.BodyLength = FIX50SP2.Tags.BodyLength(required=True)
            self.MsgType = FIX50SP2.Tags.MsgType(required=True)
            self.SenderCompID = FIX50SP2.Tags.SenderCompID(required=True)
            self.TargetCompID = FIX50SP2.Tags.TargetCompID(required=True)
            self.OnBehalfOfCompID = FIX50SP2.Tags.OnBehalfOfCompID(required=False)
            self.DeliverToCompID = FIX50SP2.Tags.DeliverToCompID(required=False)
            self.SecureDataLen = FIX50SP2.Tags.SecureDataLen(required=False)
            self.SecureData = FIX50SP2.Tags.SecureData(required=False)
            self.MsgSeqNum = FIX50SP2.Tags.MsgSeqNum(required=True)
            self.SenderSubID = FIX50SP2.Tags.SenderSubID(required=False)
            self.SenderLocationID = FIX50SP2.Tags.SenderLocationID(required=False)
            self.TargetSubID = FIX50SP2.Tags.TargetSubID(required=False)
            self.TargetLocationID = FIX50SP2.Tags.TargetLocationID(required=False)
            self.OnBehalfOfSubID = FIX50SP2.Tags.OnBehalfOfSubID(required=False)
            self.OnBehalfOfLocationID = FIX50SP2.Tags.OnBehalfOfLocationID(required=False)
            self.DeliverToSubID = FIX50SP2.Tags.DeliverToSubID(required=False)
            self.DeliverToLocationID = FIX50SP2.Tags.DeliverToLocationID(required=False)
            self.PossDupFlag = FIX50SP2.Tags.PossDupFlag(required=False)
            self.PossResend = FIX50SP2.Tags.PossResend(required=False)
            self.SendingTime = FIX50SP2.Tags.SendingTime(required=True)
            self.OrigSendingTime = FIX50SP2.Tags.OrigSendingTime(required=False)
            self.XmlDataLen = FIX50SP2.Tags.XmlDataLen(required=False)
            self.XmlData = FIX50SP2.Tags.XmlData(required=False)
            self.MessageEncoding = FIX50SP2.Tags.MessageEncoding(required=False)
            self.LastMsgSeqNumProcessed = FIX50SP2.Tags.LastMsgSeqNumProcessed(required=False)
            self.ApplVerID = FIX50SP2.Tags.ApplVerID(required=False)
            self.CstmApplVerID = FIX50SP2.Tags.CstmApplVerID(required=False)
            self.HopGrp = FIX50SP2.Components.HopGrp(required=False)

    class Messages:
        class IOI(AppMessage):
            MsgType = "6"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "6"
                self.IOIID = FIX50SP2.Tags.IOIID(required=True)
                self.IOITransType = FIX50SP2.Tags.IOITransType(required=True)
                self.IOIRefID = FIX50SP2.Tags.IOIRefID(required=False)
                self.Side = FIX50SP2.Tags.Side(required=True)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.IOIQty = FIX50SP2.Tags.IOIQty(required=True)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.Price = FIX50SP2.Tags.Price(required=False)
                self.ValidUntilTime = FIX50SP2.Tags.ValidUntilTime(required=False)
                self.IOIQltyInd = FIX50SP2.Tags.IOIQltyInd(required=False)
                self.IOINaturalFlag = FIX50SP2.Tags.IOINaturalFlag(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.URLLink = FIX50SP2.Tags.URLLink(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.OrderQtyData = FIX50SP2.Components.OrderQtyData(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                self.InstrmtLegIOIGrp = FIX50SP2.Components.InstrmtLegIOIGrp(required=False)
                self.IOIQualGrp = FIX50SP2.Components.IOIQualGrp(required=False)
                self.RoutingGrp = FIX50SP2.Components.RoutingGrp(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.YieldData = FIX50SP2.Components.YieldData(required=False)

        class Advertisement(AppMessage):
            MsgType = "7"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "7"
                self.AdvId = FIX50SP2.Tags.AdvId(required=True)
                self.AdvTransType = FIX50SP2.Tags.AdvTransType(required=True)
                self.AdvRefID = FIX50SP2.Tags.AdvRefID(required=False)
                self.AdvSide = FIX50SP2.Tags.AdvSide(required=True)
                self.Quantity = FIX50SP2.Tags.Quantity(required=True)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.Price = FIX50SP2.Tags.Price(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.URLLink = FIX50SP2.Tags.URLLink(required=False)
                self.LastMkt = FIX50SP2.Tags.LastMkt(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)

        class ExecutionReport(AppMessage):
            MsgType = "8"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "8"
                self.OrderID = FIX50SP2.Tags.OrderID(required=True)
                self.SecondaryOrderID = FIX50SP2.Tags.SecondaryOrderID(required=False)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.SecondaryExecID = FIX50SP2.Tags.SecondaryExecID(required=False)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.OrigClOrdID = FIX50SP2.Tags.OrigClOrdID(required=False)
                self.ClOrdLinkID = FIX50SP2.Tags.ClOrdLinkID(required=False)
                self.QuoteRespID = FIX50SP2.Tags.QuoteRespID(required=False)
                self.OrdStatusReqID = FIX50SP2.Tags.OrdStatusReqID(required=False)
                self.MassStatusReqID = FIX50SP2.Tags.MassStatusReqID(required=False)
                self.HostCrossID = FIX50SP2.Tags.HostCrossID(required=False)
                self.TotNumReports = FIX50SP2.Tags.TotNumReports(required=False)
                self.LastRptRequested = FIX50SP2.Tags.LastRptRequested(required=False)
                self.TradeOriginationDate = FIX50SP2.Tags.TradeOriginationDate(required=False)
                self.ListID = FIX50SP2.Tags.ListID(required=False)
                self.CrossID = FIX50SP2.Tags.CrossID(required=False)
                self.OrigCrossID = FIX50SP2.Tags.OrigCrossID(required=False)
                self.CrossType = FIX50SP2.Tags.CrossType(required=False)
                self.TrdMatchID = FIX50SP2.Tags.TrdMatchID(required=False)
                self.ExecID = FIX50SP2.Tags.ExecID(required=True)
                self.ExecRefID = FIX50SP2.Tags.ExecRefID(required=False)
                self.ExecType = FIX50SP2.Tags.ExecType(required=True)
                self.OrdStatus = FIX50SP2.Tags.OrdStatus(required=True)
                self.WorkingIndicator = FIX50SP2.Tags.WorkingIndicator(required=False)
                self.OrdRejReason = FIX50SP2.Tags.OrdRejReason(required=False)
                self.ExecRestatementReason = FIX50SP2.Tags.ExecRestatementReason(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.DayBookingInst = FIX50SP2.Tags.DayBookingInst(required=False)
                self.BookingUnit = FIX50SP2.Tags.BookingUnit(required=False)
                self.PreallocMethod = FIX50SP2.Tags.PreallocMethod(required=False)
                self.AllocID = FIX50SP2.Tags.AllocID(required=False)
                self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.MatchType = FIX50SP2.Tags.MatchType(required=False)
                self.OrderCategory = FIX50SP2.Tags.OrderCategory(required=False)
                self.CashMargin = FIX50SP2.Tags.CashMargin(required=False)
                self.ClearingFeeIndicator = FIX50SP2.Tags.ClearingFeeIndicator(required=False)
                self.Side = FIX50SP2.Tags.Side(required=True)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.LotType = FIX50SP2.Tags.LotType(required=False)
                self.OrdType = FIX50SP2.Tags.OrdType(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.Price = FIX50SP2.Tags.Price(required=False)
                self.PriceProtectionScope = FIX50SP2.Tags.PriceProtectionScope(required=False)
                self.StopPx = FIX50SP2.Tags.StopPx(required=False)
                self.PeggedPrice = FIX50SP2.Tags.PeggedPrice(required=False)
                self.PeggedRefPrice = FIX50SP2.Tags.PeggedRefPrice(required=False)
                self.DiscretionPrice = FIX50SP2.Tags.DiscretionPrice(required=False)
                self.TargetStrategy = FIX50SP2.Tags.TargetStrategy(required=False)
                self.TargetStrategyParameters = FIX50SP2.Tags.TargetStrategyParameters(required=False)
                self.ParticipationRate = FIX50SP2.Tags.ParticipationRate(required=False)
                self.TargetStrategyPerformance = FIX50SP2.Tags.TargetStrategyPerformance(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.ComplianceID = FIX50SP2.Tags.ComplianceID(required=False)
                self.SolicitedFlag = FIX50SP2.Tags.SolicitedFlag(required=False)
                self.TimeInForce = FIX50SP2.Tags.TimeInForce(required=False)
                self.EffectiveTime = FIX50SP2.Tags.EffectiveTime(required=False)
                self.ExpireDate = FIX50SP2.Tags.ExpireDate(required=False)
                self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                self.ExecInst = FIX50SP2.Tags.ExecInst(required=False)
                self.AggressorIndicator = FIX50SP2.Tags.AggressorIndicator(required=False)
                self.OrderCapacity = FIX50SP2.Tags.OrderCapacity(required=False)
                self.OrderRestrictions = FIX50SP2.Tags.OrderRestrictions(required=False)
                self.PreTradeAnonymity = FIX50SP2.Tags.PreTradeAnonymity(required=False)
                self.CustOrderCapacity = FIX50SP2.Tags.CustOrderCapacity(required=False)
                self.LastQty = FIX50SP2.Tags.LastQty(required=False)
                self.CalculatedCcyLastQty = FIX50SP2.Tags.CalculatedCcyLastQty(required=False)
                self.LastSwapPoints = FIX50SP2.Tags.LastSwapPoints(required=False)
                self.UnderlyingLastQty = FIX50SP2.Tags.UnderlyingLastQty(required=False)
                self.LastPx = FIX50SP2.Tags.LastPx(required=False)
                self.UnderlyingLastPx = FIX50SP2.Tags.UnderlyingLastPx(required=False)
                self.LastParPx = FIX50SP2.Tags.LastParPx(required=False)
                self.LastSpotRate = FIX50SP2.Tags.LastSpotRate(required=False)
                self.LastForwardPoints = FIX50SP2.Tags.LastForwardPoints(required=False)
                self.LastMkt = FIX50SP2.Tags.LastMkt(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.TimeBracket = FIX50SP2.Tags.TimeBracket(required=False)
                self.LastCapacity = FIX50SP2.Tags.LastCapacity(required=False)
                self.LeavesQty = FIX50SP2.Tags.LeavesQty(required=True)
                self.CumQty = FIX50SP2.Tags.CumQty(required=True)
                self.AvgPx = FIX50SP2.Tags.AvgPx(required=False)
                self.DayOrderQty = FIX50SP2.Tags.DayOrderQty(required=False)
                self.DayCumQty = FIX50SP2.Tags.DayCumQty(required=False)
                self.DayAvgPx = FIX50SP2.Tags.DayAvgPx(required=False)
                self.TotNoFills = FIX50SP2.Tags.TotNoFills(required=False)
                self.LastFragment = FIX50SP2.Tags.LastFragment(required=False)
                self.GTBookingInst = FIX50SP2.Tags.GTBookingInst(required=False)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.ReportToExch = FIX50SP2.Tags.ReportToExch(required=False)
                self.GrossTradeAmt = FIX50SP2.Tags.GrossTradeAmt(required=False)
                self.NumDaysInterest = FIX50SP2.Tags.NumDaysInterest(required=False)
                self.ExDate = FIX50SP2.Tags.ExDate(required=False)
                self.AccruedInterestRate = FIX50SP2.Tags.AccruedInterestRate(required=False)
                self.AccruedInterestAmt = FIX50SP2.Tags.AccruedInterestAmt(required=False)
                self.InterestAtMaturity = FIX50SP2.Tags.InterestAtMaturity(required=False)
                self.EndAccruedInterestAmt = FIX50SP2.Tags.EndAccruedInterestAmt(required=False)
                self.StartCash = FIX50SP2.Tags.StartCash(required=False)
                self.EndCash = FIX50SP2.Tags.EndCash(required=False)
                self.TradedFlatSwitch = FIX50SP2.Tags.TradedFlatSwitch(required=False)
                self.BasisFeatureDate = FIX50SP2.Tags.BasisFeatureDate(required=False)
                self.BasisFeaturePrice = FIX50SP2.Tags.BasisFeaturePrice(required=False)
                self.Concession = FIX50SP2.Tags.Concession(required=False)
                self.TotalTakedown = FIX50SP2.Tags.TotalTakedown(required=False)
                self.NetMoney = FIX50SP2.Tags.NetMoney(required=False)
                self.SettlCurrAmt = FIX50SP2.Tags.SettlCurrAmt(required=False)
                self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                self.SettlCurrFxRate = FIX50SP2.Tags.SettlCurrFxRate(required=False)
                self.SettlCurrFxRateCalc = FIX50SP2.Tags.SettlCurrFxRateCalc(required=False)
                self.HandlInst = FIX50SP2.Tags.HandlInst(required=False)
                self.MinQty = FIX50SP2.Tags.MinQty(required=False)
                self.MatchIncrement = FIX50SP2.Tags.MatchIncrement(required=False)
                self.MaxPriceLevels = FIX50SP2.Tags.MaxPriceLevels(required=False)
                self.MaxFloor = FIX50SP2.Tags.MaxFloor(required=False)
                self.PositionEffect = FIX50SP2.Tags.PositionEffect(required=False)
                self.MaxShow = FIX50SP2.Tags.MaxShow(required=False)
                self.BookingType = FIX50SP2.Tags.BookingType(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.SettlDate2 = FIX50SP2.Tags.SettlDate2(required=False)
                self.OrderQty2 = FIX50SP2.Tags.OrderQty2(required=False)
                self.LastForwardPoints2 = FIX50SP2.Tags.LastForwardPoints2(required=False)
                self.MultiLegReportingType = FIX50SP2.Tags.MultiLegReportingType(required=False)
                self.CancellationRights = FIX50SP2.Tags.CancellationRights(required=False)
                self.MoneyLaunderingStatus = FIX50SP2.Tags.MoneyLaunderingStatus(required=False)
                self.RegistID = FIX50SP2.Tags.RegistID(required=False)
                self.Designation = FIX50SP2.Tags.Designation(required=False)
                self.TransBkdTime = FIX50SP2.Tags.TransBkdTime(required=False)
                self.ExecValuationPoint = FIX50SP2.Tags.ExecValuationPoint(required=False)
                self.ExecPriceType = FIX50SP2.Tags.ExecPriceType(required=False)
                self.ExecPriceAdjustment = FIX50SP2.Tags.ExecPriceAdjustment(required=False)
                self.PriorityIndicator = FIX50SP2.Tags.PriorityIndicator(required=False)
                self.PriceImprovement = FIX50SP2.Tags.PriceImprovement(required=False)
                self.LastLiquidityInd = FIX50SP2.Tags.LastLiquidityInd(required=False)
                self.CopyMsgIndicator = FIX50SP2.Tags.CopyMsgIndicator(required=False)
                self.DividendYield = FIX50SP2.Tags.DividendYield(required=False)
                self.ManualOrderIndicator = FIX50SP2.Tags.ManualOrderIndicator(required=False)
                self.CustDirectedOrder = FIX50SP2.Tags.CustDirectedOrder(required=False)
                self.ReceivedDeptID = FIX50SP2.Tags.ReceivedDeptID(required=False)
                self.CustOrderHandlingInst = FIX50SP2.Tags.CustOrderHandlingInst(required=False)
                self.OrderHandlingInstSource = FIX50SP2.Tags.OrderHandlingInstSource(required=False)
                self.Volatility = FIX50SP2.Tags.Volatility(required=False)
                self.TimeToExpiration = FIX50SP2.Tags.TimeToExpiration(required=False)
                self.RiskFreeRate = FIX50SP2.Tags.RiskFreeRate(required=False)
                self.PriceDelta = FIX50SP2.Tags.PriceDelta(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.ContraGrp = FIX50SP2.Components.ContraGrp(required=False)
                self.PreAllocGrp = FIX50SP2.Components.PreAllocGrp(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                self.OrderQtyData = FIX50SP2.Components.OrderQtyData(required=False)
                self.TriggeringInstruction = FIX50SP2.Components.TriggeringInstruction(required=False)
                self.PegInstructions = FIX50SP2.Components.PegInstructions(required=False)
                self.DiscretionInstructions = FIX50SP2.Components.DiscretionInstructions(required=False)
                self.StrategyParametersGrp = FIX50SP2.Components.StrategyParametersGrp(required=False)
                self.FillsGrp = FIX50SP2.Components.FillsGrp(required=False)
                self.CommissionData = FIX50SP2.Components.CommissionData(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.YieldData = FIX50SP2.Components.YieldData(required=False)
                self.DisplayInstruction = FIX50SP2.Components.DisplayInstruction(required=False)
                self.ContAmtGrp = FIX50SP2.Components.ContAmtGrp(required=False)
                self.InstrmtLegExecGrp = FIX50SP2.Components.InstrmtLegExecGrp(required=False)
                self.MiscFeesGrp = FIX50SP2.Components.MiscFeesGrp(required=False)
                self.TrdRegTimestamps = FIX50SP2.Components.TrdRegTimestamps(required=False)
                self.RateSource = FIX50SP2.Components.RateSource(required=False)

        class OrderCancelReject(AppMessage):
            MsgType = "9"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "9"
                self.OrderID = FIX50SP2.Tags.OrderID(required=True)
                self.SecondaryOrderID = FIX50SP2.Tags.SecondaryOrderID(required=False)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=True)
                self.ClOrdLinkID = FIX50SP2.Tags.ClOrdLinkID(required=False)
                self.OrigClOrdID = FIX50SP2.Tags.OrigClOrdID(required=False)
                self.OrdStatus = FIX50SP2.Tags.OrdStatus(required=True)
                self.WorkingIndicator = FIX50SP2.Tags.WorkingIndicator(required=False)
                self.OrigOrdModTime = FIX50SP2.Tags.OrigOrdModTime(required=False)
                self.ListID = FIX50SP2.Tags.ListID(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.TradeOriginationDate = FIX50SP2.Tags.TradeOriginationDate(required=False)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.CxlRejResponseTo = FIX50SP2.Tags.CxlRejResponseTo(required=True)
                self.CxlRejReason = FIX50SP2.Tags.CxlRejReason(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)

        class News(AppMessage):
            MsgType = "B"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "B"
                self.OrigTime = FIX50SP2.Tags.OrigTime(required=False)
                self.Urgency = FIX50SP2.Tags.Urgency(required=False)
                self.Headline = FIX50SP2.Tags.Headline(required=True)
                self.EncodedHeadlineLen = FIX50SP2.Tags.EncodedHeadlineLen(required=False)
                self.EncodedHeadline = FIX50SP2.Tags.EncodedHeadline(required=False)
                self.URLLink = FIX50SP2.Tags.URLLink(required=False)
                self.RawDataLength = FIX50SP2.Tags.RawDataLength(required=False)
                self.RawData = FIX50SP2.Tags.RawData(required=False)
                self.NewsID = FIX50SP2.Tags.NewsID(required=False)
                self.NewsCategory = FIX50SP2.Tags.NewsCategory(required=False)
                self.LanguageCode = FIX50SP2.Tags.LanguageCode(required=False)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.RoutingGrp = FIX50SP2.Components.RoutingGrp(required=False)
                self.InstrmtGrp = FIX50SP2.Components.InstrmtGrp(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.LinesOfTextGrp = FIX50SP2.Components.LinesOfTextGrp(required=True)
                self.NewsRefGrp = FIX50SP2.Components.NewsRefGrp(required=False)

        class Email(AppMessage):
            MsgType = "C"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "C"
                self.EmailThreadID = FIX50SP2.Tags.EmailThreadID(required=True)
                self.EmailType = FIX50SP2.Tags.EmailType(required=True)
                self.OrigTime = FIX50SP2.Tags.OrigTime(required=False)
                self.Subject = FIX50SP2.Tags.Subject(required=True)
                self.EncodedSubjectLen = FIX50SP2.Tags.EncodedSubjectLen(required=False)
                self.EncodedSubject = FIX50SP2.Tags.EncodedSubject(required=False)
                self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.RawDataLength = FIX50SP2.Tags.RawDataLength(required=False)
                self.RawData = FIX50SP2.Tags.RawData(required=False)
                self.RoutingGrp = FIX50SP2.Components.RoutingGrp(required=False)
                self.InstrmtGrp = FIX50SP2.Components.InstrmtGrp(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.LinesOfTextGrp = FIX50SP2.Components.LinesOfTextGrp(required=True)

        class NewOrderSingle(AppMessage):
            MsgType = "D"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "D"
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=True)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.ClOrdLinkID = FIX50SP2.Tags.ClOrdLinkID(required=False)
                self.TradeOriginationDate = FIX50SP2.Tags.TradeOriginationDate(required=False)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.DayBookingInst = FIX50SP2.Tags.DayBookingInst(required=False)
                self.BookingUnit = FIX50SP2.Tags.BookingUnit(required=False)
                self.PreallocMethod = FIX50SP2.Tags.PreallocMethod(required=False)
                self.AllocID = FIX50SP2.Tags.AllocID(required=False)
                self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.CashMargin = FIX50SP2.Tags.CashMargin(required=False)
                self.ClearingFeeIndicator = FIX50SP2.Tags.ClearingFeeIndicator(required=False)
                self.HandlInst = FIX50SP2.Tags.HandlInst(required=False)
                self.ExecInst = FIX50SP2.Tags.ExecInst(required=False)
                self.MinQty = FIX50SP2.Tags.MinQty(required=False)
                self.MatchIncrement = FIX50SP2.Tags.MatchIncrement(required=False)
                self.MaxPriceLevels = FIX50SP2.Tags.MaxPriceLevels(required=False)
                self.MaxFloor = FIX50SP2.Tags.MaxFloor(required=False)
                self.ExDestination = FIX50SP2.Tags.ExDestination(required=False)
                self.ExDestinationIDSource = FIX50SP2.Tags.ExDestinationIDSource(required=False)
                self.ProcessCode = FIX50SP2.Tags.ProcessCode(required=False)
                self.PrevClosePx = FIX50SP2.Tags.PrevClosePx(required=False)
                self.Side = FIX50SP2.Tags.Side(required=True)
                self.LocateReqd = FIX50SP2.Tags.LocateReqd(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.OrdType = FIX50SP2.Tags.OrdType(required=True)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.Price = FIX50SP2.Tags.Price(required=False)
                self.PriceProtectionScope = FIX50SP2.Tags.PriceProtectionScope(required=False)
                self.StopPx = FIX50SP2.Tags.StopPx(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.ComplianceID = FIX50SP2.Tags.ComplianceID(required=False)
                self.SolicitedFlag = FIX50SP2.Tags.SolicitedFlag(required=False)
                self.IOIID = FIX50SP2.Tags.IOIID(required=False)
                self.QuoteID = FIX50SP2.Tags.QuoteID(required=False)
                self.TimeInForce = FIX50SP2.Tags.TimeInForce(required=False)
                self.EffectiveTime = FIX50SP2.Tags.EffectiveTime(required=False)
                self.ExpireDate = FIX50SP2.Tags.ExpireDate(required=False)
                self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                self.GTBookingInst = FIX50SP2.Tags.GTBookingInst(required=False)
                self.OrderCapacity = FIX50SP2.Tags.OrderCapacity(required=False)
                self.OrderRestrictions = FIX50SP2.Tags.OrderRestrictions(required=False)
                self.PreTradeAnonymity = FIX50SP2.Tags.PreTradeAnonymity(required=False)
                self.CustOrderCapacity = FIX50SP2.Tags.CustOrderCapacity(required=False)
                self.ForexReq = FIX50SP2.Tags.ForexReq(required=False)
                self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                self.BookingType = FIX50SP2.Tags.BookingType(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.SettlDate2 = FIX50SP2.Tags.SettlDate2(required=False)
                self.OrderQty2 = FIX50SP2.Tags.OrderQty2(required=False)
                self.Price2 = FIX50SP2.Tags.Price2(required=False)
                self.PositionEffect = FIX50SP2.Tags.PositionEffect(required=False)
                self.CoveredOrUncovered = FIX50SP2.Tags.CoveredOrUncovered(required=False)
                self.MaxShow = FIX50SP2.Tags.MaxShow(required=False)
                self.TargetStrategy = FIX50SP2.Tags.TargetStrategy(required=False)
                self.TargetStrategyParameters = FIX50SP2.Tags.TargetStrategyParameters(required=False)
                self.ParticipationRate = FIX50SP2.Tags.ParticipationRate(required=False)
                self.CancellationRights = FIX50SP2.Tags.CancellationRights(required=False)
                self.MoneyLaunderingStatus = FIX50SP2.Tags.MoneyLaunderingStatus(required=False)
                self.RegistID = FIX50SP2.Tags.RegistID(required=False)
                self.Designation = FIX50SP2.Tags.Designation(required=False)
                self.ManualOrderIndicator = FIX50SP2.Tags.ManualOrderIndicator(required=False)
                self.CustDirectedOrder = FIX50SP2.Tags.CustDirectedOrder(required=False)
                self.ReceivedDeptID = FIX50SP2.Tags.ReceivedDeptID(required=False)
                self.CustOrderHandlingInst = FIX50SP2.Tags.CustOrderHandlingInst(required=False)
                self.OrderHandlingInstSource = FIX50SP2.Tags.OrderHandlingInstSource(required=False)
                self.RefOrderID = FIX50SP2.Tags.RefOrderID(required=False)
                self.RefOrderIDSource = FIX50SP2.Tags.RefOrderIDSource(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.PreAllocGrp = FIX50SP2.Components.PreAllocGrp(required=False)
                self.DisplayInstruction = FIX50SP2.Components.DisplayInstruction(required=False)
                self.TrdgSesGrp = FIX50SP2.Components.TrdgSesGrp(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                self.OrderQtyData = FIX50SP2.Components.OrderQtyData(required=True)
                self.TriggeringInstruction = FIX50SP2.Components.TriggeringInstruction(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.YieldData = FIX50SP2.Components.YieldData(required=False)
                self.CommissionData = FIX50SP2.Components.CommissionData(required=False)
                self.PegInstructions = FIX50SP2.Components.PegInstructions(required=False)
                self.DiscretionInstructions = FIX50SP2.Components.DiscretionInstructions(required=False)
                self.StrategyParametersGrp = FIX50SP2.Components.StrategyParametersGrp(required=False)
                self.TrdRegTimestamps = FIX50SP2.Components.TrdRegTimestamps(required=False)

        class NewOrderList(AppMessage):
            MsgType = "E"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "E"
                self.ListID = FIX50SP2.Tags.ListID(required=True)
                self.BidID = FIX50SP2.Tags.BidID(required=False)
                self.ClientBidID = FIX50SP2.Tags.ClientBidID(required=False)
                self.ProgRptReqs = FIX50SP2.Tags.ProgRptReqs(required=False)
                self.BidType = FIX50SP2.Tags.BidType(required=True)
                self.ProgPeriodInterval = FIX50SP2.Tags.ProgPeriodInterval(required=False)
                self.CancellationRights = FIX50SP2.Tags.CancellationRights(required=False)
                self.MoneyLaunderingStatus = FIX50SP2.Tags.MoneyLaunderingStatus(required=False)
                self.RegistID = FIX50SP2.Tags.RegistID(required=False)
                self.ListExecInstType = FIX50SP2.Tags.ListExecInstType(required=False)
                self.ListExecInst = FIX50SP2.Tags.ListExecInst(required=False)
                self.ContingencyType = FIX50SP2.Tags.ContingencyType(required=False)
                self.EncodedListExecInstLen = FIX50SP2.Tags.EncodedListExecInstLen(required=False)
                self.EncodedListExecInst = FIX50SP2.Tags.EncodedListExecInst(required=False)
                self.AllowableOneSidednessPct = FIX50SP2.Tags.AllowableOneSidednessPct(required=False)
                self.AllowableOneSidednessValue = FIX50SP2.Tags.AllowableOneSidednessValue(required=False)
                self.AllowableOneSidednessCurr = FIX50SP2.Tags.AllowableOneSidednessCurr(required=False)
                self.TotNoOrders = FIX50SP2.Tags.TotNoOrders(required=True)
                self.LastFragment = FIX50SP2.Tags.LastFragment(required=False)
                self.RootParties = FIX50SP2.Components.RootParties(required=False)
                self.ListOrdGrp = FIX50SP2.Components.ListOrdGrp(required=True)

        class OrderCancelRequest(AppMessage):
            MsgType = "F"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "F"
                self.OrigClOrdID = FIX50SP2.Tags.OrigClOrdID(required=False)
                self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=True)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.ClOrdLinkID = FIX50SP2.Tags.ClOrdLinkID(required=False)
                self.ListID = FIX50SP2.Tags.ListID(required=False)
                self.OrigOrdModTime = FIX50SP2.Tags.OrigOrdModTime(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.Side = FIX50SP2.Tags.Side(required=True)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.ComplianceID = FIX50SP2.Tags.ComplianceID(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.OrderQtyData = FIX50SP2.Components.OrderQtyData(required=True)

        class OrderCancelReplaceRequest(AppMessage):
            MsgType = "G"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "G"
                self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                self.TradeOriginationDate = FIX50SP2.Tags.TradeOriginationDate(required=False)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                self.OrigClOrdID = FIX50SP2.Tags.OrigClOrdID(required=False)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=True)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.ClOrdLinkID = FIX50SP2.Tags.ClOrdLinkID(required=False)
                self.ListID = FIX50SP2.Tags.ListID(required=False)
                self.OrigOrdModTime = FIX50SP2.Tags.OrigOrdModTime(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.DayBookingInst = FIX50SP2.Tags.DayBookingInst(required=False)
                self.BookingUnit = FIX50SP2.Tags.BookingUnit(required=False)
                self.PreallocMethod = FIX50SP2.Tags.PreallocMethod(required=False)
                self.AllocID = FIX50SP2.Tags.AllocID(required=False)
                self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.CashMargin = FIX50SP2.Tags.CashMargin(required=False)
                self.ClearingFeeIndicator = FIX50SP2.Tags.ClearingFeeIndicator(required=False)
                self.HandlInst = FIX50SP2.Tags.HandlInst(required=False)
                self.ExecInst = FIX50SP2.Tags.ExecInst(required=False)
                self.MinQty = FIX50SP2.Tags.MinQty(required=False)
                self.MatchIncrement = FIX50SP2.Tags.MatchIncrement(required=False)
                self.MaxPriceLevels = FIX50SP2.Tags.MaxPriceLevels(required=False)
                self.MaxFloor = FIX50SP2.Tags.MaxFloor(required=False)
                self.ExDestination = FIX50SP2.Tags.ExDestination(required=False)
                self.ExDestinationIDSource = FIX50SP2.Tags.ExDestinationIDSource(required=False)
                self.Side = FIX50SP2.Tags.Side(required=True)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.OrdType = FIX50SP2.Tags.OrdType(required=True)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.Price = FIX50SP2.Tags.Price(required=False)
                self.PriceProtectionScope = FIX50SP2.Tags.PriceProtectionScope(required=False)
                self.StopPx = FIX50SP2.Tags.StopPx(required=False)
                self.TargetStrategy = FIX50SP2.Tags.TargetStrategy(required=False)
                self.TargetStrategyParameters = FIX50SP2.Tags.TargetStrategyParameters(required=False)
                self.ParticipationRate = FIX50SP2.Tags.ParticipationRate(required=False)
                self.ComplianceID = FIX50SP2.Tags.ComplianceID(required=False)
                self.SolicitedFlag = FIX50SP2.Tags.SolicitedFlag(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.TimeInForce = FIX50SP2.Tags.TimeInForce(required=False)
                self.EffectiveTime = FIX50SP2.Tags.EffectiveTime(required=False)
                self.ExpireDate = FIX50SP2.Tags.ExpireDate(required=False)
                self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                self.GTBookingInst = FIX50SP2.Tags.GTBookingInst(required=False)
                self.OrderCapacity = FIX50SP2.Tags.OrderCapacity(required=False)
                self.OrderRestrictions = FIX50SP2.Tags.OrderRestrictions(required=False)
                self.PreTradeAnonymity = FIX50SP2.Tags.PreTradeAnonymity(required=False)
                self.CustOrderCapacity = FIX50SP2.Tags.CustOrderCapacity(required=False)
                self.ForexReq = FIX50SP2.Tags.ForexReq(required=False)
                self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                self.BookingType = FIX50SP2.Tags.BookingType(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.SettlDate2 = FIX50SP2.Tags.SettlDate2(required=False)
                self.OrderQty2 = FIX50SP2.Tags.OrderQty2(required=False)
                self.Price2 = FIX50SP2.Tags.Price2(required=False)
                self.PositionEffect = FIX50SP2.Tags.PositionEffect(required=False)
                self.CoveredOrUncovered = FIX50SP2.Tags.CoveredOrUncovered(required=False)
                self.MaxShow = FIX50SP2.Tags.MaxShow(required=False)
                self.LocateReqd = FIX50SP2.Tags.LocateReqd(required=False)
                self.CancellationRights = FIX50SP2.Tags.CancellationRights(required=False)
                self.MoneyLaunderingStatus = FIX50SP2.Tags.MoneyLaunderingStatus(required=False)
                self.RegistID = FIX50SP2.Tags.RegistID(required=False)
                self.Designation = FIX50SP2.Tags.Designation(required=False)
                self.ManualOrderIndicator = FIX50SP2.Tags.ManualOrderIndicator(required=False)
                self.CustDirectedOrder = FIX50SP2.Tags.CustDirectedOrder(required=False)
                self.ReceivedDeptID = FIX50SP2.Tags.ReceivedDeptID(required=False)
                self.CustOrderHandlingInst = FIX50SP2.Tags.CustOrderHandlingInst(required=False)
                self.OrderHandlingInstSource = FIX50SP2.Tags.OrderHandlingInstSource(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.PreAllocGrp = FIX50SP2.Components.PreAllocGrp(required=False)
                self.DisplayInstruction = FIX50SP2.Components.DisplayInstruction(required=False)
                self.TrdgSesGrp = FIX50SP2.Components.TrdgSesGrp(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.OrderQtyData = FIX50SP2.Components.OrderQtyData(required=True)
                self.TriggeringInstruction = FIX50SP2.Components.TriggeringInstruction(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.YieldData = FIX50SP2.Components.YieldData(required=False)
                self.PegInstructions = FIX50SP2.Components.PegInstructions(required=False)
                self.DiscretionInstructions = FIX50SP2.Components.DiscretionInstructions(required=False)
                self.StrategyParametersGrp = FIX50SP2.Components.StrategyParametersGrp(required=False)
                self.CommissionData = FIX50SP2.Components.CommissionData(required=False)
                self.TrdRegTimestamps = FIX50SP2.Components.TrdRegTimestamps(required=False)

        class OrderStatusRequest(AppMessage):
            MsgType = "H"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "H"
                self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.ClOrdLinkID = FIX50SP2.Tags.ClOrdLinkID(required=False)
                self.OrdStatusReqID = FIX50SP2.Tags.OrdStatusReqID(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.Side = FIX50SP2.Tags.Side(required=True)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)

        class AllocationInstruction(AppMessage):
            MsgType = "J"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "J"
                self.AllocID = FIX50SP2.Tags.AllocID(required=True)
                self.AllocTransType = FIX50SP2.Tags.AllocTransType(required=True)
                self.AllocType = FIX50SP2.Tags.AllocType(required=True)
                self.SecondaryAllocID = FIX50SP2.Tags.SecondaryAllocID(required=False)
                self.RefAllocID = FIX50SP2.Tags.RefAllocID(required=False)
                self.AllocCancReplaceReason = FIX50SP2.Tags.AllocCancReplaceReason(required=False)
                self.AllocIntermedReqType = FIX50SP2.Tags.AllocIntermedReqType(required=False)
                self.AllocLinkID = FIX50SP2.Tags.AllocLinkID(required=False)
                self.AllocLinkType = FIX50SP2.Tags.AllocLinkType(required=False)
                self.BookingRefID = FIX50SP2.Tags.BookingRefID(required=False)
                self.AllocNoOrdersType = FIX50SP2.Tags.AllocNoOrdersType(required=False)
                self.PreviouslyReported = FIX50SP2.Tags.PreviouslyReported(required=False)
                self.ReversalIndicator = FIX50SP2.Tags.ReversalIndicator(required=False)
                self.MatchType = FIX50SP2.Tags.MatchType(required=False)
                self.Side = FIX50SP2.Tags.Side(required=True)
                self.Quantity = FIX50SP2.Tags.Quantity(required=True)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.LastMkt = FIX50SP2.Tags.LastMkt(required=False)
                self.TradeOriginationDate = FIX50SP2.Tags.TradeOriginationDate(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.AvgPx = FIX50SP2.Tags.AvgPx(required=False)
                self.AvgParPx = FIX50SP2.Tags.AvgParPx(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.AvgPxPrecision = FIX50SP2.Tags.AvgPxPrecision(required=False)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=True)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.BookingType = FIX50SP2.Tags.BookingType(required=False)
                self.GrossTradeAmt = FIX50SP2.Tags.GrossTradeAmt(required=False)
                self.Concession = FIX50SP2.Tags.Concession(required=False)
                self.TotalTakedown = FIX50SP2.Tags.TotalTakedown(required=False)
                self.NetMoney = FIX50SP2.Tags.NetMoney(required=False)
                self.PositionEffect = FIX50SP2.Tags.PositionEffect(required=False)
                self.AutoAcceptIndicator = FIX50SP2.Tags.AutoAcceptIndicator(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.NumDaysInterest = FIX50SP2.Tags.NumDaysInterest(required=False)
                self.AccruedInterestRate = FIX50SP2.Tags.AccruedInterestRate(required=False)
                self.AccruedInterestAmt = FIX50SP2.Tags.AccruedInterestAmt(required=False)
                self.TotalAccruedInterestAmt = FIX50SP2.Tags.TotalAccruedInterestAmt(required=False)
                self.InterestAtMaturity = FIX50SP2.Tags.InterestAtMaturity(required=False)
                self.EndAccruedInterestAmt = FIX50SP2.Tags.EndAccruedInterestAmt(required=False)
                self.StartCash = FIX50SP2.Tags.StartCash(required=False)
                self.EndCash = FIX50SP2.Tags.EndCash(required=False)
                self.LegalConfirm = FIX50SP2.Tags.LegalConfirm(required=False)
                self.TotNoAllocs = FIX50SP2.Tags.TotNoAllocs(required=False)
                self.LastFragment = FIX50SP2.Tags.LastFragment(required=False)
                self.AvgPxIndicator = FIX50SP2.Tags.AvgPxIndicator(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.TrdType = FIX50SP2.Tags.TrdType(required=False)
                self.TrdSubType = FIX50SP2.Tags.TrdSubType(required=False)
                self.CustOrderCapacity = FIX50SP2.Tags.CustOrderCapacity(required=False)
                self.TradeInputSource = FIX50SP2.Tags.TradeInputSource(required=False)
                self.MultiLegReportingType = FIX50SP2.Tags.MultiLegReportingType(required=False)
                self.MessageEventSource = FIX50SP2.Tags.MessageEventSource(required=False)
                self.RndPx = FIX50SP2.Tags.RndPx(required=False)
                self.OrdAllocGrp = FIX50SP2.Components.OrdAllocGrp(required=False)
                self.ExecAllocGrp = FIX50SP2.Components.ExecAllocGrp(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.InstrumentExtension = FIX50SP2.Components.InstrumentExtension(required=False)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                self.YieldData = FIX50SP2.Components.YieldData(required=False)
                self.PositionAmountData = FIX50SP2.Components.PositionAmountData(required=False)
                self.AllocGrp = FIX50SP2.Components.AllocGrp(required=False)
                self.RateSource = FIX50SP2.Components.RateSource(required=False)

        class ListCancelRequest(AppMessage):
            MsgType = "K"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "K"
                self.ListID = FIX50SP2.Tags.ListID(required=True)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.TradeOriginationDate = FIX50SP2.Tags.TradeOriginationDate(required=False)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)

        class ListExecute(AppMessage):
            MsgType = "L"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "L"
                self.ListID = FIX50SP2.Tags.ListID(required=True)
                self.ClientBidID = FIX50SP2.Tags.ClientBidID(required=False)
                self.BidID = FIX50SP2.Tags.BidID(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)

        class ListStatusRequest(AppMessage):
            MsgType = "M"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "M"
                self.ListID = FIX50SP2.Tags.ListID(required=True)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)

        class ListStatus(AppMessage):
            MsgType = "N"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "N"
                self.ListID = FIX50SP2.Tags.ListID(required=True)
                self.ListStatusType = FIX50SP2.Tags.ListStatusType(required=True)
                self.NoRpts = FIX50SP2.Tags.NoRpts(required=True)
                self.ListOrderStatus = FIX50SP2.Tags.ListOrderStatus(required=True)
                self.ContingencyType = FIX50SP2.Tags.ContingencyType(required=False)
                self.ListRejectReason = FIX50SP2.Tags.ListRejectReason(required=False)
                self.RptSeq = FIX50SP2.Tags.RptSeq(required=True)
                self.ListStatusText = FIX50SP2.Tags.ListStatusText(required=False)
                self.EncodedListStatusTextLen = FIX50SP2.Tags.EncodedListStatusTextLen(required=False)
                self.EncodedListStatusText = FIX50SP2.Tags.EncodedListStatusText(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.TotNoOrders = FIX50SP2.Tags.TotNoOrders(required=True)
                self.LastFragment = FIX50SP2.Tags.LastFragment(required=False)
                self.OrdListStatGrp = FIX50SP2.Components.OrdListStatGrp(required=True)

        class AllocationInstructionAck(AppMessage):
            MsgType = "P"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "P"
                self.AllocID = FIX50SP2.Tags.AllocID(required=True)
                self.SecondaryAllocID = FIX50SP2.Tags.SecondaryAllocID(required=False)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.AllocStatus = FIX50SP2.Tags.AllocStatus(required=True)
                self.AllocRejCode = FIX50SP2.Tags.AllocRejCode(required=False)
                self.AllocType = FIX50SP2.Tags.AllocType(required=False)
                self.AllocIntermedReqType = FIX50SP2.Tags.AllocIntermedReqType(required=False)
                self.MatchStatus = FIX50SP2.Tags.MatchStatus(required=False)
                self.Product = FIX50SP2.Tags.Product(required=False)
                self.SecurityType = FIX50SP2.Tags.SecurityType(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.AllocAckGrp = FIX50SP2.Components.AllocAckGrp(required=False)

        class DontKnowTrade(AppMessage):
            MsgType = "Q"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "Q"
                self.OrderID = FIX50SP2.Tags.OrderID(required=True)
                self.SecondaryOrderID = FIX50SP2.Tags.SecondaryOrderID(required=False)
                self.ExecID = FIX50SP2.Tags.ExecID(required=True)
                self.DKReason = FIX50SP2.Tags.DKReason(required=True)
                self.Side = FIX50SP2.Tags.Side(required=True)
                self.LastQty = FIX50SP2.Tags.LastQty(required=False)
                self.LastPx = FIX50SP2.Tags.LastPx(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.OrderQtyData = FIX50SP2.Components.OrderQtyData(required=True)

        class QuoteRequest(AppMessage):
            MsgType = "R"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "R"
                self.QuoteReqID = FIX50SP2.Tags.QuoteReqID(required=True)
                self.RFQReqID = FIX50SP2.Tags.RFQReqID(required=False)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.OrderCapacity = FIX50SP2.Tags.OrderCapacity(required=False)
                self.PrivateQuote = FIX50SP2.Tags.PrivateQuote(required=False)
                self.RespondentType = FIX50SP2.Tags.RespondentType(required=False)
                self.PreTradeAnonymity = FIX50SP2.Tags.PreTradeAnonymity(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.BookingType = FIX50SP2.Tags.BookingType(required=False)
                self.OrderRestrictions = FIX50SP2.Tags.OrderRestrictions(required=False)
                self.RootParties = FIX50SP2.Components.RootParties(required=False)
                self.QuotReqGrp = FIX50SP2.Components.QuotReqGrp(required=True)

        class Quote(AppMessage):
            MsgType = "S"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "S"
                self.QuoteReqID = FIX50SP2.Tags.QuoteReqID(required=False)
                self.QuoteID = FIX50SP2.Tags.QuoteID(required=True)
                self.QuoteMsgID = FIX50SP2.Tags.QuoteMsgID(required=False)
                self.QuoteRespID = FIX50SP2.Tags.QuoteRespID(required=False)
                self.QuoteType = FIX50SP2.Tags.QuoteType(required=False)
                self.PrivateQuote = FIX50SP2.Tags.PrivateQuote(required=False)
                self.QuoteResponseLevel = FIX50SP2.Tags.QuoteResponseLevel(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.Side = FIX50SP2.Tags.Side(required=False)
                self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.SettlDate2 = FIX50SP2.Tags.SettlDate2(required=False)
                self.OrderQty2 = FIX50SP2.Tags.OrderQty2(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.BidPx = FIX50SP2.Tags.BidPx(required=False)
                self.OfferPx = FIX50SP2.Tags.OfferPx(required=False)
                self.MktBidPx = FIX50SP2.Tags.MktBidPx(required=False)
                self.MktOfferPx = FIX50SP2.Tags.MktOfferPx(required=False)
                self.MinBidSize = FIX50SP2.Tags.MinBidSize(required=False)
                self.BidSize = FIX50SP2.Tags.BidSize(required=False)
                self.MinOfferSize = FIX50SP2.Tags.MinOfferSize(required=False)
                self.OfferSize = FIX50SP2.Tags.OfferSize(required=False)
                self.MinQty = FIX50SP2.Tags.MinQty(required=False)
                self.ValidUntilTime = FIX50SP2.Tags.ValidUntilTime(required=False)
                self.BidSpotRate = FIX50SP2.Tags.BidSpotRate(required=False)
                self.OfferSpotRate = FIX50SP2.Tags.OfferSpotRate(required=False)
                self.BidForwardPoints = FIX50SP2.Tags.BidForwardPoints(required=False)
                self.OfferForwardPoints = FIX50SP2.Tags.OfferForwardPoints(required=False)
                self.BidSwapPoints = FIX50SP2.Tags.BidSwapPoints(required=False)
                self.OfferSwapPoints = FIX50SP2.Tags.OfferSwapPoints(required=False)
                self.MidPx = FIX50SP2.Tags.MidPx(required=False)
                self.BidYield = FIX50SP2.Tags.BidYield(required=False)
                self.MidYield = FIX50SP2.Tags.MidYield(required=False)
                self.OfferYield = FIX50SP2.Tags.OfferYield(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.OrdType = FIX50SP2.Tags.OrdType(required=False)
                self.BidForwardPoints2 = FIX50SP2.Tags.BidForwardPoints2(required=False)
                self.OfferForwardPoints2 = FIX50SP2.Tags.OfferForwardPoints2(required=False)
                self.SettlCurrBidFxRate = FIX50SP2.Tags.SettlCurrBidFxRate(required=False)
                self.SettlCurrOfferFxRate = FIX50SP2.Tags.SettlCurrOfferFxRate(required=False)
                self.SettlCurrFxRateCalc = FIX50SP2.Tags.SettlCurrFxRateCalc(required=False)
                self.CommType = FIX50SP2.Tags.CommType(required=False)
                self.Commission = FIX50SP2.Tags.Commission(required=False)
                self.CustOrderCapacity = FIX50SP2.Tags.CustOrderCapacity(required=False)
                self.ExDestination = FIX50SP2.Tags.ExDestination(required=False)
                self.ExDestinationIDSource = FIX50SP2.Tags.ExDestinationIDSource(required=False)
                self.OrderCapacity = FIX50SP2.Tags.OrderCapacity(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.BookingType = FIX50SP2.Tags.BookingType(required=False)
                self.OrderRestrictions = FIX50SP2.Tags.OrderRestrictions(required=False)
                self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                self.QuotQualGrp = FIX50SP2.Components.QuotQualGrp(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.OrderQtyData = FIX50SP2.Components.OrderQtyData(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                self.LegQuotGrp = FIX50SP2.Components.LegQuotGrp(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.YieldData = FIX50SP2.Components.YieldData(required=False)
                self.RateSource = FIX50SP2.Components.RateSource(required=False)

        class SettlementInstructions(AppMessage):
            MsgType = "T"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "T"
                self.SettlInstMsgID = FIX50SP2.Tags.SettlInstMsgID(required=True)
                self.SettlInstReqID = FIX50SP2.Tags.SettlInstReqID(required=False)
                self.SettlInstMode = FIX50SP2.Tags.SettlInstMode(required=True)
                self.SettlInstReqRejCode = FIX50SP2.Tags.SettlInstReqRejCode(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.SettlInstGrp = FIX50SP2.Components.SettlInstGrp(required=False)

        class MarketDataRequest(AppMessage):
            MsgType = "V"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "V"
                self.MDReqID = FIX50SP2.Tags.MDReqID(required=True)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=True)
                self.MarketDepth = FIX50SP2.Tags.MarketDepth(required=True)
                self.MDUpdateType = FIX50SP2.Tags.MDUpdateType(required=False)
                self.AggregatedBook = FIX50SP2.Tags.AggregatedBook(required=False)
                self.OpenCloseSettlFlag = FIX50SP2.Tags.OpenCloseSettlFlag(required=False)
                self.Scope = FIX50SP2.Tags.Scope(required=False)
                self.MDImplicitDelete = FIX50SP2.Tags.MDImplicitDelete(required=False)
                self.ApplQueueAction = FIX50SP2.Tags.ApplQueueAction(required=False)
                self.ApplQueueMax = FIX50SP2.Tags.ApplQueueMax(required=False)
                self.MDQuoteType = FIX50SP2.Tags.MDQuoteType(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.MDReqGrp = FIX50SP2.Components.MDReqGrp(required=True)
                self.InstrmtMDReqGrp = FIX50SP2.Components.InstrmtMDReqGrp(required=True)
                self.TrdgSesGrp = FIX50SP2.Components.TrdgSesGrp(required=False)

        class MarketDataSnapshotFullRefresh(AppMessage):
            MsgType = "W"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "W"
                self.TotNumReports = FIX50SP2.Tags.TotNumReports(required=False)
                self.MDReportID = FIX50SP2.Tags.MDReportID(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.MDBookType = FIX50SP2.Tags.MDBookType(required=False)
                self.MDSubBookType = FIX50SP2.Tags.MDSubBookType(required=False)
                self.MarketDepth = FIX50SP2.Tags.MarketDepth(required=False)
                self.MDFeedType = FIX50SP2.Tags.MDFeedType(required=False)
                self.RefreshIndicator = FIX50SP2.Tags.RefreshIndicator(required=False)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                self.MDReqID = FIX50SP2.Tags.MDReqID(required=False)
                self.FinancialStatus = FIX50SP2.Tags.FinancialStatus(required=False)
                self.CorporateAction = FIX50SP2.Tags.CorporateAction(required=False)
                self.NetChgPrevDay = FIX50SP2.Tags.NetChgPrevDay(required=False)
                self.ApplQueueDepth = FIX50SP2.Tags.ApplQueueDepth(required=False)
                self.ApplQueueResolution = FIX50SP2.Tags.ApplQueueResolution(required=False)
                self.MDStreamID = FIX50SP2.Tags.MDStreamID(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.MDFullGrp = FIX50SP2.Components.MDFullGrp(required=True)
                self.RoutingGrp = FIX50SP2.Components.RoutingGrp(required=False)

        class MarketDataIncrementalRefresh(AppMessage):
            MsgType = "X"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "X"
                self.MDBookType = FIX50SP2.Tags.MDBookType(required=False)
                self.MDFeedType = FIX50SP2.Tags.MDFeedType(required=False)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                self.MDReqID = FIX50SP2.Tags.MDReqID(required=False)
                self.ApplQueueDepth = FIX50SP2.Tags.ApplQueueDepth(required=False)
                self.ApplQueueResolution = FIX50SP2.Tags.ApplQueueResolution(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.MDIncGrp = FIX50SP2.Components.MDIncGrp(required=True)
                self.RoutingGrp = FIX50SP2.Components.RoutingGrp(required=False)

        class MarketDataRequestReject(AppMessage):
            MsgType = "Y"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "Y"
                self.MDReqID = FIX50SP2.Tags.MDReqID(required=True)
                self.MDReqRejReason = FIX50SP2.Tags.MDReqRejReason(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.MDRjctGrp = FIX50SP2.Components.MDRjctGrp(required=False)

        class QuoteCancel(AppMessage):
            MsgType = "Z"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "Z"
                self.QuoteReqID = FIX50SP2.Tags.QuoteReqID(required=False)
                self.QuoteID = FIX50SP2.Tags.QuoteID(required=False)
                self.QuoteMsgID = FIX50SP2.Tags.QuoteMsgID(required=False)
                self.QuoteCancelType = FIX50SP2.Tags.QuoteCancelType(required=True)
                self.QuoteResponseLevel = FIX50SP2.Tags.QuoteResponseLevel(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.QuoteType = FIX50SP2.Tags.QuoteType(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.QuotCxlEntriesGrp = FIX50SP2.Components.QuotCxlEntriesGrp(required=False)
                self.TargetParties = FIX50SP2.Components.TargetParties(required=False)

        class QuoteStatusRequest(AppMessage):
            MsgType = "a"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "a"
                self.QuoteStatusReqID = FIX50SP2.Tags.QuoteStatusReqID(required=False)
                self.QuoteID = FIX50SP2.Tags.QuoteID(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.TargetParties = FIX50SP2.Components.TargetParties(required=False)

        class MassQuoteAcknowledgement(AppMessage):
            MsgType = "b"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "b"
                self.QuoteReqID = FIX50SP2.Tags.QuoteReqID(required=False)
                self.QuoteID = FIX50SP2.Tags.QuoteID(required=False)
                self.QuoteStatus = FIX50SP2.Tags.QuoteStatus(required=True)
                self.QuoteRejectReason = FIX50SP2.Tags.QuoteRejectReason(required=False)
                self.QuoteResponseLevel = FIX50SP2.Tags.QuoteResponseLevel(required=False)
                self.QuoteType = FIX50SP2.Tags.QuoteType(required=False)
                self.QuoteCancelType = FIX50SP2.Tags.QuoteCancelType(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.QuotSetAckGrp = FIX50SP2.Components.QuotSetAckGrp(required=False)
                self.TargetParties = FIX50SP2.Components.TargetParties(required=False)

        class SecurityDefinitionRequest(AppMessage):
            MsgType = "c"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "c"
                self.SecurityReqID = FIX50SP2.Tags.SecurityReqID(required=True)
                self.SecurityRequestType = FIX50SP2.Tags.SecurityRequestType(required=True)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.ExpirationCycle = FIX50SP2.Tags.ExpirationCycle(required=False)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.InstrumentExtension = FIX50SP2.Components.InstrumentExtension(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.YieldData = FIX50SP2.Components.YieldData(required=False)

        class SecurityDefinition(AppMessage):
            MsgType = "d"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "d"
                self.SecurityReportID = FIX50SP2.Tags.SecurityReportID(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.SecurityReqID = FIX50SP2.Tags.SecurityReqID(required=False)
                self.SecurityResponseID = FIX50SP2.Tags.SecurityResponseID(required=False)
                self.SecurityResponseType = FIX50SP2.Tags.SecurityResponseType(required=False)
                self.CorporateAction = FIX50SP2.Tags.CorporateAction(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.InstrumentExtension = FIX50SP2.Components.InstrumentExtension(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.YieldData = FIX50SP2.Components.YieldData(required=False)
                self.MarketSegmentGrp = FIX50SP2.Components.MarketSegmentGrp(required=False)

        class SecurityStatusRequest(AppMessage):
            MsgType = "e"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "e"
                self.SecurityStatusReqID = FIX50SP2.Tags.SecurityStatusReqID(required=True)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=True)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.InstrumentExtension = FIX50SP2.Components.InstrumentExtension(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)

        class SecurityStatus(AppMessage):
            MsgType = "f"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "f"
                self.SecurityStatusReqID = FIX50SP2.Tags.SecurityStatusReqID(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.UnsolicitedIndicator = FIX50SP2.Tags.UnsolicitedIndicator(required=False)
                self.SecurityTradingStatus = FIX50SP2.Tags.SecurityTradingStatus(required=False)
                self.SecurityTradingEvent = FIX50SP2.Tags.SecurityTradingEvent(required=False)
                self.FinancialStatus = FIX50SP2.Tags.FinancialStatus(required=False)
                self.CorporateAction = FIX50SP2.Tags.CorporateAction(required=False)
                self.HaltReasonInt = FIX50SP2.Tags.HaltReasonInt(required=False)
                self.InViewOfCommon = FIX50SP2.Tags.InViewOfCommon(required=False)
                self.DueToRelated = FIX50SP2.Tags.DueToRelated(required=False)
                self.MDBookType = FIX50SP2.Tags.MDBookType(required=False)
                self.MarketDepth = FIX50SP2.Tags.MarketDepth(required=False)
                self.BuyVolume = FIX50SP2.Tags.BuyVolume(required=False)
                self.SellVolume = FIX50SP2.Tags.SellVolume(required=False)
                self.HighPx = FIX50SP2.Tags.HighPx(required=False)
                self.LowPx = FIX50SP2.Tags.LowPx(required=False)
                self.LastPx = FIX50SP2.Tags.LastPx(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.Adjustment = FIX50SP2.Tags.Adjustment(required=False)
                self.FirstPx = FIX50SP2.Tags.FirstPx(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.InstrumentExtension = FIX50SP2.Components.InstrumentExtension(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)

        class TradingSessionStatusRequest(AppMessage):
            MsgType = "g"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "g"
                self.TradSesReqID = FIX50SP2.Tags.TradSesReqID(required=True)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.TradSesMethod = FIX50SP2.Tags.TradSesMethod(required=False)
                self.TradSesMode = FIX50SP2.Tags.TradSesMode(required=False)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=True)
                self.SecurityExchange = FIX50SP2.Tags.SecurityExchange(required=False)

        class TradingSessionStatus(AppMessage):
            MsgType = "h"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "h"
                self.TradSesReqID = FIX50SP2.Tags.TradSesReqID(required=False)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=True)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.TradSesMethod = FIX50SP2.Tags.TradSesMethod(required=False)
                self.TradSesMode = FIX50SP2.Tags.TradSesMode(required=False)
                self.UnsolicitedIndicator = FIX50SP2.Tags.UnsolicitedIndicator(required=False)
                self.TradSesStatus = FIX50SP2.Tags.TradSesStatus(required=True)
                self.TradSesEvent = FIX50SP2.Tags.TradSesEvent(required=False)
                self.TradSesStatusRejReason = FIX50SP2.Tags.TradSesStatusRejReason(required=False)
                self.TradSesStartTime = FIX50SP2.Tags.TradSesStartTime(required=False)
                self.TradSesOpenTime = FIX50SP2.Tags.TradSesOpenTime(required=False)
                self.TradSesPreCloseTime = FIX50SP2.Tags.TradSesPreCloseTime(required=False)
                self.TradSesCloseTime = FIX50SP2.Tags.TradSesCloseTime(required=False)
                self.TradSesEndTime = FIX50SP2.Tags.TradSesEndTime(required=False)
                self.TotalVolumeTraded = FIX50SP2.Tags.TotalVolumeTraded(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)

        class MassQuote(AppMessage):
            MsgType = "i"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "i"
                self.QuoteReqID = FIX50SP2.Tags.QuoteReqID(required=False)
                self.QuoteID = FIX50SP2.Tags.QuoteID(required=True)
                self.QuoteType = FIX50SP2.Tags.QuoteType(required=False)
                self.QuoteResponseLevel = FIX50SP2.Tags.QuoteResponseLevel(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.DefBidSize = FIX50SP2.Tags.DefBidSize(required=False)
                self.DefOfferSize = FIX50SP2.Tags.DefOfferSize(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.QuotSetGrp = FIX50SP2.Components.QuotSetGrp(required=True)

        class BusinessMessageReject(AppMessage):
            MsgType = "j"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "j"
                self.RefSeqNum = FIX50SP2.Tags.RefSeqNum(required=False)
                self.RefMsgType = FIX50SP2.Tags.RefMsgType(required=True)
                self.RefApplVerID = FIX50SP2.Tags.RefApplVerID(required=False)
                self.RefApplExtID = FIX50SP2.Tags.RefApplExtID(required=False)
                self.RefCstmApplVerID = FIX50SP2.Tags.RefCstmApplVerID(required=False)
                self.BusinessRejectRefID = FIX50SP2.Tags.BusinessRejectRefID(required=False)
                self.BusinessRejectReason = FIX50SP2.Tags.BusinessRejectReason(required=True)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)

        class BidRequest(AppMessage):
            MsgType = "k"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "k"
                self.BidID = FIX50SP2.Tags.BidID(required=False)
                self.ClientBidID = FIX50SP2.Tags.ClientBidID(required=True)
                self.BidRequestTransType = FIX50SP2.Tags.BidRequestTransType(required=True)
                self.ListName = FIX50SP2.Tags.ListName(required=False)
                self.TotNoRelatedSym = FIX50SP2.Tags.TotNoRelatedSym(required=True)
                self.BidType = FIX50SP2.Tags.BidType(required=True)
                self.NumTickets = FIX50SP2.Tags.NumTickets(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.SideValue1 = FIX50SP2.Tags.SideValue1(required=False)
                self.SideValue2 = FIX50SP2.Tags.SideValue2(required=False)
                self.LiquidityIndType = FIX50SP2.Tags.LiquidityIndType(required=False)
                self.WtAverageLiquidity = FIX50SP2.Tags.WtAverageLiquidity(required=False)
                self.ExchangeForPhysical = FIX50SP2.Tags.ExchangeForPhysical(required=False)
                self.OutMainCntryUIndex = FIX50SP2.Tags.OutMainCntryUIndex(required=False)
                self.CrossPercent = FIX50SP2.Tags.CrossPercent(required=False)
                self.ProgRptReqs = FIX50SP2.Tags.ProgRptReqs(required=False)
                self.ProgPeriodInterval = FIX50SP2.Tags.ProgPeriodInterval(required=False)
                self.IncTaxInd = FIX50SP2.Tags.IncTaxInd(required=False)
                self.ForexReq = FIX50SP2.Tags.ForexReq(required=False)
                self.NumBidders = FIX50SP2.Tags.NumBidders(required=False)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                self.BidTradeType = FIX50SP2.Tags.BidTradeType(required=True)
                self.BasisPxType = FIX50SP2.Tags.BasisPxType(required=True)
                self.StrikeTime = FIX50SP2.Tags.StrikeTime(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.BidDescReqGrp = FIX50SP2.Components.BidDescReqGrp(required=False)
                self.BidCompReqGrp = FIX50SP2.Components.BidCompReqGrp(required=False)

        class BidResponse(AppMessage):
            MsgType = "l"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "l"
                self.BidID = FIX50SP2.Tags.BidID(required=False)
                self.ClientBidID = FIX50SP2.Tags.ClientBidID(required=False)
                self.BidCompRspGrp = FIX50SP2.Components.BidCompRspGrp(required=True)

        class ListStrikePrice(AppMessage):
            MsgType = "m"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "m"
                self.ListID = FIX50SP2.Tags.ListID(required=True)
                self.TotNoStrikes = FIX50SP2.Tags.TotNoStrikes(required=True)
                self.LastFragment = FIX50SP2.Tags.LastFragment(required=False)
                self.InstrmtStrkPxGrp = FIX50SP2.Components.InstrmtStrkPxGrp(required=True)

        class RegistrationInstructions(AppMessage):
            MsgType = "o"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "o"
                self.RegistID = FIX50SP2.Tags.RegistID(required=True)
                self.RegistTransType = FIX50SP2.Tags.RegistTransType(required=True)
                self.RegistRefID = FIX50SP2.Tags.RegistRefID(required=True)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.RegistAcctType = FIX50SP2.Tags.RegistAcctType(required=False)
                self.TaxAdvantageType = FIX50SP2.Tags.TaxAdvantageType(required=False)
                self.OwnershipType = FIX50SP2.Tags.OwnershipType(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.RgstDtlsGrp = FIX50SP2.Components.RgstDtlsGrp(required=False)
                self.RgstDistInstGrp = FIX50SP2.Components.RgstDistInstGrp(required=False)

        class RegistrationInstructionsResponse(AppMessage):
            MsgType = "p"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "p"
                self.RegistID = FIX50SP2.Tags.RegistID(required=True)
                self.RegistTransType = FIX50SP2.Tags.RegistTransType(required=True)
                self.RegistRefID = FIX50SP2.Tags.RegistRefID(required=True)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.RegistStatus = FIX50SP2.Tags.RegistStatus(required=True)
                self.RegistRejReasonCode = FIX50SP2.Tags.RegistRejReasonCode(required=False)
                self.RegistRejReasonText = FIX50SP2.Tags.RegistRejReasonText(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)

        class OrderMassCancelRequest(AppMessage):
            MsgType = "q"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "q"
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=True)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.MassCancelRequestType = FIX50SP2.Tags.MassCancelRequestType(required=True)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.Side = FIX50SP2.Tags.Side(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.UnderlyingInstrument = FIX50SP2.Components.UnderlyingInstrument(required=False)
                self.TargetParties = FIX50SP2.Components.TargetParties(required=False)

        class OrderMassCancelReport(AppMessage):
            MsgType = "r"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "r"
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.OrderID = FIX50SP2.Tags.OrderID(required=True)
                self.MassActionReportID = FIX50SP2.Tags.MassActionReportID(required=True)
                self.SecondaryOrderID = FIX50SP2.Tags.SecondaryOrderID(required=False)
                self.MassCancelRequestType = FIX50SP2.Tags.MassCancelRequestType(required=True)
                self.MassCancelResponse = FIX50SP2.Tags.MassCancelResponse(required=True)
                self.MassCancelRejectReason = FIX50SP2.Tags.MassCancelRejectReason(required=False)
                self.TotalAffectedOrders = FIX50SP2.Tags.TotalAffectedOrders(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.Side = FIX50SP2.Tags.Side(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.AffectedOrdGrp = FIX50SP2.Components.AffectedOrdGrp(required=False)
                self.NotAffectedOrdersGrp = FIX50SP2.Components.NotAffectedOrdersGrp(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.UnderlyingInstrument = FIX50SP2.Components.UnderlyingInstrument(required=False)
                self.TargetParties = FIX50SP2.Components.TargetParties(required=False)

        class NewOrderCross(AppMessage):
            MsgType = "s"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "s"
                self.CrossID = FIX50SP2.Tags.CrossID(required=True)
                self.CrossType = FIX50SP2.Tags.CrossType(required=True)
                self.CrossPrioritization = FIX50SP2.Tags.CrossPrioritization(required=True)
                self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.HandlInst = FIX50SP2.Tags.HandlInst(required=False)
                self.ExecInst = FIX50SP2.Tags.ExecInst(required=False)
                self.MinQty = FIX50SP2.Tags.MinQty(required=False)
                self.MatchIncrement = FIX50SP2.Tags.MatchIncrement(required=False)
                self.MaxPriceLevels = FIX50SP2.Tags.MaxPriceLevels(required=False)
                self.MaxFloor = FIX50SP2.Tags.MaxFloor(required=False)
                self.ExDestination = FIX50SP2.Tags.ExDestination(required=False)
                self.ExDestinationIDSource = FIX50SP2.Tags.ExDestinationIDSource(required=False)
                self.ProcessCode = FIX50SP2.Tags.ProcessCode(required=False)
                self.PrevClosePx = FIX50SP2.Tags.PrevClosePx(required=False)
                self.LocateReqd = FIX50SP2.Tags.LocateReqd(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.TransBkdTime = FIX50SP2.Tags.TransBkdTime(required=False)
                self.OrdType = FIX50SP2.Tags.OrdType(required=True)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.Price = FIX50SP2.Tags.Price(required=False)
                self.PriceProtectionScope = FIX50SP2.Tags.PriceProtectionScope(required=False)
                self.StopPx = FIX50SP2.Tags.StopPx(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.ComplianceID = FIX50SP2.Tags.ComplianceID(required=False)
                self.IOIID = FIX50SP2.Tags.IOIID(required=False)
                self.QuoteID = FIX50SP2.Tags.QuoteID(required=False)
                self.TimeInForce = FIX50SP2.Tags.TimeInForce(required=False)
                self.EffectiveTime = FIX50SP2.Tags.EffectiveTime(required=False)
                self.ExpireDate = FIX50SP2.Tags.ExpireDate(required=False)
                self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                self.GTBookingInst = FIX50SP2.Tags.GTBookingInst(required=False)
                self.MaxShow = FIX50SP2.Tags.MaxShow(required=False)
                self.TargetStrategy = FIX50SP2.Tags.TargetStrategy(required=False)
                self.TargetStrategyParameters = FIX50SP2.Tags.TargetStrategyParameters(required=False)
                self.ParticipationRate = FIX50SP2.Tags.ParticipationRate(required=False)
                self.CancellationRights = FIX50SP2.Tags.CancellationRights(required=False)
                self.MoneyLaunderingStatus = FIX50SP2.Tags.MoneyLaunderingStatus(required=False)
                self.RegistID = FIX50SP2.Tags.RegistID(required=False)
                self.Designation = FIX50SP2.Tags.Designation(required=False)
                self.RootParties = FIX50SP2.Components.RootParties(required=False)
                self.SideCrossOrdModGrp = FIX50SP2.Components.SideCrossOrdModGrp(required=True)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.DisplayInstruction = FIX50SP2.Components.DisplayInstruction(required=False)
                self.TrdgSesGrp = FIX50SP2.Components.TrdgSesGrp(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                self.TriggeringInstruction = FIX50SP2.Components.TriggeringInstruction(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.YieldData = FIX50SP2.Components.YieldData(required=False)
                self.PegInstructions = FIX50SP2.Components.PegInstructions(required=False)
                self.DiscretionInstructions = FIX50SP2.Components.DiscretionInstructions(required=False)
                self.StrategyParametersGrp = FIX50SP2.Components.StrategyParametersGrp(required=False)

        class CrossOrderCancelReplaceRequest(AppMessage):
            MsgType = "t"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "t"
                self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                self.CrossID = FIX50SP2.Tags.CrossID(required=True)
                self.OrigCrossID = FIX50SP2.Tags.OrigCrossID(required=True)
                self.HostCrossID = FIX50SP2.Tags.HostCrossID(required=False)
                self.CrossType = FIX50SP2.Tags.CrossType(required=True)
                self.CrossPrioritization = FIX50SP2.Tags.CrossPrioritization(required=True)
                self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.HandlInst = FIX50SP2.Tags.HandlInst(required=False)
                self.ExecInst = FIX50SP2.Tags.ExecInst(required=False)
                self.MinQty = FIX50SP2.Tags.MinQty(required=False)
                self.MatchIncrement = FIX50SP2.Tags.MatchIncrement(required=False)
                self.MaxPriceLevels = FIX50SP2.Tags.MaxPriceLevels(required=False)
                self.MaxFloor = FIX50SP2.Tags.MaxFloor(required=False)
                self.ExDestination = FIX50SP2.Tags.ExDestination(required=False)
                self.ExDestinationIDSource = FIX50SP2.Tags.ExDestinationIDSource(required=False)
                self.ProcessCode = FIX50SP2.Tags.ProcessCode(required=False)
                self.PrevClosePx = FIX50SP2.Tags.PrevClosePx(required=False)
                self.LocateReqd = FIX50SP2.Tags.LocateReqd(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.TransBkdTime = FIX50SP2.Tags.TransBkdTime(required=False)
                self.OrdType = FIX50SP2.Tags.OrdType(required=True)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.Price = FIX50SP2.Tags.Price(required=False)
                self.PriceProtectionScope = FIX50SP2.Tags.PriceProtectionScope(required=False)
                self.StopPx = FIX50SP2.Tags.StopPx(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.ComplianceID = FIX50SP2.Tags.ComplianceID(required=False)
                self.IOIID = FIX50SP2.Tags.IOIID(required=False)
                self.QuoteID = FIX50SP2.Tags.QuoteID(required=False)
                self.TimeInForce = FIX50SP2.Tags.TimeInForce(required=False)
                self.EffectiveTime = FIX50SP2.Tags.EffectiveTime(required=False)
                self.ExpireDate = FIX50SP2.Tags.ExpireDate(required=False)
                self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                self.GTBookingInst = FIX50SP2.Tags.GTBookingInst(required=False)
                self.MaxShow = FIX50SP2.Tags.MaxShow(required=False)
                self.TargetStrategy = FIX50SP2.Tags.TargetStrategy(required=False)
                self.TargetStrategyParameters = FIX50SP2.Tags.TargetStrategyParameters(required=False)
                self.ParticipationRate = FIX50SP2.Tags.ParticipationRate(required=False)
                self.CancellationRights = FIX50SP2.Tags.CancellationRights(required=False)
                self.MoneyLaunderingStatus = FIX50SP2.Tags.MoneyLaunderingStatus(required=False)
                self.RegistID = FIX50SP2.Tags.RegistID(required=False)
                self.Designation = FIX50SP2.Tags.Designation(required=False)
                self.RootParties = FIX50SP2.Components.RootParties(required=False)
                self.SideCrossOrdModGrp = FIX50SP2.Components.SideCrossOrdModGrp(required=True)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.DisplayInstruction = FIX50SP2.Components.DisplayInstruction(required=False)
                self.TrdgSesGrp = FIX50SP2.Components.TrdgSesGrp(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                self.TriggeringInstruction = FIX50SP2.Components.TriggeringInstruction(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.YieldData = FIX50SP2.Components.YieldData(required=False)
                self.PegInstructions = FIX50SP2.Components.PegInstructions(required=False)
                self.DiscretionInstructions = FIX50SP2.Components.DiscretionInstructions(required=False)
                self.StrategyParametersGrp = FIX50SP2.Components.StrategyParametersGrp(required=False)

        class CrossOrderCancelRequest(AppMessage):
            MsgType = "u"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "u"
                self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                self.CrossID = FIX50SP2.Tags.CrossID(required=True)
                self.OrigCrossID = FIX50SP2.Tags.OrigCrossID(required=True)
                self.HostCrossID = FIX50SP2.Tags.HostCrossID(required=False)
                self.CrossType = FIX50SP2.Tags.CrossType(required=True)
                self.CrossPrioritization = FIX50SP2.Tags.CrossPrioritization(required=True)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.RootParties = FIX50SP2.Components.RootParties(required=False)
                self.SideCrossOrdCxlGrp = FIX50SP2.Components.SideCrossOrdCxlGrp(required=True)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)

        class SecurityTypeRequest(AppMessage):
            MsgType = "v"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "v"
                self.SecurityReqID = FIX50SP2.Tags.SecurityReqID(required=True)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.Product = FIX50SP2.Tags.Product(required=False)
                self.SecurityType = FIX50SP2.Tags.SecurityType(required=False)
                self.SecuritySubType = FIX50SP2.Tags.SecuritySubType(required=False)

        class SecurityTypes(AppMessage):
            MsgType = "w"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "w"
                self.SecurityReqID = FIX50SP2.Tags.SecurityReqID(required=True)
                self.SecurityResponseID = FIX50SP2.Tags.SecurityResponseID(required=True)
                self.SecurityResponseType = FIX50SP2.Tags.SecurityResponseType(required=True)
                self.TotNoSecurityTypes = FIX50SP2.Tags.TotNoSecurityTypes(required=False)
                self.LastFragment = FIX50SP2.Tags.LastFragment(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.SecTypesGrp = FIX50SP2.Components.SecTypesGrp(required=False)

        class SecurityListRequest(AppMessage):
            MsgType = "x"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "x"
                self.SecurityReqID = FIX50SP2.Tags.SecurityReqID(required=True)
                self.SecurityListRequestType = FIX50SP2.Tags.SecurityListRequestType(required=True)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=False)
                self.SecurityListID = FIX50SP2.Tags.SecurityListID(required=False)
                self.SecurityListType = FIX50SP2.Tags.SecurityListType(required=False)
                self.SecurityListTypeSource = FIX50SP2.Tags.SecurityListTypeSource(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.InstrumentExtension = FIX50SP2.Components.InstrumentExtension(required=False)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)

        class SecurityList(AppMessage):
            MsgType = "y"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "y"
                self.SecurityReportID = FIX50SP2.Tags.SecurityReportID(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.SecurityReqID = FIX50SP2.Tags.SecurityReqID(required=False)
                self.SecurityResponseID = FIX50SP2.Tags.SecurityResponseID(required=False)
                self.SecurityRequestResult = FIX50SP2.Tags.SecurityRequestResult(required=False)
                self.TotNoRelatedSym = FIX50SP2.Tags.TotNoRelatedSym(required=False)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.LastFragment = FIX50SP2.Tags.LastFragment(required=False)
                self.SecurityListID = FIX50SP2.Tags.SecurityListID(required=False)
                self.SecurityListRefID = FIX50SP2.Tags.SecurityListRefID(required=False)
                self.SecurityListDesc = FIX50SP2.Tags.SecurityListDesc(required=False)
                self.EncodedSecurityListDescLen = FIX50SP2.Tags.EncodedSecurityListDescLen(required=False)
                self.EncodedSecurityListDesc = FIX50SP2.Tags.EncodedSecurityListDesc(required=False)
                self.SecurityListType = FIX50SP2.Tags.SecurityListType(required=False)
                self.SecurityListTypeSource = FIX50SP2.Tags.SecurityListTypeSource(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.SecListGrp = FIX50SP2.Components.SecListGrp(required=False)

        class DerivativeSecurityListRequest(AppMessage):
            MsgType = "z"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "z"
                self.SecurityReqID = FIX50SP2.Tags.SecurityReqID(required=True)
                self.SecurityListRequestType = FIX50SP2.Tags.SecurityListRequestType(required=True)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.SecuritySubType = FIX50SP2.Tags.SecuritySubType(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=False)
                self.UnderlyingInstrument = FIX50SP2.Components.UnderlyingInstrument(required=False)
                self.DerivativeInstrument = FIX50SP2.Components.DerivativeInstrument(required=False)

        class DerivativeSecurityList(AppMessage):
            MsgType = "AA"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AA"
                self.SecurityReqID = FIX50SP2.Tags.SecurityReqID(required=False)
                self.SecurityResponseID = FIX50SP2.Tags.SecurityResponseID(required=False)
                self.SecurityRequestResult = FIX50SP2.Tags.SecurityRequestResult(required=False)
                self.TotNoRelatedSym = FIX50SP2.Tags.TotNoRelatedSym(required=False)
                self.LastFragment = FIX50SP2.Tags.LastFragment(required=False)
                self.SecurityReportID = FIX50SP2.Tags.SecurityReportID(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.UnderlyingInstrument = FIX50SP2.Components.UnderlyingInstrument(required=False)
                self.DerivativeSecurityDefinition = FIX50SP2.Components.DerivativeSecurityDefinition(required=False)
                self.RelSymDerivSecGrp = FIX50SP2.Components.RelSymDerivSecGrp(required=False)

        class NewOrderMultileg(AppMessage):
            MsgType = "AB"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AB"
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=True)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.ClOrdLinkID = FIX50SP2.Tags.ClOrdLinkID(required=False)
                self.TradeOriginationDate = FIX50SP2.Tags.TradeOriginationDate(required=False)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.DayBookingInst = FIX50SP2.Tags.DayBookingInst(required=False)
                self.BookingUnit = FIX50SP2.Tags.BookingUnit(required=False)
                self.PreallocMethod = FIX50SP2.Tags.PreallocMethod(required=False)
                self.AllocID = FIX50SP2.Tags.AllocID(required=False)
                self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.CashMargin = FIX50SP2.Tags.CashMargin(required=False)
                self.ClearingFeeIndicator = FIX50SP2.Tags.ClearingFeeIndicator(required=False)
                self.HandlInst = FIX50SP2.Tags.HandlInst(required=False)
                self.ExecInst = FIX50SP2.Tags.ExecInst(required=False)
                self.MinQty = FIX50SP2.Tags.MinQty(required=False)
                self.MatchIncrement = FIX50SP2.Tags.MatchIncrement(required=False)
                self.MaxPriceLevels = FIX50SP2.Tags.MaxPriceLevels(required=False)
                self.MaxFloor = FIX50SP2.Tags.MaxFloor(required=False)
                self.ExDestination = FIX50SP2.Tags.ExDestination(required=False)
                self.ExDestinationIDSource = FIX50SP2.Tags.ExDestinationIDSource(required=False)
                self.ProcessCode = FIX50SP2.Tags.ProcessCode(required=False)
                self.Side = FIX50SP2.Tags.Side(required=True)
                self.PrevClosePx = FIX50SP2.Tags.PrevClosePx(required=False)
                self.SwapPoints = FIX50SP2.Tags.SwapPoints(required=False)
                self.LocateReqd = FIX50SP2.Tags.LocateReqd(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.OrdType = FIX50SP2.Tags.OrdType(required=True)
                self.MultilegModel = FIX50SP2.Tags.MultilegModel(required=False)
                self.MultilegPriceMethod = FIX50SP2.Tags.MultilegPriceMethod(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.Price = FIX50SP2.Tags.Price(required=False)
                self.PriceProtectionScope = FIX50SP2.Tags.PriceProtectionScope(required=False)
                self.StopPx = FIX50SP2.Tags.StopPx(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.ComplianceID = FIX50SP2.Tags.ComplianceID(required=False)
                self.SolicitedFlag = FIX50SP2.Tags.SolicitedFlag(required=False)
                self.IOIID = FIX50SP2.Tags.IOIID(required=False)
                self.QuoteID = FIX50SP2.Tags.QuoteID(required=False)
                self.RefOrderID = FIX50SP2.Tags.RefOrderID(required=False)
                self.RefOrderIDSource = FIX50SP2.Tags.RefOrderIDSource(required=False)
                self.TimeInForce = FIX50SP2.Tags.TimeInForce(required=False)
                self.EffectiveTime = FIX50SP2.Tags.EffectiveTime(required=False)
                self.ExpireDate = FIX50SP2.Tags.ExpireDate(required=False)
                self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                self.GTBookingInst = FIX50SP2.Tags.GTBookingInst(required=False)
                self.OrderCapacity = FIX50SP2.Tags.OrderCapacity(required=False)
                self.OrderRestrictions = FIX50SP2.Tags.OrderRestrictions(required=False)
                self.PreTradeAnonymity = FIX50SP2.Tags.PreTradeAnonymity(required=False)
                self.CustOrderCapacity = FIX50SP2.Tags.CustOrderCapacity(required=False)
                self.ForexReq = FIX50SP2.Tags.ForexReq(required=False)
                self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                self.BookingType = FIX50SP2.Tags.BookingType(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.PositionEffect = FIX50SP2.Tags.PositionEffect(required=False)
                self.CoveredOrUncovered = FIX50SP2.Tags.CoveredOrUncovered(required=False)
                self.MaxShow = FIX50SP2.Tags.MaxShow(required=False)
                self.TargetStrategy = FIX50SP2.Tags.TargetStrategy(required=False)
                self.TargetStrategyParameters = FIX50SP2.Tags.TargetStrategyParameters(required=False)
                self.RiskFreeRate = FIX50SP2.Tags.RiskFreeRate(required=False)
                self.ParticipationRate = FIX50SP2.Tags.ParticipationRate(required=False)
                self.CancellationRights = FIX50SP2.Tags.CancellationRights(required=False)
                self.MoneyLaunderingStatus = FIX50SP2.Tags.MoneyLaunderingStatus(required=False)
                self.RegistID = FIX50SP2.Tags.RegistID(required=False)
                self.Designation = FIX50SP2.Tags.Designation(required=False)
                self.MultiLegRptTypeReq = FIX50SP2.Tags.MultiLegRptTypeReq(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.PreAllocMlegGrp = FIX50SP2.Components.PreAllocMlegGrp(required=False)
                self.DisplayInstruction = FIX50SP2.Components.DisplayInstruction(required=False)
                self.TrdgSesGrp = FIX50SP2.Components.TrdgSesGrp(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.LegOrdGrp = FIX50SP2.Components.LegOrdGrp(required=False)
                self.OrderQtyData = FIX50SP2.Components.OrderQtyData(required=False)
                self.TriggeringInstruction = FIX50SP2.Components.TriggeringInstruction(required=False)
                self.CommissionData = FIX50SP2.Components.CommissionData(required=False)
                self.PegInstructions = FIX50SP2.Components.PegInstructions(required=False)
                self.DiscretionInstructions = FIX50SP2.Components.DiscretionInstructions(required=False)
                self.StrategyParametersGrp = FIX50SP2.Components.StrategyParametersGrp(required=False)

        class MultilegOrderCancelReplace(AppMessage):
            MsgType = "AC"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AC"
                self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                self.OrigClOrdID = FIX50SP2.Tags.OrigClOrdID(required=False)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.ClOrdLinkID = FIX50SP2.Tags.ClOrdLinkID(required=False)
                self.OrigOrdModTime = FIX50SP2.Tags.OrigOrdModTime(required=False)
                self.TradeOriginationDate = FIX50SP2.Tags.TradeOriginationDate(required=False)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.DayBookingInst = FIX50SP2.Tags.DayBookingInst(required=False)
                self.BookingUnit = FIX50SP2.Tags.BookingUnit(required=False)
                self.PreallocMethod = FIX50SP2.Tags.PreallocMethod(required=False)
                self.AllocID = FIX50SP2.Tags.AllocID(required=False)
                self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.CashMargin = FIX50SP2.Tags.CashMargin(required=False)
                self.ClearingFeeIndicator = FIX50SP2.Tags.ClearingFeeIndicator(required=False)
                self.HandlInst = FIX50SP2.Tags.HandlInst(required=False)
                self.ExecInst = FIX50SP2.Tags.ExecInst(required=False)
                self.MinQty = FIX50SP2.Tags.MinQty(required=False)
                self.MatchIncrement = FIX50SP2.Tags.MatchIncrement(required=False)
                self.MaxPriceLevels = FIX50SP2.Tags.MaxPriceLevels(required=False)
                self.MaxFloor = FIX50SP2.Tags.MaxFloor(required=False)
                self.ExDestination = FIX50SP2.Tags.ExDestination(required=False)
                self.ExDestinationIDSource = FIX50SP2.Tags.ExDestinationIDSource(required=False)
                self.ProcessCode = FIX50SP2.Tags.ProcessCode(required=False)
                self.Side = FIX50SP2.Tags.Side(required=True)
                self.PrevClosePx = FIX50SP2.Tags.PrevClosePx(required=False)
                self.SwapPoints = FIX50SP2.Tags.SwapPoints(required=False)
                self.LocateReqd = FIX50SP2.Tags.LocateReqd(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.OrdType = FIX50SP2.Tags.OrdType(required=True)
                self.MultilegModel = FIX50SP2.Tags.MultilegModel(required=False)
                self.MultilegPriceMethod = FIX50SP2.Tags.MultilegPriceMethod(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.Price = FIX50SP2.Tags.Price(required=False)
                self.PriceProtectionScope = FIX50SP2.Tags.PriceProtectionScope(required=False)
                self.StopPx = FIX50SP2.Tags.StopPx(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.ComplianceID = FIX50SP2.Tags.ComplianceID(required=False)
                self.SolicitedFlag = FIX50SP2.Tags.SolicitedFlag(required=False)
                self.IOIID = FIX50SP2.Tags.IOIID(required=False)
                self.QuoteID = FIX50SP2.Tags.QuoteID(required=False)
                self.TimeInForce = FIX50SP2.Tags.TimeInForce(required=False)
                self.EffectiveTime = FIX50SP2.Tags.EffectiveTime(required=False)
                self.ExpireDate = FIX50SP2.Tags.ExpireDate(required=False)
                self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                self.GTBookingInst = FIX50SP2.Tags.GTBookingInst(required=False)
                self.OrderCapacity = FIX50SP2.Tags.OrderCapacity(required=False)
                self.OrderRestrictions = FIX50SP2.Tags.OrderRestrictions(required=False)
                self.PreTradeAnonymity = FIX50SP2.Tags.PreTradeAnonymity(required=False)
                self.CustOrderCapacity = FIX50SP2.Tags.CustOrderCapacity(required=False)
                self.ForexReq = FIX50SP2.Tags.ForexReq(required=False)
                self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                self.BookingType = FIX50SP2.Tags.BookingType(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.PositionEffect = FIX50SP2.Tags.PositionEffect(required=False)
                self.CoveredOrUncovered = FIX50SP2.Tags.CoveredOrUncovered(required=False)
                self.MaxShow = FIX50SP2.Tags.MaxShow(required=False)
                self.TargetStrategy = FIX50SP2.Tags.TargetStrategy(required=False)
                self.TargetStrategyParameters = FIX50SP2.Tags.TargetStrategyParameters(required=False)
                self.RiskFreeRate = FIX50SP2.Tags.RiskFreeRate(required=False)
                self.ParticipationRate = FIX50SP2.Tags.ParticipationRate(required=False)
                self.CancellationRights = FIX50SP2.Tags.CancellationRights(required=False)
                self.MoneyLaunderingStatus = FIX50SP2.Tags.MoneyLaunderingStatus(required=False)
                self.RegistID = FIX50SP2.Tags.RegistID(required=False)
                self.Designation = FIX50SP2.Tags.Designation(required=False)
                self.MultiLegRptTypeReq = FIX50SP2.Tags.MultiLegRptTypeReq(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.PreAllocMlegGrp = FIX50SP2.Components.PreAllocMlegGrp(required=False)
                self.DisplayInstruction = FIX50SP2.Components.DisplayInstruction(required=False)
                self.TrdgSesGrp = FIX50SP2.Components.TrdgSesGrp(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.LegOrdGrp = FIX50SP2.Components.LegOrdGrp(required=False)
                self.OrderQtyData = FIX50SP2.Components.OrderQtyData(required=True)
                self.TriggeringInstruction = FIX50SP2.Components.TriggeringInstruction(required=False)
                self.CommissionData = FIX50SP2.Components.CommissionData(required=False)
                self.PegInstructions = FIX50SP2.Components.PegInstructions(required=False)
                self.DiscretionInstructions = FIX50SP2.Components.DiscretionInstructions(required=False)
                self.StrategyParametersGrp = FIX50SP2.Components.StrategyParametersGrp(required=False)

        class TradeCaptureReportRequest(AppMessage):
            MsgType = "AD"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AD"
                self.TradeRequestID = FIX50SP2.Tags.TradeRequestID(required=True)
                self.TradeID = FIX50SP2.Tags.TradeID(required=False)
                self.SecondaryTradeID = FIX50SP2.Tags.SecondaryTradeID(required=False)
                self.FirmTradeID = FIX50SP2.Tags.FirmTradeID(required=False)
                self.SecondaryFirmTradeID = FIX50SP2.Tags.SecondaryFirmTradeID(required=False)
                self.TradeRequestType = FIX50SP2.Tags.TradeRequestType(required=True)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=False)
                self.TradeReportID = FIX50SP2.Tags.TradeReportID(required=False)
                self.SecondaryTradeReportID = FIX50SP2.Tags.SecondaryTradeReportID(required=False)
                self.ExecID = FIX50SP2.Tags.ExecID(required=False)
                self.ExecType = FIX50SP2.Tags.ExecType(required=False)
                self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.MatchStatus = FIX50SP2.Tags.MatchStatus(required=False)
                self.TrdType = FIX50SP2.Tags.TrdType(required=False)
                self.TrdSubType = FIX50SP2.Tags.TrdSubType(required=False)
                self.TradeHandlingInstr = FIX50SP2.Tags.TradeHandlingInstr(required=False)
                self.TransferReason = FIX50SP2.Tags.TransferReason(required=False)
                self.SecondaryTrdType = FIX50SP2.Tags.SecondaryTrdType(required=False)
                self.TradeLinkID = FIX50SP2.Tags.TradeLinkID(required=False)
                self.TrdMatchID = FIX50SP2.Tags.TrdMatchID(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.TimeBracket = FIX50SP2.Tags.TimeBracket(required=False)
                self.Side = FIX50SP2.Tags.Side(required=False)
                self.MultiLegReportingType = FIX50SP2.Tags.MultiLegReportingType(required=False)
                self.TradeInputSource = FIX50SP2.Tags.TradeInputSource(required=False)
                self.TradeInputDevice = FIX50SP2.Tags.TradeInputDevice(required=False)
                self.ResponseTransportType = FIX50SP2.Tags.ResponseTransportType(required=False)
                self.ResponseDestination = FIX50SP2.Tags.ResponseDestination(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.MessageEventSource = FIX50SP2.Tags.MessageEventSource(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.InstrumentExtension = FIX50SP2.Components.InstrumentExtension(required=False)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.TrdCapDtGrp = FIX50SP2.Components.TrdCapDtGrp(required=False)

        class TradeCaptureReport(AppMessage):
            MsgType = "AE"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AE"
                self.TradeReportID = FIX50SP2.Tags.TradeReportID(required=False)
                self.TradeID = FIX50SP2.Tags.TradeID(required=False)
                self.SecondaryTradeID = FIX50SP2.Tags.SecondaryTradeID(required=False)
                self.FirmTradeID = FIX50SP2.Tags.FirmTradeID(required=False)
                self.SecondaryFirmTradeID = FIX50SP2.Tags.SecondaryFirmTradeID(required=False)
                self.TradeReportTransType = FIX50SP2.Tags.TradeReportTransType(required=False)
                self.TradeReportType = FIX50SP2.Tags.TradeReportType(required=False)
                self.TrdRptStatus = FIX50SP2.Tags.TrdRptStatus(required=False)
                self.TradeRequestID = FIX50SP2.Tags.TradeRequestID(required=False)
                self.TrdType = FIX50SP2.Tags.TrdType(required=False)
                self.TrdSubType = FIX50SP2.Tags.TrdSubType(required=False)
                self.SecondaryTrdType = FIX50SP2.Tags.SecondaryTrdType(required=False)
                self.TradeHandlingInstr = FIX50SP2.Tags.TradeHandlingInstr(required=False)
                self.OrigTradeHandlingInstr = FIX50SP2.Tags.OrigTradeHandlingInstr(required=False)
                self.OrigTradeDate = FIX50SP2.Tags.OrigTradeDate(required=False)
                self.OrigTradeID = FIX50SP2.Tags.OrigTradeID(required=False)
                self.OrigSecondaryTradeID = FIX50SP2.Tags.OrigSecondaryTradeID(required=False)
                self.TransferReason = FIX50SP2.Tags.TransferReason(required=False)
                self.ExecType = FIX50SP2.Tags.ExecType(required=False)
                self.TotNumTradeReports = FIX50SP2.Tags.TotNumTradeReports(required=False)
                self.LastRptRequested = FIX50SP2.Tags.LastRptRequested(required=False)
                self.UnsolicitedIndicator = FIX50SP2.Tags.UnsolicitedIndicator(required=False)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=False)
                self.TradeReportRefID = FIX50SP2.Tags.TradeReportRefID(required=False)
                self.SecondaryTradeReportRefID = FIX50SP2.Tags.SecondaryTradeReportRefID(required=False)
                self.SecondaryTradeReportID = FIX50SP2.Tags.SecondaryTradeReportID(required=False)
                self.TradeLinkID = FIX50SP2.Tags.TradeLinkID(required=False)
                self.TrdMatchID = FIX50SP2.Tags.TrdMatchID(required=False)
                self.ExecID = FIX50SP2.Tags.ExecID(required=False)
                self.SecondaryExecID = FIX50SP2.Tags.SecondaryExecID(required=False)
                self.ExecRestatementReason = FIX50SP2.Tags.ExecRestatementReason(required=False)
                self.PreviouslyReported = FIX50SP2.Tags.PreviouslyReported(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.AsOfIndicator = FIX50SP2.Tags.AsOfIndicator(required=False)
                self.SettlSessID = FIX50SP2.Tags.SettlSessID(required=False)
                self.SettlSessSubID = FIX50SP2.Tags.SettlSessSubID(required=False)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.UnderlyingTradingSessionID = FIX50SP2.Tags.UnderlyingTradingSessionID(required=False)
                self.UnderlyingTradingSessionSubID = FIX50SP2.Tags.UnderlyingTradingSessionSubID(required=False)
                self.LastQty = FIX50SP2.Tags.LastQty(required=True)
                self.LastPx = FIX50SP2.Tags.LastPx(required=True)
                self.CalculatedCcyLastQty = FIX50SP2.Tags.CalculatedCcyLastQty(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                self.LastParPx = FIX50SP2.Tags.LastParPx(required=False)
                self.LastSpotRate = FIX50SP2.Tags.LastSpotRate(required=False)
                self.LastForwardPoints = FIX50SP2.Tags.LastForwardPoints(required=False)
                self.LastSwapPoints = FIX50SP2.Tags.LastSwapPoints(required=False)
                self.LastMkt = FIX50SP2.Tags.LastMkt(required=False)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.AvgPx = FIX50SP2.Tags.AvgPx(required=False)
                self.AvgPxIndicator = FIX50SP2.Tags.AvgPxIndicator(required=False)
                self.MultiLegReportingType = FIX50SP2.Tags.MultiLegReportingType(required=False)
                self.TradeLegRefID = FIX50SP2.Tags.TradeLegRefID(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.UnderlyingSettlementDate = FIX50SP2.Tags.UnderlyingSettlementDate(required=False)
                self.MatchStatus = FIX50SP2.Tags.MatchStatus(required=False)
                self.MatchType = FIX50SP2.Tags.MatchType(required=False)
                self.Volatility = FIX50SP2.Tags.Volatility(required=False)
                self.DividendYield = FIX50SP2.Tags.DividendYield(required=False)
                self.RiskFreeRate = FIX50SP2.Tags.RiskFreeRate(required=False)
                self.CurrencyRatio = FIX50SP2.Tags.CurrencyRatio(required=False)
                self.CopyMsgIndicator = FIX50SP2.Tags.CopyMsgIndicator(required=False)
                self.PublishTrdIndicator = FIX50SP2.Tags.PublishTrdIndicator(required=False)
                self.TradePublishIndicator = FIX50SP2.Tags.TradePublishIndicator(required=False)
                self.ShortSaleReason = FIX50SP2.Tags.ShortSaleReason(required=False)
                self.TierCode = FIX50SP2.Tags.TierCode(required=False)
                self.MessageEventSource = FIX50SP2.Tags.MessageEventSource(required=False)
                self.LastUpdateTime = FIX50SP2.Tags.LastUpdateTime(required=False)
                self.RndPx = FIX50SP2.Tags.RndPx(required=False)
                self.TZTransactTime = FIX50SP2.Tags.TZTransactTime(required=False)
                self.ReportedPxDiff = FIX50SP2.Tags.ReportedPxDiff(required=False)
                self.GrossTradeAmt = FIX50SP2.Tags.GrossTradeAmt(required=False)
                self.RejectText = FIX50SP2.Tags.RejectText(required=False)
                self.FeeMultiplier = FIX50SP2.Tags.FeeMultiplier(required=False)
                self.VenueType = FIX50SP2.Tags.VenueType(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.RootParties = FIX50SP2.Components.RootParties(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.YieldData = FIX50SP2.Components.YieldData(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.PositionAmountData = FIX50SP2.Components.PositionAmountData(required=False)
                self.TrdInstrmtLegGrp = FIX50SP2.Components.TrdInstrmtLegGrp(required=False)
                self.TrdRegTimestamps = FIX50SP2.Components.TrdRegTimestamps(required=False)
                self.TrdCapRptSideGrp = FIX50SP2.Components.TrdCapRptSideGrp(required=True)
                self.TrdRepIndicatorsGrp = FIX50SP2.Components.TrdRepIndicatorsGrp(required=False)

        class OrderMassStatusRequest(AppMessage):
            MsgType = "AF"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AF"
                self.MassStatusReqID = FIX50SP2.Tags.MassStatusReqID(required=True)
                self.MassStatusReqType = FIX50SP2.Tags.MassStatusReqType(required=True)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.Side = FIX50SP2.Tags.Side(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.UnderlyingInstrument = FIX50SP2.Components.UnderlyingInstrument(required=False)
                self.TargetParties = FIX50SP2.Components.TargetParties(required=False)

        class QuoteRequestReject(AppMessage):
            MsgType = "AG"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AG"
                self.QuoteReqID = FIX50SP2.Tags.QuoteReqID(required=True)
                self.RFQReqID = FIX50SP2.Tags.RFQReqID(required=False)
                self.QuoteRequestRejectReason = FIX50SP2.Tags.QuoteRequestRejectReason(required=True)
                self.PrivateQuote = FIX50SP2.Tags.PrivateQuote(required=False)
                self.RespondentType = FIX50SP2.Tags.RespondentType(required=False)
                self.PreTradeAnonymity = FIX50SP2.Tags.PreTradeAnonymity(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.RootParties = FIX50SP2.Components.RootParties(required=False)
                self.QuotReqRjctGrp = FIX50SP2.Components.QuotReqRjctGrp(required=True)

        class RFQRequest(AppMessage):
            MsgType = "AH"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AH"
                self.RFQReqID = FIX50SP2.Tags.RFQReqID(required=True)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=False)
                self.PrivateQuote = FIX50SP2.Tags.PrivateQuote(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.RFQReqGrp = FIX50SP2.Components.RFQReqGrp(required=True)

        class QuoteStatusReport(AppMessage):
            MsgType = "AI"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AI"
                self.QuoteStatusReqID = FIX50SP2.Tags.QuoteStatusReqID(required=False)
                self.QuoteReqID = FIX50SP2.Tags.QuoteReqID(required=False)
                self.QuoteID = FIX50SP2.Tags.QuoteID(required=False)
                self.QuoteMsgID = FIX50SP2.Tags.QuoteMsgID(required=False)
                self.QuoteRespID = FIX50SP2.Tags.QuoteRespID(required=False)
                self.QuoteType = FIX50SP2.Tags.QuoteType(required=False)
                self.QuoteCancelType = FIX50SP2.Tags.QuoteCancelType(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.Side = FIX50SP2.Tags.Side(required=False)
                self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.SettlDate2 = FIX50SP2.Tags.SettlDate2(required=False)
                self.OrderQty2 = FIX50SP2.Tags.OrderQty2(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                self.Price = FIX50SP2.Tags.Price(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.BidPx = FIX50SP2.Tags.BidPx(required=False)
                self.OfferPx = FIX50SP2.Tags.OfferPx(required=False)
                self.MktBidPx = FIX50SP2.Tags.MktBidPx(required=False)
                self.MktOfferPx = FIX50SP2.Tags.MktOfferPx(required=False)
                self.MinBidSize = FIX50SP2.Tags.MinBidSize(required=False)
                self.BidSize = FIX50SP2.Tags.BidSize(required=False)
                self.MinOfferSize = FIX50SP2.Tags.MinOfferSize(required=False)
                self.OfferSize = FIX50SP2.Tags.OfferSize(required=False)
                self.MinQty = FIX50SP2.Tags.MinQty(required=False)
                self.ValidUntilTime = FIX50SP2.Tags.ValidUntilTime(required=False)
                self.BidSpotRate = FIX50SP2.Tags.BidSpotRate(required=False)
                self.OfferSpotRate = FIX50SP2.Tags.OfferSpotRate(required=False)
                self.BidForwardPoints = FIX50SP2.Tags.BidForwardPoints(required=False)
                self.OfferForwardPoints = FIX50SP2.Tags.OfferForwardPoints(required=False)
                self.MidPx = FIX50SP2.Tags.MidPx(required=False)
                self.BidYield = FIX50SP2.Tags.BidYield(required=False)
                self.MidYield = FIX50SP2.Tags.MidYield(required=False)
                self.OfferYield = FIX50SP2.Tags.OfferYield(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.OrdType = FIX50SP2.Tags.OrdType(required=False)
                self.BidForwardPoints2 = FIX50SP2.Tags.BidForwardPoints2(required=False)
                self.OfferForwardPoints2 = FIX50SP2.Tags.OfferForwardPoints2(required=False)
                self.SettlCurrBidFxRate = FIX50SP2.Tags.SettlCurrBidFxRate(required=False)
                self.SettlCurrOfferFxRate = FIX50SP2.Tags.SettlCurrOfferFxRate(required=False)
                self.SettlCurrFxRateCalc = FIX50SP2.Tags.SettlCurrFxRateCalc(required=False)
                self.CommType = FIX50SP2.Tags.CommType(required=False)
                self.Commission = FIX50SP2.Tags.Commission(required=False)
                self.CustOrderCapacity = FIX50SP2.Tags.CustOrderCapacity(required=False)
                self.ExDestination = FIX50SP2.Tags.ExDestination(required=False)
                self.ExDestinationIDSource = FIX50SP2.Tags.ExDestinationIDSource(required=False)
                self.QuoteStatus = FIX50SP2.Tags.QuoteStatus(required=False)
                self.QuoteRejectReason = FIX50SP2.Tags.QuoteRejectReason(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.BookingType = FIX50SP2.Tags.BookingType(required=False)
                self.OrderCapacity = FIX50SP2.Tags.OrderCapacity(required=False)
                self.OrderRestrictions = FIX50SP2.Tags.OrderRestrictions(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.OrderQtyData = FIX50SP2.Components.OrderQtyData(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                self.LegQuotStatGrp = FIX50SP2.Components.LegQuotStatGrp(required=False)
                self.QuotQualGrp = FIX50SP2.Components.QuotQualGrp(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.YieldData = FIX50SP2.Components.YieldData(required=False)
                self.TargetParties = FIX50SP2.Components.TargetParties(required=False)

        class QuoteResponse(AppMessage):
            MsgType = "AJ"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AJ"
                self.QuoteRespID = FIX50SP2.Tags.QuoteRespID(required=True)
                self.QuoteID = FIX50SP2.Tags.QuoteID(required=False)
                self.QuoteMsgID = FIX50SP2.Tags.QuoteMsgID(required=False)
                self.QuoteRespType = FIX50SP2.Tags.QuoteRespType(required=True)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.OrderCapacity = FIX50SP2.Tags.OrderCapacity(required=False)
                self.OrderRestrictions = FIX50SP2.Tags.OrderRestrictions(required=False)
                self.IOIID = FIX50SP2.Tags.IOIID(required=False)
                self.QuoteType = FIX50SP2.Tags.QuoteType(required=False)
                self.PreTradeAnonymity = FIX50SP2.Tags.PreTradeAnonymity(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.Side = FIX50SP2.Tags.Side(required=False)
                self.MinQty = FIX50SP2.Tags.MinQty(required=False)
                self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.SettlDate2 = FIX50SP2.Tags.SettlDate2(required=False)
                self.OrderQty2 = FIX50SP2.Tags.OrderQty2(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.BidPx = FIX50SP2.Tags.BidPx(required=False)
                self.OfferPx = FIX50SP2.Tags.OfferPx(required=False)
                self.MktBidPx = FIX50SP2.Tags.MktBidPx(required=False)
                self.MktOfferPx = FIX50SP2.Tags.MktOfferPx(required=False)
                self.MinBidSize = FIX50SP2.Tags.MinBidSize(required=False)
                self.BidSize = FIX50SP2.Tags.BidSize(required=False)
                self.MinOfferSize = FIX50SP2.Tags.MinOfferSize(required=False)
                self.OfferSize = FIX50SP2.Tags.OfferSize(required=False)
                self.ValidUntilTime = FIX50SP2.Tags.ValidUntilTime(required=False)
                self.BidSpotRate = FIX50SP2.Tags.BidSpotRate(required=False)
                self.OfferSpotRate = FIX50SP2.Tags.OfferSpotRate(required=False)
                self.BidForwardPoints = FIX50SP2.Tags.BidForwardPoints(required=False)
                self.OfferForwardPoints = FIX50SP2.Tags.OfferForwardPoints(required=False)
                self.MidPx = FIX50SP2.Tags.MidPx(required=False)
                self.BidYield = FIX50SP2.Tags.BidYield(required=False)
                self.MidYield = FIX50SP2.Tags.MidYield(required=False)
                self.OfferYield = FIX50SP2.Tags.OfferYield(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.OrdType = FIX50SP2.Tags.OrdType(required=False)
                self.BidForwardPoints2 = FIX50SP2.Tags.BidForwardPoints2(required=False)
                self.OfferForwardPoints2 = FIX50SP2.Tags.OfferForwardPoints2(required=False)
                self.SettlCurrBidFxRate = FIX50SP2.Tags.SettlCurrBidFxRate(required=False)
                self.SettlCurrOfferFxRate = FIX50SP2.Tags.SettlCurrOfferFxRate(required=False)
                self.SettlCurrFxRateCalc = FIX50SP2.Tags.SettlCurrFxRateCalc(required=False)
                self.Commission = FIX50SP2.Tags.Commission(required=False)
                self.CommType = FIX50SP2.Tags.CommType(required=False)
                self.CustOrderCapacity = FIX50SP2.Tags.CustOrderCapacity(required=False)
                self.ExDestination = FIX50SP2.Tags.ExDestination(required=False)
                self.ExDestinationIDSource = FIX50SP2.Tags.ExDestinationIDSource(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.Price = FIX50SP2.Tags.Price(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.QuotQualGrp = FIX50SP2.Components.QuotQualGrp(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.OrderQtyData = FIX50SP2.Components.OrderQtyData(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                self.LegQuotGrp = FIX50SP2.Components.LegQuotGrp(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.YieldData = FIX50SP2.Components.YieldData(required=False)

        class Confirmation(AppMessage):
            MsgType = "AK"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AK"
                self.ConfirmID = FIX50SP2.Tags.ConfirmID(required=True)
                self.ConfirmRefID = FIX50SP2.Tags.ConfirmRefID(required=False)
                self.ConfirmReqID = FIX50SP2.Tags.ConfirmReqID(required=False)
                self.ConfirmTransType = FIX50SP2.Tags.ConfirmTransType(required=True)
                self.ConfirmType = FIX50SP2.Tags.ConfirmType(required=True)
                self.CopyMsgIndicator = FIX50SP2.Tags.CopyMsgIndicator(required=False)
                self.LegalConfirm = FIX50SP2.Tags.LegalConfirm(required=False)
                self.ConfirmStatus = FIX50SP2.Tags.ConfirmStatus(required=True)
                self.AllocID = FIX50SP2.Tags.AllocID(required=False)
                self.SecondaryAllocID = FIX50SP2.Tags.SecondaryAllocID(required=False)
                self.IndividualAllocID = FIX50SP2.Tags.IndividualAllocID(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=True)
                self.AllocQty = FIX50SP2.Tags.AllocQty(required=True)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.Side = FIX50SP2.Tags.Side(required=True)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.LastMkt = FIX50SP2.Tags.LastMkt(required=False)
                self.AllocAccount = FIX50SP2.Tags.AllocAccount(required=True)
                self.AllocAcctIDSource = FIX50SP2.Tags.AllocAcctIDSource(required=False)
                self.AllocAccountType = FIX50SP2.Tags.AllocAccountType(required=False)
                self.AvgPx = FIX50SP2.Tags.AvgPx(required=True)
                self.AvgPxPrecision = FIX50SP2.Tags.AvgPxPrecision(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.AvgParPx = FIX50SP2.Tags.AvgParPx(required=False)
                self.ReportedPx = FIX50SP2.Tags.ReportedPx(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.ProcessCode = FIX50SP2.Tags.ProcessCode(required=False)
                self.GrossTradeAmt = FIX50SP2.Tags.GrossTradeAmt(required=True)
                self.NumDaysInterest = FIX50SP2.Tags.NumDaysInterest(required=False)
                self.ExDate = FIX50SP2.Tags.ExDate(required=False)
                self.AccruedInterestRate = FIX50SP2.Tags.AccruedInterestRate(required=False)
                self.AccruedInterestAmt = FIX50SP2.Tags.AccruedInterestAmt(required=False)
                self.InterestAtMaturity = FIX50SP2.Tags.InterestAtMaturity(required=False)
                self.EndAccruedInterestAmt = FIX50SP2.Tags.EndAccruedInterestAmt(required=False)
                self.StartCash = FIX50SP2.Tags.StartCash(required=False)
                self.EndCash = FIX50SP2.Tags.EndCash(required=False)
                self.Concession = FIX50SP2.Tags.Concession(required=False)
                self.TotalTakedown = FIX50SP2.Tags.TotalTakedown(required=False)
                self.NetMoney = FIX50SP2.Tags.NetMoney(required=True)
                self.MaturityNetMoney = FIX50SP2.Tags.MaturityNetMoney(required=False)
                self.SettlCurrAmt = FIX50SP2.Tags.SettlCurrAmt(required=False)
                self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                self.SettlCurrFxRate = FIX50SP2.Tags.SettlCurrFxRate(required=False)
                self.SettlCurrFxRateCalc = FIX50SP2.Tags.SettlCurrFxRateCalc(required=False)
                self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.SharedCommission = FIX50SP2.Tags.SharedCommission(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.OrdAllocGrp = FIX50SP2.Components.OrdAllocGrp(required=False)
                self.TrdRegTimestamps = FIX50SP2.Components.TrdRegTimestamps(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.InstrumentExtension = FIX50SP2.Components.InstrumentExtension(required=False)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.YieldData = FIX50SP2.Components.YieldData(required=False)
                self.CpctyConfGrp = FIX50SP2.Components.CpctyConfGrp(required=True)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.SettlInstructionsData = FIX50SP2.Components.SettlInstructionsData(required=False)
                self.CommissionData = FIX50SP2.Components.CommissionData(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                self.MiscFeesGrp = FIX50SP2.Components.MiscFeesGrp(required=False)

        class PositionMaintenanceRequest(AppMessage):
            MsgType = "AL"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AL"
                self.PosReqID = FIX50SP2.Tags.PosReqID(required=False)
                self.PosTransType = FIX50SP2.Tags.PosTransType(required=True)
                self.PosMaintAction = FIX50SP2.Tags.PosMaintAction(required=True)
                self.OrigPosReqRefID = FIX50SP2.Tags.OrigPosReqRefID(required=False)
                self.PosMaintRptRefID = FIX50SP2.Tags.PosMaintRptRefID(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=True)
                self.SettlSessID = FIX50SP2.Tags.SettlSessID(required=False)
                self.SettlSessSubID = FIX50SP2.Tags.SettlSessSubID(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.AdjustmentType = FIX50SP2.Tags.AdjustmentType(required=False)
                self.ContraryInstructionIndicator = FIX50SP2.Tags.ContraryInstructionIndicator(required=False)
                self.PriorSpreadIndicator = FIX50SP2.Tags.PriorSpreadIndicator(required=False)
                self.ThresholdAmount = FIX50SP2.Tags.ThresholdAmount(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=True)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.TrdgSesGrp = FIX50SP2.Components.TrdgSesGrp(required=False)
                self.PositionQty = FIX50SP2.Components.PositionQty(required=True)
                self.PositionAmountData = FIX50SP2.Components.PositionAmountData(required=False)

        class PositionMaintenanceReport(AppMessage):
            MsgType = "AM"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AM"
                self.PosMaintRptID = FIX50SP2.Tags.PosMaintRptID(required=True)
                self.PosTransType = FIX50SP2.Tags.PosTransType(required=True)
                self.PosReqID = FIX50SP2.Tags.PosReqID(required=False)
                self.PosMaintAction = FIX50SP2.Tags.PosMaintAction(required=True)
                self.OrigPosReqRefID = FIX50SP2.Tags.OrigPosReqRefID(required=False)
                self.PosMaintStatus = FIX50SP2.Tags.PosMaintStatus(required=True)
                self.PosMaintResult = FIX50SP2.Tags.PosMaintResult(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=True)
                self.SettlSessID = FIX50SP2.Tags.SettlSessID(required=False)
                self.SettlSessSubID = FIX50SP2.Tags.SettlSessSubID(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.PosMaintRptRefID = FIX50SP2.Tags.PosMaintRptRefID(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                self.ContraryInstructionIndicator = FIX50SP2.Tags.ContraryInstructionIndicator(required=False)
                self.PriorSpreadIndicator = FIX50SP2.Tags.PriorSpreadIndicator(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.AdjustmentType = FIX50SP2.Tags.AdjustmentType(required=False)
                self.ThresholdAmount = FIX50SP2.Tags.ThresholdAmount(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.TrdgSesGrp = FIX50SP2.Components.TrdgSesGrp(required=False)
                self.PositionQty = FIX50SP2.Components.PositionQty(required=True)
                self.PositionAmountData = FIX50SP2.Components.PositionAmountData(required=False)

        class RequestForPositions(AppMessage):
            MsgType = "AN"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AN"
                self.PosReqID = FIX50SP2.Tags.PosReqID(required=True)
                self.PosReqType = FIX50SP2.Tags.PosReqType(required=True)
                self.MatchStatus = FIX50SP2.Tags.MatchStatus(required=False)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=False)
                self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=True)
                self.SettlSessID = FIX50SP2.Tags.SettlSessID(required=False)
                self.SettlSessSubID = FIX50SP2.Tags.SettlSessSubID(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.ResponseTransportType = FIX50SP2.Tags.ResponseTransportType(required=False)
                self.ResponseDestination = FIX50SP2.Tags.ResponseDestination(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=True)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.TrdgSesGrp = FIX50SP2.Components.TrdgSesGrp(required=False)

        class RequestForPositionsAck(AppMessage):
            MsgType = "AO"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AO"
                self.PosMaintRptID = FIX50SP2.Tags.PosMaintRptID(required=True)
                self.PosReqID = FIX50SP2.Tags.PosReqID(required=False)
                self.TotalNumPosReports = FIX50SP2.Tags.TotalNumPosReports(required=False)
                self.UnsolicitedIndicator = FIX50SP2.Tags.UnsolicitedIndicator(required=False)
                self.PosReqResult = FIX50SP2.Tags.PosReqResult(required=True)
                self.PosReqStatus = FIX50SP2.Tags.PosReqStatus(required=True)
                self.PosReqType = FIX50SP2.Tags.PosReqType(required=False)
                self.MatchStatus = FIX50SP2.Tags.MatchStatus(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=False)
                self.SettlSessID = FIX50SP2.Tags.SettlSessID(required=False)
                self.SettlSessSubID = FIX50SP2.Tags.SettlSessSubID(required=False)
                self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.ResponseTransportType = FIX50SP2.Tags.ResponseTransportType(required=False)
                self.ResponseDestination = FIX50SP2.Tags.ResponseDestination(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=True)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)

        class PositionReport(AppMessage):
            MsgType = "AP"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AP"
                self.PosMaintRptID = FIX50SP2.Tags.PosMaintRptID(required=True)
                self.PosReqID = FIX50SP2.Tags.PosReqID(required=False)
                self.PosReqType = FIX50SP2.Tags.PosReqType(required=False)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=False)
                self.TotalNumPosReports = FIX50SP2.Tags.TotalNumPosReports(required=False)
                self.PosReqResult = FIX50SP2.Tags.PosReqResult(required=False)
                self.UnsolicitedIndicator = FIX50SP2.Tags.UnsolicitedIndicator(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=True)
                self.SettlSessID = FIX50SP2.Tags.SettlSessID(required=False)
                self.SettlSessSubID = FIX50SP2.Tags.SettlSessSubID(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                self.MessageEventSource = FIX50SP2.Tags.MessageEventSource(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AcctIDSource = FIX50SP2.Tags.AcctIDSource(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.SettlPrice = FIX50SP2.Tags.SettlPrice(required=False)
                self.SettlPriceType = FIX50SP2.Tags.SettlPriceType(required=False)
                self.PriorSettlPrice = FIX50SP2.Tags.PriorSettlPrice(required=False)
                self.MatchStatus = FIX50SP2.Tags.MatchStatus(required=False)
                self.RegistStatus = FIX50SP2.Tags.RegistStatus(required=False)
                self.DeliveryDate = FIX50SP2.Tags.DeliveryDate(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.ModelType = FIX50SP2.Tags.ModelType(required=False)
                self.PriceDelta = FIX50SP2.Tags.PriceDelta(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=True)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.PosUndInstrmtGrp = FIX50SP2.Components.PosUndInstrmtGrp(required=False)
                self.PositionQty = FIX50SP2.Components.PositionQty(required=False)
                self.PositionAmountData = FIX50SP2.Components.PositionAmountData(required=False)

        class TradeCaptureReportRequestAck(AppMessage):
            MsgType = "AQ"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AQ"
                self.TradeRequestID = FIX50SP2.Tags.TradeRequestID(required=True)
                self.TradeID = FIX50SP2.Tags.TradeID(required=False)
                self.SecondaryTradeID = FIX50SP2.Tags.SecondaryTradeID(required=False)
                self.FirmTradeID = FIX50SP2.Tags.FirmTradeID(required=False)
                self.SecondaryFirmTradeID = FIX50SP2.Tags.SecondaryFirmTradeID(required=False)
                self.TradeRequestType = FIX50SP2.Tags.TradeRequestType(required=True)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=False)
                self.TotNumTradeReports = FIX50SP2.Tags.TotNumTradeReports(required=False)
                self.TradeRequestResult = FIX50SP2.Tags.TradeRequestResult(required=True)
                self.TradeRequestStatus = FIX50SP2.Tags.TradeRequestStatus(required=True)
                self.MultiLegReportingType = FIX50SP2.Tags.MultiLegReportingType(required=False)
                self.ResponseTransportType = FIX50SP2.Tags.ResponseTransportType(required=False)
                self.ResponseDestination = FIX50SP2.Tags.ResponseDestination(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.MessageEventSource = FIX50SP2.Tags.MessageEventSource(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)

        class TradeCaptureReportAck(AppMessage):
            MsgType = "AR"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AR"
                self.TradeReportID = FIX50SP2.Tags.TradeReportID(required=False)
                self.TradeID = FIX50SP2.Tags.TradeID(required=False)
                self.SecondaryTradeID = FIX50SP2.Tags.SecondaryTradeID(required=False)
                self.FirmTradeID = FIX50SP2.Tags.FirmTradeID(required=False)
                self.SecondaryFirmTradeID = FIX50SP2.Tags.SecondaryFirmTradeID(required=False)
                self.TradeReportTransType = FIX50SP2.Tags.TradeReportTransType(required=False)
                self.TradeReportType = FIX50SP2.Tags.TradeReportType(required=False)
                self.TrdType = FIX50SP2.Tags.TrdType(required=False)
                self.TrdSubType = FIX50SP2.Tags.TrdSubType(required=False)
                self.SecondaryTrdType = FIX50SP2.Tags.SecondaryTrdType(required=False)
                self.TradeHandlingInstr = FIX50SP2.Tags.TradeHandlingInstr(required=False)
                self.OrigTradeHandlingInstr = FIX50SP2.Tags.OrigTradeHandlingInstr(required=False)
                self.OrigTradeDate = FIX50SP2.Tags.OrigTradeDate(required=False)
                self.OrigTradeID = FIX50SP2.Tags.OrigTradeID(required=False)
                self.OrigSecondaryTradeID = FIX50SP2.Tags.OrigSecondaryTradeID(required=False)
                self.TransferReason = FIX50SP2.Tags.TransferReason(required=False)
                self.ExecType = FIX50SP2.Tags.ExecType(required=False)
                self.TradeReportRefID = FIX50SP2.Tags.TradeReportRefID(required=False)
                self.SecondaryTradeReportRefID = FIX50SP2.Tags.SecondaryTradeReportRefID(required=False)
                self.TrdRptStatus = FIX50SP2.Tags.TrdRptStatus(required=False)
                self.TradeReportRejectReason = FIX50SP2.Tags.TradeReportRejectReason(required=False)
                self.SecondaryTradeReportID = FIX50SP2.Tags.SecondaryTradeReportID(required=False)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=False)
                self.TradeLinkID = FIX50SP2.Tags.TradeLinkID(required=False)
                self.TrdMatchID = FIX50SP2.Tags.TrdMatchID(required=False)
                self.ExecID = FIX50SP2.Tags.ExecID(required=False)
                self.SecondaryExecID = FIX50SP2.Tags.SecondaryExecID(required=False)
                self.ExecRestatementReason = FIX50SP2.Tags.ExecRestatementReason(required=False)
                self.PreviouslyReported = FIX50SP2.Tags.PreviouslyReported(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.UnderlyingTradingSessionID = FIX50SP2.Tags.UnderlyingTradingSessionID(required=False)
                self.UnderlyingTradingSessionSubID = FIX50SP2.Tags.UnderlyingTradingSessionSubID(required=False)
                self.SettlSessID = FIX50SP2.Tags.SettlSessID(required=False)
                self.SettlSessSubID = FIX50SP2.Tags.SettlSessSubID(required=False)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.LastQty = FIX50SP2.Tags.LastQty(required=False)
                self.LastPx = FIX50SP2.Tags.LastPx(required=False)
                self.LastParPx = FIX50SP2.Tags.LastParPx(required=False)
                self.CalculatedCcyLastQty = FIX50SP2.Tags.CalculatedCcyLastQty(required=False)
                self.LastSwapPoints = FIX50SP2.Tags.LastSwapPoints(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                self.LastSpotRate = FIX50SP2.Tags.LastSpotRate(required=False)
                self.LastForwardPoints = FIX50SP2.Tags.LastForwardPoints(required=False)
                self.LastMkt = FIX50SP2.Tags.LastMkt(required=False)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.AvgPx = FIX50SP2.Tags.AvgPx(required=False)
                self.AvgPxIndicator = FIX50SP2.Tags.AvgPxIndicator(required=False)
                self.MultiLegReportingType = FIX50SP2.Tags.MultiLegReportingType(required=False)
                self.TradeLegRefID = FIX50SP2.Tags.TradeLegRefID(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                self.MatchStatus = FIX50SP2.Tags.MatchStatus(required=False)
                self.MatchType = FIX50SP2.Tags.MatchType(required=False)
                self.CopyMsgIndicator = FIX50SP2.Tags.CopyMsgIndicator(required=False)
                self.PublishTrdIndicator = FIX50SP2.Tags.PublishTrdIndicator(required=False)
                self.TradePublishIndicator = FIX50SP2.Tags.TradePublishIndicator(required=False)
                self.ShortSaleReason = FIX50SP2.Tags.ShortSaleReason(required=False)
                self.ResponseTransportType = FIX50SP2.Tags.ResponseTransportType(required=False)
                self.ResponseDestination = FIX50SP2.Tags.ResponseDestination(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.AsOfIndicator = FIX50SP2.Tags.AsOfIndicator(required=False)
                self.ClearingFeeIndicator = FIX50SP2.Tags.ClearingFeeIndicator(required=False)
                self.TierCode = FIX50SP2.Tags.TierCode(required=False)
                self.MessageEventSource = FIX50SP2.Tags.MessageEventSource(required=False)
                self.LastUpdateTime = FIX50SP2.Tags.LastUpdateTime(required=False)
                self.RndPx = FIX50SP2.Tags.RndPx(required=False)
                self.RptSys = FIX50SP2.Tags.RptSys(required=False)
                self.GrossTradeAmt = FIX50SP2.Tags.GrossTradeAmt(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.FeeMultiplier = FIX50SP2.Tags.FeeMultiplier(required=False)
                self.VenueType = FIX50SP2.Tags.VenueType(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.RootParties = FIX50SP2.Components.RootParties(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.TrdRepIndicatorsGrp = FIX50SP2.Components.TrdRepIndicatorsGrp(required=False)
                self.TrdInstrmtLegGrp = FIX50SP2.Components.TrdInstrmtLegGrp(required=False)
                self.TrdRegTimestamps = FIX50SP2.Components.TrdRegTimestamps(required=False)
                self.PositionAmountData = FIX50SP2.Components.PositionAmountData(required=False)
                self.TrdCapRptAckSideGrp = FIX50SP2.Components.TrdCapRptAckSideGrp(required=False)

        class AllocationReport(AppMessage):
            MsgType = "AS"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AS"
                self.AllocReportID = FIX50SP2.Tags.AllocReportID(required=True)
                self.AllocID = FIX50SP2.Tags.AllocID(required=False)
                self.AllocTransType = FIX50SP2.Tags.AllocTransType(required=True)
                self.AllocReportRefID = FIX50SP2.Tags.AllocReportRefID(required=False)
                self.AllocCancReplaceReason = FIX50SP2.Tags.AllocCancReplaceReason(required=False)
                self.SecondaryAllocID = FIX50SP2.Tags.SecondaryAllocID(required=False)
                self.AllocReportType = FIX50SP2.Tags.AllocReportType(required=True)
                self.AllocStatus = FIX50SP2.Tags.AllocStatus(required=True)
                self.AllocRejCode = FIX50SP2.Tags.AllocRejCode(required=False)
                self.RefAllocID = FIX50SP2.Tags.RefAllocID(required=False)
                self.AllocIntermedReqType = FIX50SP2.Tags.AllocIntermedReqType(required=False)
                self.AllocLinkID = FIX50SP2.Tags.AllocLinkID(required=False)
                self.AllocLinkType = FIX50SP2.Tags.AllocLinkType(required=False)
                self.BookingRefID = FIX50SP2.Tags.BookingRefID(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.TrdType = FIX50SP2.Tags.TrdType(required=False)
                self.TrdSubType = FIX50SP2.Tags.TrdSubType(required=False)
                self.MultiLegReportingType = FIX50SP2.Tags.MultiLegReportingType(required=False)
                self.CustOrderCapacity = FIX50SP2.Tags.CustOrderCapacity(required=False)
                self.TradeInputSource = FIX50SP2.Tags.TradeInputSource(required=False)
                self.RndPx = FIX50SP2.Tags.RndPx(required=False)
                self.MessageEventSource = FIX50SP2.Tags.MessageEventSource(required=False)
                self.TradeInputDevice = FIX50SP2.Tags.TradeInputDevice(required=False)
                self.AvgPxIndicator = FIX50SP2.Tags.AvgPxIndicator(required=False)
                self.AllocNoOrdersType = FIX50SP2.Tags.AllocNoOrdersType(required=False)
                self.PreviouslyReported = FIX50SP2.Tags.PreviouslyReported(required=False)
                self.ReversalIndicator = FIX50SP2.Tags.ReversalIndicator(required=False)
                self.MatchType = FIX50SP2.Tags.MatchType(required=False)
                self.Side = FIX50SP2.Tags.Side(required=True)
                self.Quantity = FIX50SP2.Tags.Quantity(required=True)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.LastMkt = FIX50SP2.Tags.LastMkt(required=False)
                self.TradeOriginationDate = FIX50SP2.Tags.TradeOriginationDate(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.AvgPx = FIX50SP2.Tags.AvgPx(required=True)
                self.AvgParPx = FIX50SP2.Tags.AvgParPx(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.AvgPxPrecision = FIX50SP2.Tags.AvgPxPrecision(required=False)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=True)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.BookingType = FIX50SP2.Tags.BookingType(required=False)
                self.GrossTradeAmt = FIX50SP2.Tags.GrossTradeAmt(required=False)
                self.Concession = FIX50SP2.Tags.Concession(required=False)
                self.TotalTakedown = FIX50SP2.Tags.TotalTakedown(required=False)
                self.NetMoney = FIX50SP2.Tags.NetMoney(required=False)
                self.PositionEffect = FIX50SP2.Tags.PositionEffect(required=False)
                self.AutoAcceptIndicator = FIX50SP2.Tags.AutoAcceptIndicator(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.NumDaysInterest = FIX50SP2.Tags.NumDaysInterest(required=False)
                self.AccruedInterestRate = FIX50SP2.Tags.AccruedInterestRate(required=False)
                self.AccruedInterestAmt = FIX50SP2.Tags.AccruedInterestAmt(required=False)
                self.TotalAccruedInterestAmt = FIX50SP2.Tags.TotalAccruedInterestAmt(required=False)
                self.InterestAtMaturity = FIX50SP2.Tags.InterestAtMaturity(required=False)
                self.EndAccruedInterestAmt = FIX50SP2.Tags.EndAccruedInterestAmt(required=False)
                self.StartCash = FIX50SP2.Tags.StartCash(required=False)
                self.EndCash = FIX50SP2.Tags.EndCash(required=False)
                self.LegalConfirm = FIX50SP2.Tags.LegalConfirm(required=False)
                self.TotNoAllocs = FIX50SP2.Tags.TotNoAllocs(required=False)
                self.LastFragment = FIX50SP2.Tags.LastFragment(required=False)
                self.OrdAllocGrp = FIX50SP2.Components.OrdAllocGrp(required=False)
                self.ExecAllocGrp = FIX50SP2.Components.ExecAllocGrp(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.InstrumentExtension = FIX50SP2.Components.InstrumentExtension(required=False)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                self.YieldData = FIX50SP2.Components.YieldData(required=False)
                self.PositionAmountData = FIX50SP2.Components.PositionAmountData(required=False)
                self.AllocGrp = FIX50SP2.Components.AllocGrp(required=False)
                self.RateSource = FIX50SP2.Components.RateSource(required=False)

        class AllocationReportAck(AppMessage):
            MsgType = "AT"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AT"
                self.AllocReportID = FIX50SP2.Tags.AllocReportID(required=True)
                self.AllocID = FIX50SP2.Tags.AllocID(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.AvgPxIndicator = FIX50SP2.Tags.AvgPxIndicator(required=False)
                self.Quantity = FIX50SP2.Tags.Quantity(required=False)
                self.AllocTransType = FIX50SP2.Tags.AllocTransType(required=False)
                self.SecondaryAllocID = FIX50SP2.Tags.SecondaryAllocID(required=False)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.AllocStatus = FIX50SP2.Tags.AllocStatus(required=False)
                self.AllocRejCode = FIX50SP2.Tags.AllocRejCode(required=False)
                self.AllocReportType = FIX50SP2.Tags.AllocReportType(required=False)
                self.AllocIntermedReqType = FIX50SP2.Tags.AllocIntermedReqType(required=False)
                self.MatchStatus = FIX50SP2.Tags.MatchStatus(required=False)
                self.Product = FIX50SP2.Tags.Product(required=False)
                self.SecurityType = FIX50SP2.Tags.SecurityType(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.AllocAckGrp = FIX50SP2.Components.AllocAckGrp(required=False)

        class ConfirmationAck(AppMessage):
            MsgType = "AU"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AU"
                self.ConfirmID = FIX50SP2.Tags.ConfirmID(required=True)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=True)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.AffirmStatus = FIX50SP2.Tags.AffirmStatus(required=True)
                self.ConfirmRejReason = FIX50SP2.Tags.ConfirmRejReason(required=False)
                self.MatchStatus = FIX50SP2.Tags.MatchStatus(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)

        class SettlementInstructionRequest(AppMessage):
            MsgType = "AV"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AV"
                self.SettlInstReqID = FIX50SP2.Tags.SettlInstReqID(required=True)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.AllocAccount = FIX50SP2.Tags.AllocAccount(required=False)
                self.AllocAcctIDSource = FIX50SP2.Tags.AllocAcctIDSource(required=False)
                self.Side = FIX50SP2.Tags.Side(required=False)
                self.Product = FIX50SP2.Tags.Product(required=False)
                self.SecurityType = FIX50SP2.Tags.SecurityType(required=False)
                self.CFICode = FIX50SP2.Tags.CFICode(required=False)
                self.SettlCurrency = FIX50SP2.Tags.SettlCurrency(required=False)
                self.EffectiveTime = FIX50SP2.Tags.EffectiveTime(required=False)
                self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                self.LastUpdateTime = FIX50SP2.Tags.LastUpdateTime(required=False)
                self.StandInstDbType = FIX50SP2.Tags.StandInstDbType(required=False)
                self.StandInstDbName = FIX50SP2.Tags.StandInstDbName(required=False)
                self.StandInstDbID = FIX50SP2.Tags.StandInstDbID(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)

        class AssignmentReport(AppMessage):
            MsgType = "AW"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AW"
                self.AsgnRptID = FIX50SP2.Tags.AsgnRptID(required=True)
                self.TotNumAssignmentReports = FIX50SP2.Tags.TotNumAssignmentReports(required=False)
                self.LastRptRequested = FIX50SP2.Tags.LastRptRequested(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.ThresholdAmount = FIX50SP2.Tags.ThresholdAmount(required=False)
                self.SettlPrice = FIX50SP2.Tags.SettlPrice(required=False)
                self.SettlPriceType = FIX50SP2.Tags.SettlPriceType(required=False)
                self.UnderlyingSettlPrice = FIX50SP2.Tags.UnderlyingSettlPrice(required=False)
                self.PriorSettlPrice = FIX50SP2.Tags.PriorSettlPrice(required=False)
                self.ExpireDate = FIX50SP2.Tags.ExpireDate(required=False)
                self.AssignmentMethod = FIX50SP2.Tags.AssignmentMethod(required=False)
                self.AssignmentUnit = FIX50SP2.Tags.AssignmentUnit(required=False)
                self.OpenInterest = FIX50SP2.Tags.OpenInterest(required=False)
                self.ExerciseMethod = FIX50SP2.Tags.ExerciseMethod(required=False)
                self.SettlSessID = FIX50SP2.Tags.SettlSessID(required=False)
                self.SettlSessSubID = FIX50SP2.Tags.SettlSessSubID(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=True)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.PosReqID = FIX50SP2.Tags.PosReqID(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=True)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.PositionQty = FIX50SP2.Components.PositionQty(required=False)
                self.PositionAmountData = FIX50SP2.Components.PositionAmountData(required=False)

        class CollateralRequest(AppMessage):
            MsgType = "AX"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AX"
                self.CollReqID = FIX50SP2.Tags.CollReqID(required=True)
                self.CollAsgnReason = FIX50SP2.Tags.CollAsgnReason(required=True)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                self.SecondaryOrderID = FIX50SP2.Tags.SecondaryOrderID(required=False)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.Quantity = FIX50SP2.Tags.Quantity(required=False)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.MarginExcess = FIX50SP2.Tags.MarginExcess(required=False)
                self.TotalNetValue = FIX50SP2.Tags.TotalNetValue(required=False)
                self.CashOutstanding = FIX50SP2.Tags.CashOutstanding(required=False)
                self.Side = FIX50SP2.Tags.Side(required=False)
                self.Price = FIX50SP2.Tags.Price(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.AccruedInterestAmt = FIX50SP2.Tags.AccruedInterestAmt(required=False)
                self.EndAccruedInterestAmt = FIX50SP2.Tags.EndAccruedInterestAmt(required=False)
                self.StartCash = FIX50SP2.Tags.StartCash(required=False)
                self.EndCash = FIX50SP2.Tags.EndCash(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.SettlSessID = FIX50SP2.Tags.SettlSessID(required=False)
                self.SettlSessSubID = FIX50SP2.Tags.SettlSessSubID(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.ExecCollGrp = FIX50SP2.Components.ExecCollGrp(required=False)
                self.TrdCollGrp = FIX50SP2.Components.TrdCollGrp(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.UndInstrmtCollGrp = FIX50SP2.Components.UndInstrmtCollGrp(required=False)
                self.TrdRegTimestamps = FIX50SP2.Components.TrdRegTimestamps(required=False)
                self.MiscFeesGrp = FIX50SP2.Components.MiscFeesGrp(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)

        class CollateralAssignment(AppMessage):
            MsgType = "AY"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AY"
                self.CollAsgnID = FIX50SP2.Tags.CollAsgnID(required=True)
                self.CollReqID = FIX50SP2.Tags.CollReqID(required=False)
                self.CollAsgnReason = FIX50SP2.Tags.CollAsgnReason(required=True)
                self.CollAsgnTransType = FIX50SP2.Tags.CollAsgnTransType(required=True)
                self.CollAsgnRefID = FIX50SP2.Tags.CollAsgnRefID(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.ExpireTime = FIX50SP2.Tags.ExpireTime(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                self.SecondaryOrderID = FIX50SP2.Tags.SecondaryOrderID(required=False)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.Quantity = FIX50SP2.Tags.Quantity(required=False)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.MarginExcess = FIX50SP2.Tags.MarginExcess(required=False)
                self.TotalNetValue = FIX50SP2.Tags.TotalNetValue(required=False)
                self.CashOutstanding = FIX50SP2.Tags.CashOutstanding(required=False)
                self.Side = FIX50SP2.Tags.Side(required=False)
                self.Price = FIX50SP2.Tags.Price(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.AccruedInterestAmt = FIX50SP2.Tags.AccruedInterestAmt(required=False)
                self.EndAccruedInterestAmt = FIX50SP2.Tags.EndAccruedInterestAmt(required=False)
                self.StartCash = FIX50SP2.Tags.StartCash(required=False)
                self.EndCash = FIX50SP2.Tags.EndCash(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.SettlSessID = FIX50SP2.Tags.SettlSessID(required=False)
                self.SettlSessSubID = FIX50SP2.Tags.SettlSessSubID(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.ExecCollGrp = FIX50SP2.Components.ExecCollGrp(required=False)
                self.TrdCollGrp = FIX50SP2.Components.TrdCollGrp(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.UndInstrmtCollGrp = FIX50SP2.Components.UndInstrmtCollGrp(required=False)
                self.TrdRegTimestamps = FIX50SP2.Components.TrdRegTimestamps(required=False)
                self.MiscFeesGrp = FIX50SP2.Components.MiscFeesGrp(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                self.SettlInstructionsData = FIX50SP2.Components.SettlInstructionsData(required=False)

        class CollateralResponse(AppMessage):
            MsgType = "AZ"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "AZ"
                self.CollRespID = FIX50SP2.Tags.CollRespID(required=True)
                self.CollAsgnID = FIX50SP2.Tags.CollAsgnID(required=False)
                self.CollReqID = FIX50SP2.Tags.CollReqID(required=False)
                self.CollAsgnReason = FIX50SP2.Tags.CollAsgnReason(required=False)
                self.CollAsgnTransType = FIX50SP2.Tags.CollAsgnTransType(required=False)
                self.CollAsgnRespType = FIX50SP2.Tags.CollAsgnRespType(required=True)
                self.CollAsgnRejectReason = FIX50SP2.Tags.CollAsgnRejectReason(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.CollApplType = FIX50SP2.Tags.CollApplType(required=False)
                self.FinancialStatus = FIX50SP2.Tags.FinancialStatus(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                self.SecondaryOrderID = FIX50SP2.Tags.SecondaryOrderID(required=False)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.Quantity = FIX50SP2.Tags.Quantity(required=False)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.MarginExcess = FIX50SP2.Tags.MarginExcess(required=False)
                self.TotalNetValue = FIX50SP2.Tags.TotalNetValue(required=False)
                self.CashOutstanding = FIX50SP2.Tags.CashOutstanding(required=False)
                self.Side = FIX50SP2.Tags.Side(required=False)
                self.Price = FIX50SP2.Tags.Price(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.AccruedInterestAmt = FIX50SP2.Tags.AccruedInterestAmt(required=False)
                self.EndAccruedInterestAmt = FIX50SP2.Tags.EndAccruedInterestAmt(required=False)
                self.StartCash = FIX50SP2.Tags.StartCash(required=False)
                self.EndCash = FIX50SP2.Tags.EndCash(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.ExecCollGrp = FIX50SP2.Components.ExecCollGrp(required=False)
                self.TrdCollGrp = FIX50SP2.Components.TrdCollGrp(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.UndInstrmtCollGrp = FIX50SP2.Components.UndInstrmtCollGrp(required=False)
                self.TrdRegTimestamps = FIX50SP2.Components.TrdRegTimestamps(required=False)
                self.MiscFeesGrp = FIX50SP2.Components.MiscFeesGrp(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)

        class CollateralReport(AppMessage):
            MsgType = "BA"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BA"
                self.CollRptID = FIX50SP2.Tags.CollRptID(required=True)
                self.CollInquiryID = FIX50SP2.Tags.CollInquiryID(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.CollApplType = FIX50SP2.Tags.CollApplType(required=False)
                self.FinancialStatus = FIX50SP2.Tags.FinancialStatus(required=False)
                self.CollStatus = FIX50SP2.Tags.CollStatus(required=True)
                self.TotNumReports = FIX50SP2.Tags.TotNumReports(required=False)
                self.LastRptRequested = FIX50SP2.Tags.LastRptRequested(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                self.SecondaryOrderID = FIX50SP2.Tags.SecondaryOrderID(required=False)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.Quantity = FIX50SP2.Tags.Quantity(required=False)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.MarginExcess = FIX50SP2.Tags.MarginExcess(required=False)
                self.TotalNetValue = FIX50SP2.Tags.TotalNetValue(required=False)
                self.CashOutstanding = FIX50SP2.Tags.CashOutstanding(required=False)
                self.Side = FIX50SP2.Tags.Side(required=False)
                self.Price = FIX50SP2.Tags.Price(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.AccruedInterestAmt = FIX50SP2.Tags.AccruedInterestAmt(required=False)
                self.EndAccruedInterestAmt = FIX50SP2.Tags.EndAccruedInterestAmt(required=False)
                self.StartCash = FIX50SP2.Tags.StartCash(required=False)
                self.EndCash = FIX50SP2.Tags.EndCash(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.SettlSessID = FIX50SP2.Tags.SettlSessID(required=False)
                self.SettlSessSubID = FIX50SP2.Tags.SettlSessSubID(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.ExecCollGrp = FIX50SP2.Components.ExecCollGrp(required=False)
                self.TrdCollGrp = FIX50SP2.Components.TrdCollGrp(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.TrdRegTimestamps = FIX50SP2.Components.TrdRegTimestamps(required=False)
                self.MiscFeesGrp = FIX50SP2.Components.MiscFeesGrp(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                self.SettlInstructionsData = FIX50SP2.Components.SettlInstructionsData(required=False)

        class CollateralInquiry(AppMessage):
            MsgType = "BB"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BB"
                self.CollInquiryID = FIX50SP2.Tags.CollInquiryID(required=True)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=False)
                self.ResponseTransportType = FIX50SP2.Tags.ResponseTransportType(required=False)
                self.ResponseDestination = FIX50SP2.Tags.ResponseDestination(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                self.SecondaryOrderID = FIX50SP2.Tags.SecondaryOrderID(required=False)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.Quantity = FIX50SP2.Tags.Quantity(required=False)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.MarginExcess = FIX50SP2.Tags.MarginExcess(required=False)
                self.TotalNetValue = FIX50SP2.Tags.TotalNetValue(required=False)
                self.CashOutstanding = FIX50SP2.Tags.CashOutstanding(required=False)
                self.Side = FIX50SP2.Tags.Side(required=False)
                self.Price = FIX50SP2.Tags.Price(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.AccruedInterestAmt = FIX50SP2.Tags.AccruedInterestAmt(required=False)
                self.EndAccruedInterestAmt = FIX50SP2.Tags.EndAccruedInterestAmt(required=False)
                self.StartCash = FIX50SP2.Tags.StartCash(required=False)
                self.EndCash = FIX50SP2.Tags.EndCash(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.SettlSessID = FIX50SP2.Tags.SettlSessID(required=False)
                self.SettlSessSubID = FIX50SP2.Tags.SettlSessSubID(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.CollInqQualGrp = FIX50SP2.Components.CollInqQualGrp(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.ExecCollGrp = FIX50SP2.Components.ExecCollGrp(required=False)
                self.TrdCollGrp = FIX50SP2.Components.TrdCollGrp(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.TrdRegTimestamps = FIX50SP2.Components.TrdRegTimestamps(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                self.SettlInstructionsData = FIX50SP2.Components.SettlInstructionsData(required=False)

        class NetworkCounterpartySystemStatusRequest(AppMessage):
            MsgType = "BC"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BC"
                self.NetworkRequestType = FIX50SP2.Tags.NetworkRequestType(required=True)
                self.NetworkRequestID = FIX50SP2.Tags.NetworkRequestID(required=True)
                self.CompIDReqGrp = FIX50SP2.Components.CompIDReqGrp(required=False)

        class NetworkCounterpartySystemStatusResponse(AppMessage):
            MsgType = "BD"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BD"
                self.NetworkStatusResponseType = FIX50SP2.Tags.NetworkStatusResponseType(required=True)
                self.NetworkRequestID = FIX50SP2.Tags.NetworkRequestID(required=False)
                self.NetworkResponseID = FIX50SP2.Tags.NetworkResponseID(required=True)
                self.LastNetworkResponseID = FIX50SP2.Tags.LastNetworkResponseID(required=False)
                self.CompIDStatGrp = FIX50SP2.Components.CompIDStatGrp(required=True)

        class UserRequest(AppMessage):
            MsgType = "BE"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BE"
                self.UserRequestID = FIX50SP2.Tags.UserRequestID(required=True)
                self.UserRequestType = FIX50SP2.Tags.UserRequestType(required=True)
                self.Username = FIX50SP2.Tags.Username(required=True)
                self.Password = FIX50SP2.Tags.Password(required=False)
                self.NewPassword = FIX50SP2.Tags.NewPassword(required=False)
                self.EncryptedPasswordMethod = FIX50SP2.Tags.EncryptedPasswordMethod(required=False)
                self.EncryptedPasswordLen = FIX50SP2.Tags.EncryptedPasswordLen(required=False)
                self.EncryptedPassword = FIX50SP2.Tags.EncryptedPassword(required=False)
                self.EncryptedNewPasswordLen = FIX50SP2.Tags.EncryptedNewPasswordLen(required=False)
                self.EncryptedNewPassword = FIX50SP2.Tags.EncryptedNewPassword(required=False)
                self.RawDataLength = FIX50SP2.Tags.RawDataLength(required=False)
                self.RawData = FIX50SP2.Tags.RawData(required=False)

        class UserResponse(AppMessage):
            MsgType = "BF"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BF"
                self.UserRequestID = FIX50SP2.Tags.UserRequestID(required=True)
                self.Username = FIX50SP2.Tags.Username(required=True)
                self.UserStatus = FIX50SP2.Tags.UserStatus(required=False)
                self.UserStatusText = FIX50SP2.Tags.UserStatusText(required=False)

        class CollateralInquiryAck(AppMessage):
            MsgType = "BG"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BG"
                self.CollInquiryID = FIX50SP2.Tags.CollInquiryID(required=True)
                self.CollInquiryStatus = FIX50SP2.Tags.CollInquiryStatus(required=True)
                self.CollInquiryResult = FIX50SP2.Tags.CollInquiryResult(required=False)
                self.TotNumReports = FIX50SP2.Tags.TotNumReports(required=False)
                self.Account = FIX50SP2.Tags.Account(required=False)
                self.AccountType = FIX50SP2.Tags.AccountType(required=False)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.OrderID = FIX50SP2.Tags.OrderID(required=False)
                self.SecondaryOrderID = FIX50SP2.Tags.SecondaryOrderID(required=False)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.Quantity = FIX50SP2.Tags.Quantity(required=False)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.SettlSessID = FIX50SP2.Tags.SettlSessID(required=False)
                self.SettlSessSubID = FIX50SP2.Tags.SettlSessSubID(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.ResponseTransportType = FIX50SP2.Tags.ResponseTransportType(required=False)
                self.ResponseDestination = FIX50SP2.Tags.ResponseDestination(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.CollInqQualGrp = FIX50SP2.Components.CollInqQualGrp(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.ExecCollGrp = FIX50SP2.Components.ExecCollGrp(required=False)
                self.TrdCollGrp = FIX50SP2.Components.TrdCollGrp(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)

        class ConfirmationRequest(AppMessage):
            MsgType = "BH"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BH"
                self.ConfirmReqID = FIX50SP2.Tags.ConfirmReqID(required=True)
                self.ConfirmType = FIX50SP2.Tags.ConfirmType(required=True)
                self.AllocID = FIX50SP2.Tags.AllocID(required=False)
                self.SecondaryAllocID = FIX50SP2.Tags.SecondaryAllocID(required=False)
                self.IndividualAllocID = FIX50SP2.Tags.IndividualAllocID(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.AllocAccount = FIX50SP2.Tags.AllocAccount(required=False)
                self.AllocAcctIDSource = FIX50SP2.Tags.AllocAcctIDSource(required=False)
                self.AllocAccountType = FIX50SP2.Tags.AllocAccountType(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.OrdAllocGrp = FIX50SP2.Components.OrdAllocGrp(required=False)

        class ContraryIntentionReport(AppMessage):
            MsgType = "BO"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BO"
                self.ContIntRptID = FIX50SP2.Tags.ContIntRptID(required=True)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.LateIndicator = FIX50SP2.Tags.LateIndicator(required=False)
                self.InputSource = FIX50SP2.Tags.InputSource(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=True)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=True)
                self.ExpirationQty = FIX50SP2.Components.ExpirationQty(required=True)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)

        class SecurityDefinitionUpdateReport(AppMessage):
            MsgType = "BP"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BP"
                self.SecurityReportID = FIX50SP2.Tags.SecurityReportID(required=False)
                self.SecurityReqID = FIX50SP2.Tags.SecurityReqID(required=False)
                self.SecurityResponseID = FIX50SP2.Tags.SecurityResponseID(required=False)
                self.SecurityResponseType = FIX50SP2.Tags.SecurityResponseType(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.SecurityUpdateAction = FIX50SP2.Tags.SecurityUpdateAction(required=False)
                self.CorporateAction = FIX50SP2.Tags.CorporateAction(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.InstrumentExtension = FIX50SP2.Components.InstrumentExtension(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.YieldData = FIX50SP2.Components.YieldData(required=False)
                self.MarketSegmentGrp = FIX50SP2.Components.MarketSegmentGrp(required=False)

        class SecurityListUpdateReport(AppMessage):
            MsgType = "BK"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BK"
                self.SecurityReportID = FIX50SP2.Tags.SecurityReportID(required=False)
                self.SecurityReqID = FIX50SP2.Tags.SecurityReqID(required=False)
                self.SecurityResponseID = FIX50SP2.Tags.SecurityResponseID(required=False)
                self.SecurityRequestResult = FIX50SP2.Tags.SecurityRequestResult(required=False)
                self.TotNoRelatedSym = FIX50SP2.Tags.TotNoRelatedSym(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.SecurityUpdateAction = FIX50SP2.Tags.SecurityUpdateAction(required=False)
                self.CorporateAction = FIX50SP2.Tags.CorporateAction(required=False)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.LastFragment = FIX50SP2.Tags.LastFragment(required=False)
                self.SecurityListID = FIX50SP2.Tags.SecurityListID(required=False)
                self.SecurityListRefID = FIX50SP2.Tags.SecurityListRefID(required=False)
                self.SecurityListDesc = FIX50SP2.Tags.SecurityListDesc(required=False)
                self.EncodedSecurityListDescLen = FIX50SP2.Tags.EncodedSecurityListDescLen(required=False)
                self.EncodedSecurityListDesc = FIX50SP2.Tags.EncodedSecurityListDesc(required=False)
                self.SecurityListType = FIX50SP2.Tags.SecurityListType(required=False)
                self.SecurityListTypeSource = FIX50SP2.Tags.SecurityListTypeSource(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.SecLstUpdRelSymGrp = FIX50SP2.Components.SecLstUpdRelSymGrp(required=False)

        class AdjustedPositionReport(AppMessage):
            MsgType = "BL"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BL"
                self.PosMaintRptID = FIX50SP2.Tags.PosMaintRptID(required=True)
                self.PosReqType = FIX50SP2.Tags.PosReqType(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=True)
                self.SettlSessID = FIX50SP2.Tags.SettlSessID(required=False)
                self.PosMaintRptRefID = FIX50SP2.Tags.PosMaintRptRefID(required=False)
                self.SettlPrice = FIX50SP2.Tags.SettlPrice(required=False)
                self.PriorSettlPrice = FIX50SP2.Tags.PriorSettlPrice(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=True)
                self.PositionQty = FIX50SP2.Components.PositionQty(required=True)
                self.InstrmtGrp = FIX50SP2.Components.InstrmtGrp(required=False)

        class AllocationInstructionAlert(AppMessage):
            MsgType = "BM"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BM"
                self.AllocID = FIX50SP2.Tags.AllocID(required=True)
                self.AllocTransType = FIX50SP2.Tags.AllocTransType(required=True)
                self.AllocType = FIX50SP2.Tags.AllocType(required=True)
                self.SecondaryAllocID = FIX50SP2.Tags.SecondaryAllocID(required=False)
                self.RefAllocID = FIX50SP2.Tags.RefAllocID(required=False)
                self.AllocCancReplaceReason = FIX50SP2.Tags.AllocCancReplaceReason(required=False)
                self.AllocIntermedReqType = FIX50SP2.Tags.AllocIntermedReqType(required=False)
                self.AllocLinkID = FIX50SP2.Tags.AllocLinkID(required=False)
                self.AllocLinkType = FIX50SP2.Tags.AllocLinkType(required=False)
                self.BookingRefID = FIX50SP2.Tags.BookingRefID(required=False)
                self.AllocNoOrdersType = FIX50SP2.Tags.AllocNoOrdersType(required=False)
                self.PreviouslyReported = FIX50SP2.Tags.PreviouslyReported(required=False)
                self.ReversalIndicator = FIX50SP2.Tags.ReversalIndicator(required=False)
                self.MatchType = FIX50SP2.Tags.MatchType(required=False)
                self.Side = FIX50SP2.Tags.Side(required=True)
                self.Quantity = FIX50SP2.Tags.Quantity(required=True)
                self.QtyType = FIX50SP2.Tags.QtyType(required=False)
                self.LastMkt = FIX50SP2.Tags.LastMkt(required=False)
                self.TradeOriginationDate = FIX50SP2.Tags.TradeOriginationDate(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.AvgPx = FIX50SP2.Tags.AvgPx(required=False)
                self.AvgParPx = FIX50SP2.Tags.AvgParPx(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.AvgPxPrecision = FIX50SP2.Tags.AvgPxPrecision(required=False)
                self.TradeDate = FIX50SP2.Tags.TradeDate(required=True)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.SettlType = FIX50SP2.Tags.SettlType(required=False)
                self.SettlDate = FIX50SP2.Tags.SettlDate(required=False)
                self.BookingType = FIX50SP2.Tags.BookingType(required=False)
                self.GrossTradeAmt = FIX50SP2.Tags.GrossTradeAmt(required=False)
                self.Concession = FIX50SP2.Tags.Concession(required=False)
                self.TotalTakedown = FIX50SP2.Tags.TotalTakedown(required=False)
                self.NetMoney = FIX50SP2.Tags.NetMoney(required=False)
                self.PositionEffect = FIX50SP2.Tags.PositionEffect(required=False)
                self.AutoAcceptIndicator = FIX50SP2.Tags.AutoAcceptIndicator(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.NumDaysInterest = FIX50SP2.Tags.NumDaysInterest(required=False)
                self.AccruedInterestRate = FIX50SP2.Tags.AccruedInterestRate(required=False)
                self.AccruedInterestAmt = FIX50SP2.Tags.AccruedInterestAmt(required=False)
                self.TotalAccruedInterestAmt = FIX50SP2.Tags.TotalAccruedInterestAmt(required=False)
                self.InterestAtMaturity = FIX50SP2.Tags.InterestAtMaturity(required=False)
                self.EndAccruedInterestAmt = FIX50SP2.Tags.EndAccruedInterestAmt(required=False)
                self.StartCash = FIX50SP2.Tags.StartCash(required=False)
                self.EndCash = FIX50SP2.Tags.EndCash(required=False)
                self.LegalConfirm = FIX50SP2.Tags.LegalConfirm(required=False)
                self.TotNoAllocs = FIX50SP2.Tags.TotNoAllocs(required=False)
                self.LastFragment = FIX50SP2.Tags.LastFragment(required=False)
                self.AvgPxIndicator = FIX50SP2.Tags.AvgPxIndicator(required=False)
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.TrdType = FIX50SP2.Tags.TrdType(required=False)
                self.TrdSubType = FIX50SP2.Tags.TrdSubType(required=False)
                self.CustOrderCapacity = FIX50SP2.Tags.CustOrderCapacity(required=False)
                self.TradeInputSource = FIX50SP2.Tags.TradeInputSource(required=False)
                self.MultiLegReportingType = FIX50SP2.Tags.MultiLegReportingType(required=False)
                self.MessageEventSource = FIX50SP2.Tags.MessageEventSource(required=False)
                self.RndPx = FIX50SP2.Tags.RndPx(required=False)
                self.OrdAllocGrp = FIX50SP2.Components.OrdAllocGrp(required=False)
                self.ExecAllocGrp = FIX50SP2.Components.ExecAllocGrp(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.InstrumentExtension = FIX50SP2.Components.InstrumentExtension(required=False)
                self.FinancingDetails = FIX50SP2.Components.FinancingDetails(required=False)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.SpreadOrBenchmarkCurveData = FIX50SP2.Components.SpreadOrBenchmarkCurveData(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.Stipulations = FIX50SP2.Components.Stipulations(required=False)
                self.YieldData = FIX50SP2.Components.YieldData(required=False)
                self.PositionAmountData = FIX50SP2.Components.PositionAmountData(required=False)
                self.AllocGrp = FIX50SP2.Components.AllocGrp(required=False)

        class ExecutionAcknowledgement(AppMessage):
            MsgType = "BN"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BN"
                self.OrderID = FIX50SP2.Tags.OrderID(required=True)
                self.SecondaryOrderID = FIX50SP2.Tags.SecondaryOrderID(required=False)
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.ExecAckStatus = FIX50SP2.Tags.ExecAckStatus(required=True)
                self.ExecID = FIX50SP2.Tags.ExecID(required=True)
                self.DKReason = FIX50SP2.Tags.DKReason(required=False)
                self.Side = FIX50SP2.Tags.Side(required=True)
                self.LastQty = FIX50SP2.Tags.LastQty(required=False)
                self.LastPx = FIX50SP2.Tags.LastPx(required=False)
                self.PriceType = FIX50SP2.Tags.PriceType(required=False)
                self.LastParPx = FIX50SP2.Tags.LastParPx(required=False)
                self.CumQty = FIX50SP2.Tags.CumQty(required=False)
                self.AvgPx = FIX50SP2.Tags.AvgPx(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=True)
                self.UndInstrmtGrp = FIX50SP2.Components.UndInstrmtGrp(required=False)
                self.InstrmtLegGrp = FIX50SP2.Components.InstrmtLegGrp(required=False)
                self.OrderQtyData = FIX50SP2.Components.OrderQtyData(required=True)

        class TradingSessionList(AppMessage):
            MsgType = "BJ"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BJ"
                self.TradSesReqID = FIX50SP2.Tags.TradSesReqID(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.TrdSessLstGrp = FIX50SP2.Components.TrdSessLstGrp(required=True)

        class TradingSessionListRequest(AppMessage):
            MsgType = "BI"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BI"
                self.TradSesReqID = FIX50SP2.Tags.TradSesReqID(required=True)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.SecurityExchange = FIX50SP2.Tags.SecurityExchange(required=False)
                self.TradSesMethod = FIX50SP2.Tags.TradSesMethod(required=False)
                self.TradSesMode = FIX50SP2.Tags.TradSesMode(required=False)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=True)

        class SettlementObligationReport(AppMessage):
            MsgType = "BQ"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BQ"
                self.ClearingBusinessDate = FIX50SP2.Tags.ClearingBusinessDate(required=False)
                self.SettlementCycleNo = FIX50SP2.Tags.SettlementCycleNo(required=False)
                self.SettlObligMsgID = FIX50SP2.Tags.SettlObligMsgID(required=True)
                self.SettlObligMode = FIX50SP2.Tags.SettlObligMode(required=True)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.SettlObligationInstructions = FIX50SP2.Components.SettlObligationInstructions(required=True)

        class DerivativeSecurityListUpdateReport(AppMessage):
            MsgType = "BR"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BR"
                self.SecurityReqID = FIX50SP2.Tags.SecurityReqID(required=False)
                self.SecurityResponseID = FIX50SP2.Tags.SecurityResponseID(required=False)
                self.SecurityRequestResult = FIX50SP2.Tags.SecurityRequestResult(required=False)
                self.SecurityUpdateAction = FIX50SP2.Tags.SecurityUpdateAction(required=False)
                self.TotNoRelatedSym = FIX50SP2.Tags.TotNoRelatedSym(required=False)
                self.LastFragment = FIX50SP2.Tags.LastFragment(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.UnderlyingInstrument = FIX50SP2.Components.UnderlyingInstrument(required=False)
                self.DerivativeSecurityDefinition = FIX50SP2.Components.DerivativeSecurityDefinition(required=False)
                self.RelSymDerivSecUpdGrp = FIX50SP2.Components.RelSymDerivSecUpdGrp(required=False)

        class TradingSessionListUpdateReport(AppMessage):
            MsgType = "BS"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BS"
                self.TradSesReqID = FIX50SP2.Tags.TradSesReqID(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.TrdSessLstGrp = FIX50SP2.Components.TrdSessLstGrp(required=True)

        class MarketDefinitionRequest(AppMessage):
            MsgType = "BT"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BT"
                self.MarketReqID = FIX50SP2.Tags.MarketReqID(required=True)
                self.SubscriptionRequestType = FIX50SP2.Tags.SubscriptionRequestType(required=True)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.ParentMktSegmID = FIX50SP2.Tags.ParentMktSegmID(required=False)

        class MarketDefinition(AppMessage):
            MsgType = "BU"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BU"
                self.MarketReportID = FIX50SP2.Tags.MarketReportID(required=True)
                self.MarketReqID = FIX50SP2.Tags.MarketReqID(required=False)
                self.MarketID = FIX50SP2.Tags.MarketID(required=True)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.MarketSegmentDesc = FIX50SP2.Tags.MarketSegmentDesc(required=False)
                self.EncodedMktSegmDescLen = FIX50SP2.Tags.EncodedMktSegmDescLen(required=False)
                self.EncodedMktSegmDesc = FIX50SP2.Tags.EncodedMktSegmDesc(required=False)
                self.ParentMktSegmID = FIX50SP2.Tags.ParentMktSegmID(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.BaseTradingRules = FIX50SP2.Components.BaseTradingRules(required=False)
                self.OrdTypeRules = FIX50SP2.Components.OrdTypeRules(required=False)
                self.TimeInForceRules = FIX50SP2.Components.TimeInForceRules(required=False)
                self.ExecInstRules = FIX50SP2.Components.ExecInstRules(required=False)

        class MarketDefinitionUpdateReport(AppMessage):
            MsgType = "BV"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BV"
                self.MarketReportID = FIX50SP2.Tags.MarketReportID(required=True)
                self.MarketReqID = FIX50SP2.Tags.MarketReqID(required=False)
                self.MarketUpdateAction = FIX50SP2.Tags.MarketUpdateAction(required=False)
                self.MarketID = FIX50SP2.Tags.MarketID(required=True)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.MarketSegmentDesc = FIX50SP2.Tags.MarketSegmentDesc(required=False)
                self.EncodedMktSegmDescLen = FIX50SP2.Tags.EncodedMktSegmDescLen(required=False)
                self.EncodedMktSegmDesc = FIX50SP2.Tags.EncodedMktSegmDesc(required=False)
                self.ParentMktSegmID = FIX50SP2.Tags.ParentMktSegmID(required=False)
                self.Currency = FIX50SP2.Tags.Currency(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.ApplicationSequenceControl = FIX50SP2.Components.ApplicationSequenceControl(required=False)
                self.BaseTradingRules = FIX50SP2.Components.BaseTradingRules(required=False)
                self.OrdTypeRules = FIX50SP2.Components.OrdTypeRules(required=False)
                self.TimeInForceRules = FIX50SP2.Components.TimeInForceRules(required=False)
                self.ExecInstRules = FIX50SP2.Components.ExecInstRules(required=False)

        class ApplicationMessageRequest(AppMessage):
            MsgType = "BW"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BW"
                self.ApplReqID = FIX50SP2.Tags.ApplReqID(required=True)
                self.ApplReqType = FIX50SP2.Tags.ApplReqType(required=True)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.ApplIDRequestGrp = FIX50SP2.Components.ApplIDRequestGrp(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)

        class ApplicationMessageRequestAck(AppMessage):
            MsgType = "BX"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BX"
                self.ApplResponseID = FIX50SP2.Tags.ApplResponseID(required=True)
                self.ApplReqID = FIX50SP2.Tags.ApplReqID(required=False)
                self.ApplReqType = FIX50SP2.Tags.ApplReqType(required=False)
                self.ApplResponseType = FIX50SP2.Tags.ApplResponseType(required=False)
                self.ApplTotalMessageCount = FIX50SP2.Tags.ApplTotalMessageCount(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.ApplIDRequestAckGrp = FIX50SP2.Components.ApplIDRequestAckGrp(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)

        class ApplicationMessageReport(AppMessage):
            MsgType = "BY"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BY"
                self.ApplReportID = FIX50SP2.Tags.ApplReportID(required=True)
                self.ApplReportType = FIX50SP2.Tags.ApplReportType(required=True)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.ApplReqID = FIX50SP2.Tags.ApplReqID(required=False)
                self.ApplIDReportGrp = FIX50SP2.Components.ApplIDReportGrp(required=False)

        class OrderMassActionReport(AppMessage):
            MsgType = "BZ"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "BZ"
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=False)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.MassActionReportID = FIX50SP2.Tags.MassActionReportID(required=True)
                self.MassActionType = FIX50SP2.Tags.MassActionType(required=True)
                self.MassActionScope = FIX50SP2.Tags.MassActionScope(required=True)
                self.MassActionResponse = FIX50SP2.Tags.MassActionResponse(required=True)
                self.MassActionRejectReason = FIX50SP2.Tags.MassActionRejectReason(required=False)
                self.TotalAffectedOrders = FIX50SP2.Tags.TotalAffectedOrders(required=False)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.Side = FIX50SP2.Tags.Side(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.AffectedOrdGrp = FIX50SP2.Components.AffectedOrdGrp(required=False)
                self.NotAffectedOrdersGrp = FIX50SP2.Components.NotAffectedOrdersGrp(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.UnderlyingInstrument = FIX50SP2.Components.UnderlyingInstrument(required=False)
                self.TargetParties = FIX50SP2.Components.TargetParties(required=False)

        class OrderMassActionRequest(AppMessage):
            MsgType = "CA"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "CA"
                self.ClOrdID = FIX50SP2.Tags.ClOrdID(required=True)
                self.SecondaryClOrdID = FIX50SP2.Tags.SecondaryClOrdID(required=False)
                self.MassActionType = FIX50SP2.Tags.MassActionType(required=True)
                self.MassActionScope = FIX50SP2.Tags.MassActionScope(required=True)
                self.MarketID = FIX50SP2.Tags.MarketID(required=False)
                self.MarketSegmentID = FIX50SP2.Tags.MarketSegmentID(required=False)
                self.TradingSessionID = FIX50SP2.Tags.TradingSessionID(required=False)
                self.TradingSessionSubID = FIX50SP2.Tags.TradingSessionSubID(required=False)
                self.Side = FIX50SP2.Tags.Side(required=False)
                self.TransactTime = FIX50SP2.Tags.TransactTime(required=True)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.Parties = FIX50SP2.Components.Parties(required=False)
                self.Instrument = FIX50SP2.Components.Instrument(required=False)
                self.UnderlyingInstrument = FIX50SP2.Components.UnderlyingInstrument(required=False)
                self.TargetParties = FIX50SP2.Components.TargetParties(required=False)

        class UserNotification(AppMessage):
            MsgType = "CB"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "CB"
                self.UserStatus = FIX50SP2.Tags.UserStatus(required=True)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)
                self.UsernameGrp = FIX50SP2.Components.UsernameGrp(required=False)

        class StreamAssignmentRequest(AppMessage):
            MsgType = "CC"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "CC"
                self.StreamAsgnReqID = FIX50SP2.Tags.StreamAsgnReqID(required=True)
                self.StreamAsgnReqType = FIX50SP2.Tags.StreamAsgnReqType(required=True)
                self.StrmAsgnReqGrp = FIX50SP2.Components.StrmAsgnReqGrp(required=True)

        class StreamAssignmentReport(AppMessage):
            MsgType = "CD"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "CD"
                self.StreamAsgnRptID = FIX50SP2.Tags.StreamAsgnRptID(required=True)
                self.StreamAsgnReqType = FIX50SP2.Tags.StreamAsgnReqType(required=False)
                self.StreamAsgnReqID = FIX50SP2.Tags.StreamAsgnReqID(required=False)
                self.StrmAsgnRptGrp = FIX50SP2.Components.StrmAsgnRptGrp(required=False)

        class StreamAssignmentReportACK(AppMessage):
            MsgType = "CE"
            def __init__(self):
                self.Header = FIX50SP2.Header()
                self.Header.MsgType.value = "CE"
                self.StreamAsgnAckType = FIX50SP2.Tags.StreamAsgnAckType(required=True)
                self.StreamAsgnRptID = FIX50SP2.Tags.StreamAsgnRptID(required=True)
                self.StreamAsgnRejReason = FIX50SP2.Tags.StreamAsgnRejReason(required=False)
                self.Text = FIX50SP2.Tags.Text(required=False)
                self.EncodedTextLen = FIX50SP2.Tags.EncodedTextLen(required=False)
                self.EncodedText = FIX50SP2.Tags.EncodedText(required=False)

