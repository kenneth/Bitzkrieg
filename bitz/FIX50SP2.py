#!/usr/bin/python3
class FIX50SP2:

    class Tags:

        class Account:
            Tag = 1
            Type = "STRING"

        class AdvId:
            Tag = 2
            Type = "STRING"

        class AdvRefID:
            Tag = 3
            Type = "STRING"

        class AdvSide:
            Tag = 4
            Type = "CHAR"
            class Values:
                BUY = "B"
                SELL = "S"
                TRADE = "T"
                CROSS = "X"

        class AdvTransType:
            Tag = 5
            Type = "STRING"
            class Values:
                NEW = "N"
                CANCEL = "C"
                REPLACE = "R"

        class AvgPx:
            Tag = 6
            Type = "PRICE"

        class BeginSeqNo:
            Tag = 7
            Type = "SEQNUM"

        class BeginString:
            Tag = 8
            Type = "STRING"

        class BodyLength:
            Tag = 9
            Type = "LENGTH"

        class CheckSum:
            Tag = 10
            Type = "STRING"

        class ClOrdID:
            Tag = 11
            Type = "STRING"

        class Commission:
            Tag = 12
            Type = "AMT"

        class CommType:
            Tag = 13
            Type = "CHAR"
            class Values:
                PER_UNIT = "1"
                PERCENT = "2"
                ABSOLUTE = "3"
                PERCENTAGE_WAIVED_4 = "4"
                PERCENTAGE_WAIVED_5 = "5"
                POINTS_PER_BOND_OR_CONTRACT = "6"

        class CumQty:
            Tag = 14
            Type = "QTY"

        class Currency:
            Tag = 15
            Type = "CURRENCY"

        class EndSeqNo:
            Tag = 16
            Type = "SEQNUM"

        class ExecID:
            Tag = 17
            Type = "STRING"

        class ExecInst:
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

        class ExecRefID:
            Tag = 19
            Type = "STRING"

        class HandlInst:
            Tag = 21
            Type = "CHAR"
            class Values:
                AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION = "1"
                AUTOMATED_EXECUTION_ORDER_PUBLIC_BROKER_INTERVENTION_OK = "2"
                MANUAL_ORDER_BEST_EXECUTION = "3"

        class SecurityIDSource:
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

        class IOIID:
            Tag = 23
            Type = "STRING"

        class IOIQltyInd:
            Tag = 25
            Type = "CHAR"
            class Values:
                HIGH = "H"
                LOW = "L"
                MEDIUM = "M"

        class IOIRefID:
            Tag = 26
            Type = "STRING"

        class IOIQty:
            Tag = 27
            Type = "STRING"
            class Values:
                SMALL = "S"
                MEDIUM = "M"
                LARGE = "L"
                UNDISCLOSED_QUANTITY = "U"

        class IOITransType:
            Tag = 28
            Type = "CHAR"
            class Values:
                NEW = "N"
                CANCEL = "C"
                REPLACE = "R"

        class LastCapacity:
            Tag = 29
            Type = "CHAR"
            class Values:
                AGENT = "1"
                CROSS_AS_AGENT = "2"
                CROSS_AS_PRINCIPAL = "3"
                PRINCIPAL = "4"

        class LastMkt:
            Tag = 30
            Type = "EXCHANGE"

        class LastPx:
            Tag = 31
            Type = "PRICE"

        class LastQty:
            Tag = 32
            Type = "QTY"

        class NoLinesOfText:
            Tag = 33
            Type = "NUMINGROUP"

        class MsgSeqNum:
            Tag = 34
            Type = "SEQNUM"

        class MsgType:
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

        class NewSeqNo:
            Tag = 36
            Type = "SEQNUM"

        class OrderID:
            Tag = 37
            Type = "STRING"

        class OrderQty:
            Tag = 38
            Type = "QTY"

        class OrdStatus:
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

        class OrdType:
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

        class OrigClOrdID:
            Tag = 41
            Type = "STRING"

        class OrigTime:
            Tag = 42
            Type = "UTCTIMESTAMP"

        class PossDupFlag:
            Tag = 43
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class Price:
            Tag = 44
            Type = "PRICE"

        class RefSeqNum:
            Tag = 45
            Type = "SEQNUM"

        class SecurityID:
            Tag = 48
            Type = "STRING"

        class SenderCompID:
            Tag = 49
            Type = "STRING"

        class SenderSubID:
            Tag = 50
            Type = "STRING"

        class SendingTime:
            Tag = 52
            Type = "UTCTIMESTAMP"

        class Quantity:
            Tag = 53
            Type = "QTY"

        class Side:
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

        class Symbol:
            Tag = 55
            Type = "STRING"

        class TargetCompID:
            Tag = 56
            Type = "STRING"

        class TargetSubID:
            Tag = 57
            Type = "STRING"

        class Text:
            Tag = 58
            Type = "STRING"

        class TimeInForce:
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

        class TransactTime:
            Tag = 60
            Type = "UTCTIMESTAMP"

        class Urgency:
            Tag = 61
            Type = "CHAR"
            class Values:
                NORMAL = "0"
                FLASH = "1"
                BACKGROUND = "2"

        class ValidUntilTime:
            Tag = 62
            Type = "UTCTIMESTAMP"

        class SettlType:
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

        class SettlDate:
            Tag = 64
            Type = "LOCALMKTDATE"

        class SymbolSfx:
            Tag = 65
            Type = "STRING"
            class Values:
                EUCP_WITH_LUMP_SUM_INTEREST_RATHER_THAN_DISCOUNT_PRICE = "CD"
                WHEN_ISSUED_FOR_A_SECURITY_TO_BE_REISSUED_UNDER_AN_OLD_CUSIP_OR_ISIN = "WI"

        class ListID:
            Tag = 66
            Type = "STRING"

        class ListSeqNo:
            Tag = 67
            Type = "INT"

        class TotNoOrders:
            Tag = 68
            Type = "INT"

        class ListExecInst:
            Tag = 69
            Type = "STRING"

        class AllocID:
            Tag = 70
            Type = "STRING"

        class AllocTransType:
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

        class RefAllocID:
            Tag = 72
            Type = "STRING"

        class NoOrders:
            Tag = 73
            Type = "NUMINGROUP"

        class AvgPxPrecision:
            Tag = 74
            Type = "INT"

        class TradeDate:
            Tag = 75
            Type = "LOCALMKTDATE"

        class PositionEffect:
            Tag = 77
            Type = "CHAR"
            class Values:
                CLOSE = "C"
                FIFO = "F"
                OPEN = "O"
                ROLLED = "R"
                CLOSE_BUT_NOTIFY_ON_OPEN = "N"
                DEFAULT = "D"

        class NoAllocs:
            Tag = 78
            Type = "NUMINGROUP"

        class AllocAccount:
            Tag = 79
            Type = "STRING"

        class AllocQty:
            Tag = 80
            Type = "QTY"

        class ProcessCode:
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

        class NoRpts:
            Tag = 82
            Type = "INT"

        class RptSeq:
            Tag = 83
            Type = "INT"

        class CxlQty:
            Tag = 84
            Type = "QTY"

        class NoDlvyInst:
            Tag = 85
            Type = "NUMINGROUP"

        class AllocStatus:
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

        class AllocRejCode:
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

        class Signature:
            Tag = 89
            Type = "DATA"

        class SecureDataLen:
            Tag = 90
            Type = "LENGTH"

        class SecureData:
            Tag = 91
            Type = "DATA"

        class SignatureLength:
            Tag = 93
            Type = "LENGTH"

        class EmailType:
            Tag = 94
            Type = "CHAR"
            class Values:
                NEW = "0"
                REPLY = "1"
                ADMIN_REPLY = "2"

        class RawDataLength:
            Tag = 95
            Type = "LENGTH"

        class RawData:
            Tag = 96
            Type = "DATA"

        class PossResend:
            Tag = 97
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class EncryptMethod:
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

        class StopPx:
            Tag = 99
            Type = "PRICE"

        class ExDestination:
            Tag = 100
            Type = "EXCHANGE"

        class CxlRejReason:
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

        class OrdRejReason:
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

        class IOIQualifier:
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

        class Issuer:
            Tag = 106
            Type = "STRING"

        class SecurityDesc:
            Tag = 107
            Type = "STRING"

        class HeartBtInt:
            Tag = 108
            Type = "INT"

        class MinQty:
            Tag = 110
            Type = "QTY"

        class MaxFloor:
            Tag = 111
            Type = "QTY"

        class TestReqID:
            Tag = 112
            Type = "STRING"

        class ReportToExch:
            Tag = 113
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class LocateReqd:
            Tag = 114
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class OnBehalfOfCompID:
            Tag = 115
            Type = "STRING"

        class OnBehalfOfSubID:
            Tag = 116
            Type = "STRING"

        class QuoteID:
            Tag = 117
            Type = "STRING"

        class NetMoney:
            Tag = 118
            Type = "AMT"

        class SettlCurrAmt:
            Tag = 119
            Type = "AMT"

        class SettlCurrency:
            Tag = 120
            Type = "CURRENCY"

        class ForexReq:
            Tag = 121
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class OrigSendingTime:
            Tag = 122
            Type = "UTCTIMESTAMP"

        class GapFillFlag:
            Tag = 123
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class NoExecs:
            Tag = 124
            Type = "NUMINGROUP"

        class ExpireTime:
            Tag = 126
            Type = "UTCTIMESTAMP"

        class DKReason:
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

        class DeliverToCompID:
            Tag = 128
            Type = "STRING"

        class DeliverToSubID:
            Tag = 129
            Type = "STRING"

        class IOINaturalFlag:
            Tag = 130
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class QuoteReqID:
            Tag = 131
            Type = "STRING"

        class BidPx:
            Tag = 132
            Type = "PRICE"

        class OfferPx:
            Tag = 133
            Type = "PRICE"

        class BidSize:
            Tag = 134
            Type = "QTY"

        class OfferSize:
            Tag = 135
            Type = "QTY"

        class NoMiscFees:
            Tag = 136
            Type = "NUMINGROUP"

        class MiscFeeAmt:
            Tag = 137
            Type = "AMT"

        class MiscFeeCurr:
            Tag = 138
            Type = "CURRENCY"

        class MiscFeeType:
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

        class PrevClosePx:
            Tag = 140
            Type = "PRICE"

        class ResetSeqNumFlag:
            Tag = 141
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class SenderLocationID:
            Tag = 142
            Type = "STRING"

        class TargetLocationID:
            Tag = 143
            Type = "STRING"

        class OnBehalfOfLocationID:
            Tag = 144
            Type = "STRING"

        class DeliverToLocationID:
            Tag = 145
            Type = "STRING"

        class NoRelatedSym:
            Tag = 146
            Type = "NUMINGROUP"

        class Subject:
            Tag = 147
            Type = "STRING"

        class Headline:
            Tag = 148
            Type = "STRING"

        class URLLink:
            Tag = 149
            Type = "STRING"

        class ExecType:
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

        class LeavesQty:
            Tag = 151
            Type = "QTY"

        class CashOrderQty:
            Tag = 152
            Type = "QTY"

        class AllocAvgPx:
            Tag = 153
            Type = "PRICE"

        class AllocNetMoney:
            Tag = 154
            Type = "AMT"

        class SettlCurrFxRate:
            Tag = 155
            Type = "FLOAT"

        class SettlCurrFxRateCalc:
            Tag = 156
            Type = "CHAR"
            class Values:
                MULTIPLY = "M"
                DIVIDE = "D"

        class NumDaysInterest:
            Tag = 157
            Type = "INT"

        class AccruedInterestRate:
            Tag = 158
            Type = "PERCENTAGE"

        class AccruedInterestAmt:
            Tag = 159
            Type = "AMT"

        class SettlInstMode:
            Tag = 160
            Type = "CHAR"
            class Values:
                DEFAULT = "0"
                STANDING_INSTRUCTIONS_PROVIDED = "1"
                SPECIFIC_ALLOCATION_ACCOUNT_OVERRIDING = "2"
                SPECIFIC_ALLOCATION_ACCOUNT_STANDING = "3"
                SPECIFIC_ORDER_FOR_A_SINGLE_ACCOUNT = "4"
                REQUEST_REJECT = "5"

        class AllocText:
            Tag = 161
            Type = "STRING"

        class SettlInstID:
            Tag = 162
            Type = "STRING"

        class SettlInstTransType:
            Tag = 163
            Type = "CHAR"
            class Values:
                NEW = "N"
                CANCEL = "C"
                REPLACE = "R"
                RESTATE = "T"

        class EmailThreadID:
            Tag = 164
            Type = "STRING"

        class SettlInstSource:
            Tag = 165
            Type = "CHAR"
            class Values:
                BROKERS_INSTRUCTIONS = "1"
                INSTITUTIONS_INSTRUCTIONS = "2"
                INVESTOR = "3"

        class SecurityType:
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

        class EffectiveTime:
            Tag = 168
            Type = "UTCTIMESTAMP"

        class StandInstDbType:
            Tag = 169
            Type = "INT"
            class Values:
                OTHER = 0
                DTC_SID = 1
                THOMSON_ALERT = 2
                A_GLOBAL_CUSTODIAN = 3
                ACCOUNTNET = 4

        class StandInstDbName:
            Tag = 170
            Type = "STRING"

        class StandInstDbID:
            Tag = 171
            Type = "STRING"

        class SettlDeliveryType:
            Tag = 172
            Type = "INT"
            class Values:
                VERSUS_PAYMENT_DELIVER = 0
                FREE_DELIVER = 1
                TRI_PARTY = 2
                HOLD_IN_CUSTODY = 3

        class BidSpotRate:
            Tag = 188
            Type = "PRICE"

        class BidForwardPoints:
            Tag = 189
            Type = "PRICEOFFSET"

        class OfferSpotRate:
            Tag = 190
            Type = "PRICE"

        class OfferForwardPoints:
            Tag = 191
            Type = "PRICEOFFSET"

        class OrderQty2:
            Tag = 192
            Type = "QTY"

        class SettlDate2:
            Tag = 193
            Type = "LOCALMKTDATE"

        class LastSpotRate:
            Tag = 194
            Type = "PRICE"

        class LastForwardPoints:
            Tag = 195
            Type = "PRICEOFFSET"

        class AllocLinkID:
            Tag = 196
            Type = "STRING"

        class AllocLinkType:
            Tag = 197
            Type = "INT"
            class Values:
                FX_NETTING = 0
                FX_SWAP = 1

        class SecondaryOrderID:
            Tag = 198
            Type = "STRING"

        class NoIOIQualifiers:
            Tag = 199
            Type = "NUMINGROUP"

        class MaturityMonthYear:
            Tag = 200
            Type = "MONTHYEAR"

        class PutOrCall:
            Tag = 201
            Type = "INT"
            class Values:
                PUT = 0
                CALL = 1

        class StrikePrice:
            Tag = 202
            Type = "PRICE"

        class CoveredOrUncovered:
            Tag = 203
            Type = "INT"
            class Values:
                COVERED = 0
                UNCOVERED = 1

        class OptAttribute:
            Tag = 206
            Type = "CHAR"

        class SecurityExchange:
            Tag = 207
            Type = "EXCHANGE"

        class NotifyBrokerOfCredit:
            Tag = 208
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class AllocHandlInst:
            Tag = 209
            Type = "INT"
            class Values:
                MATCH = 1
                FORWARD = 2
                FORWARD_AND_MATCH = 3

        class MaxShow:
            Tag = 210
            Type = "QTY"

        class PegOffsetValue:
            Tag = 211
            Type = "FLOAT"

        class XmlDataLen:
            Tag = 212
            Type = "LENGTH"

        class XmlData:
            Tag = 213
            Type = "DATA"

        class SettlInstRefID:
            Tag = 214
            Type = "STRING"

        class NoRoutingIDs:
            Tag = 215
            Type = "NUMINGROUP"

        class RoutingType:
            Tag = 216
            Type = "INT"
            class Values:
                TARGET_FIRM = 1
                TARGET_LIST = 2
                BLOCK_FIRM = 3
                BLOCK_LIST = 4

        class RoutingID:
            Tag = 217
            Type = "STRING"

        class Spread:
            Tag = 218
            Type = "PRICEOFFSET"

        class BenchmarkCurveCurrency:
            Tag = 220
            Type = "CURRENCY"

        class BenchmarkCurveName:
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

        class BenchmarkCurvePoint:
            Tag = 222
            Type = "STRING"

        class CouponRate:
            Tag = 223
            Type = "PERCENTAGE"

        class CouponPaymentDate:
            Tag = 224
            Type = "LOCALMKTDATE"

        class IssueDate:
            Tag = 225
            Type = "LOCALMKTDATE"

        class RepurchaseTerm:
            Tag = 226
            Type = "INT"

        class RepurchaseRate:
            Tag = 227
            Type = "PERCENTAGE"

        class Factor:
            Tag = 228
            Type = "FLOAT"

        class TradeOriginationDate:
            Tag = 229
            Type = "LOCALMKTDATE"

        class ExDate:
            Tag = 230
            Type = "LOCALMKTDATE"

        class ContractMultiplier:
            Tag = 231
            Type = "FLOAT"

        class NoStipulations:
            Tag = 232
            Type = "NUMINGROUP"

        class StipulationType:
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

        class StipulationValue:
            Tag = 234
            Type = "STRING"

        class YieldType:
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

        class Yield:
            Tag = 236
            Type = "PERCENTAGE"

        class TotalTakedown:
            Tag = 237
            Type = "AMT"

        class Concession:
            Tag = 238
            Type = "AMT"

        class RepoCollateralSecurityType:
            Tag = 239
            Type = "STRING"

        class RedemptionDate:
            Tag = 240
            Type = "LOCALMKTDATE"

        class UnderlyingCouponPaymentDate:
            Tag = 241
            Type = "LOCALMKTDATE"

        class UnderlyingIssueDate:
            Tag = 242
            Type = "LOCALMKTDATE"

        class UnderlyingRepoCollateralSecurityType:
            Tag = 243
            Type = "STRING"

        class UnderlyingRepurchaseTerm:
            Tag = 244
            Type = "INT"

        class UnderlyingRepurchaseRate:
            Tag = 245
            Type = "PERCENTAGE"

        class UnderlyingFactor:
            Tag = 246
            Type = "FLOAT"

        class UnderlyingRedemptionDate:
            Tag = 247
            Type = "LOCALMKTDATE"

        class LegCouponPaymentDate:
            Tag = 248
            Type = "LOCALMKTDATE"

        class LegIssueDate:
            Tag = 249
            Type = "LOCALMKTDATE"

        class LegRepoCollateralSecurityType:
            Tag = 250
            Type = "STRING"

        class LegRepurchaseTerm:
            Tag = 251
            Type = "INT"

        class LegRepurchaseRate:
            Tag = 252
            Type = "PERCENTAGE"

        class LegFactor:
            Tag = 253
            Type = "FLOAT"

        class LegRedemptionDate:
            Tag = 254
            Type = "LOCALMKTDATE"

        class CreditRating:
            Tag = 255
            Type = "STRING"

        class UnderlyingCreditRating:
            Tag = 256
            Type = "STRING"

        class LegCreditRating:
            Tag = 257
            Type = "STRING"

        class TradedFlatSwitch:
            Tag = 258
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class BasisFeatureDate:
            Tag = 259
            Type = "LOCALMKTDATE"

        class BasisFeaturePrice:
            Tag = 260
            Type = "PRICE"

        class MDReqID:
            Tag = 262
            Type = "STRING"

        class SubscriptionRequestType:
            Tag = 263
            Type = "CHAR"
            class Values:
                SNAPSHOT = "0"
                SNAPSHOT_PLUS_UPDATES = "1"
                DISABLE_PREVIOUS_SNAPSHOT_PLUS_UPDATE_REQUEST = "2"

        class MarketDepth:
            Tag = 264
            Type = "INT"

        class MDUpdateType:
            Tag = 265
            Type = "INT"
            class Values:
                FULL_REFRESH = 0
                INCREMENTAL_REFRESH = 1

        class AggregatedBook:
            Tag = 266
            Type = "BOOLEAN"
            class Values:
                YES = 1
                NO = 0

        class NoMDEntryTypes:
            Tag = 267
            Type = "NUMINGROUP"

        class NoMDEntries:
            Tag = 268
            Type = "NUMINGROUP"

        class MDEntryType:
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

        class MDEntryPx:
            Tag = 270
            Type = "PRICE"

        class MDEntrySize:
            Tag = 271
            Type = "QTY"

        class MDEntryDate:
            Tag = 272
            Type = "UTCDATEONLY"

        class MDEntryTime:
            Tag = 273
            Type = "UTCTIMEONLY"

        class TickDirection:
            Tag = 274
            Type = "CHAR"
            class Values:
                PLUS_TICK = "0"
                ZERO_PLUS_TICK = "1"
                MINUS_TICK = "2"
                ZERO_MINUS_TICK = "3"

        class MDMkt:
            Tag = 275
            Type = "EXCHANGE"

        class QuoteCondition:
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

        class TradeCondition:
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

        class MDEntryID:
            Tag = 278
            Type = "STRING"

        class MDUpdateAction:
            Tag = 279
            Type = "CHAR"
            class Values:
                NEW = "0"
                CHANGE = "1"
                DELETE = "2"
                DELETE_THRU = "3"
                DELETE_FROM = "4"
                OVERLAY = "5"

        class MDEntryRefID:
            Tag = 280
            Type = "STRING"

        class MDReqRejReason:
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

        class MDEntryOriginator:
            Tag = 282
            Type = "STRING"

        class LocationID:
            Tag = 283
            Type = "STRING"

        class DeskID:
            Tag = 284
            Type = "STRING"

        class DeleteReason:
            Tag = 285
            Type = "CHAR"
            class Values:
                CANCELLATION = "0"
                ERROR = "1"

        class OpenCloseSettlFlag:
            Tag = 286
            Type = "MULTIPLECHARVALUE"
            class Values:
                DAILY_OPEN = "0"
                SESSION_OPEN = "1"
                DELIVERY_SETTLEMENT_ENTRY = "2"
                EXPECTED_ENTRY = "3"
                ENTRY_FROM_PREVIOUS_BUSINESS_DAY = "4"
                THEORETICAL_PRICE_VALUE = "5"

        class SellerDays:
            Tag = 287
            Type = "INT"

        class MDEntryBuyer:
            Tag = 288
            Type = "STRING"

        class MDEntrySeller:
            Tag = 289
            Type = "STRING"

        class MDEntryPositionNo:
            Tag = 290
            Type = "INT"

        class FinancialStatus:
            Tag = 291
            Type = "MULTIPLECHARVALUE"
            class Values:
                BANKRUPT = "1"
                PENDING_DELISTING = "2"
                RESTRICTED = "3"

        class CorporateAction:
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

        class DefBidSize:
            Tag = 293
            Type = "QTY"

        class DefOfferSize:
            Tag = 294
            Type = "QTY"

        class NoQuoteEntries:
            Tag = 295
            Type = "NUMINGROUP"

        class NoQuoteSets:
            Tag = 296
            Type = "NUMINGROUP"

        class QuoteStatus:
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

        class QuoteCancelType:
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

        class QuoteEntryID:
            Tag = 299
            Type = "STRING"

        class QuoteRejectReason:
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

        class QuoteResponseLevel:
            Tag = 301
            Type = "INT"
            class Values:
                NO_ACKNOWLEDGEMENT = 0
                ACKNOWLEDGE_ONLY_NEGATIVE_OR_ERRONEOUS_QUOTES = 1
                ACKNOWLEDGE_EACH_QUOTE_MESSAGE = 2
                SUMMARY_ACKNOWLEDGEMENT = 3

        class QuoteSetID:
            Tag = 302
            Type = "STRING"

        class QuoteRequestType:
            Tag = 303
            Type = "INT"
            class Values:
                MANUAL = 1
                AUTOMATIC = 2

        class TotNoQuoteEntries:
            Tag = 304
            Type = "INT"

        class UnderlyingSecurityIDSource:
            Tag = 305
            Type = "STRING"

        class UnderlyingIssuer:
            Tag = 306
            Type = "STRING"

        class UnderlyingSecurityDesc:
            Tag = 307
            Type = "STRING"

        class UnderlyingSecurityExchange:
            Tag = 308
            Type = "EXCHANGE"

        class UnderlyingSecurityID:
            Tag = 309
            Type = "STRING"

        class UnderlyingSecurityType:
            Tag = 310
            Type = "STRING"

        class UnderlyingSymbol:
            Tag = 311
            Type = "STRING"

        class UnderlyingSymbolSfx:
            Tag = 312
            Type = "STRING"

        class UnderlyingMaturityMonthYear:
            Tag = 313
            Type = "MONTHYEAR"

        class UnderlyingPutOrCall:
            Tag = 315
            Type = "INT"

        class UnderlyingStrikePrice:
            Tag = 316
            Type = "PRICE"

        class UnderlyingOptAttribute:
            Tag = 317
            Type = "CHAR"

        class UnderlyingCurrency:
            Tag = 318
            Type = "CURRENCY"

        class SecurityReqID:
            Tag = 320
            Type = "STRING"

        class SecurityRequestType:
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

        class SecurityResponseID:
            Tag = 322
            Type = "STRING"

        class SecurityResponseType:
            Tag = 323
            Type = "INT"
            class Values:
                ACCEPT_SECURITY_PROPOSAL_AS_IS = 1
                ACCEPT_SECURITY_PROPOSAL_WITH_REVISIONS_AS_INDICATED_IN_THE_MESSAGE = 2
                LIST_OF_SECURITY_TYPES_RETURNED_PER_REQUEST = 3
                LIST_OF_SECURITIES_RETURNED_PER_REQUEST = 4
                REJECT_SECURITY_PROPOSAL = 5
                CANNOT_MATCH_SELECTION_CRITERIA = 6

        class SecurityStatusReqID:
            Tag = 324
            Type = "STRING"

        class UnsolicitedIndicator:
            Tag = 325
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class SecurityTradingStatus:
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

        class HaltReasonInt:
            Tag = 327
            Type = "INT"
            class Values:
                NEWS_DISSEMINATION = 0
                ORDER_INFLUX = 1
                ORDER_IMBALANCE = 2
                ADDITIONAL_INFORMATION = 3
                NEWS_PENDING = 4
                EQUIPMENT_CHANGEOVER = 5

        class InViewOfCommon:
            Tag = 328
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class DueToRelated:
            Tag = 329
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class BuyVolume:
            Tag = 330
            Type = "QTY"

        class SellVolume:
            Tag = 331
            Type = "QTY"

        class HighPx:
            Tag = 332
            Type = "PRICE"

        class LowPx:
            Tag = 333
            Type = "PRICE"

        class Adjustment:
            Tag = 334
            Type = "INT"
            class Values:
                CANCEL = 1
                ERROR = 2
                CORRECTION = 3

        class TradSesReqID:
            Tag = 335
            Type = "STRING"

        class TradingSessionID:
            Tag = 336
            Type = "STRING"
            class Values:
                DAY = "1"
                HALFDAY = "2"
                MORNING = "3"
                AFTERNOON = "4"
                EVENING = "5"
                AFTER_HOURS = "6"

        class ContraTrader:
            Tag = 337
            Type = "STRING"

        class TradSesMethod:
            Tag = 338
            Type = "INT"
            class Values:
                ELECTRONIC = 1
                OPEN_OUTCRY = 2
                TWO_PARTY = 3

        class TradSesMode:
            Tag = 339
            Type = "INT"
            class Values:
                TESTING = 1
                SIMULATED = 2
                PRODUCTION = 3

        class TradSesStatus:
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

        class TradSesStartTime:
            Tag = 341
            Type = "UTCTIMESTAMP"

        class TradSesOpenTime:
            Tag = 342
            Type = "UTCTIMESTAMP"

        class TradSesPreCloseTime:
            Tag = 343
            Type = "UTCTIMESTAMP"

        class TradSesCloseTime:
            Tag = 344
            Type = "UTCTIMESTAMP"

        class TradSesEndTime:
            Tag = 345
            Type = "UTCTIMESTAMP"

        class NumberOfOrders:
            Tag = 346
            Type = "INT"

        class MessageEncoding:
            Tag = 347
            Type = "STRING"

        class EncodedIssuerLen:
            Tag = 348
            Type = "LENGTH"

        class EncodedIssuer:
            Tag = 349
            Type = "DATA"

        class EncodedSecurityDescLen:
            Tag = 350
            Type = "LENGTH"

        class EncodedSecurityDesc:
            Tag = 351
            Type = "DATA"

        class EncodedListExecInstLen:
            Tag = 352
            Type = "LENGTH"

        class EncodedListExecInst:
            Tag = 353
            Type = "DATA"

        class EncodedTextLen:
            Tag = 354
            Type = "LENGTH"

        class EncodedText:
            Tag = 355
            Type = "DATA"

        class EncodedSubjectLen:
            Tag = 356
            Type = "LENGTH"

        class EncodedSubject:
            Tag = 357
            Type = "DATA"

        class EncodedHeadlineLen:
            Tag = 358
            Type = "LENGTH"

        class EncodedHeadline:
            Tag = 359
            Type = "DATA"

        class EncodedAllocTextLen:
            Tag = 360
            Type = "LENGTH"

        class EncodedAllocText:
            Tag = 361
            Type = "DATA"

        class EncodedUnderlyingIssuerLen:
            Tag = 362
            Type = "LENGTH"

        class EncodedUnderlyingIssuer:
            Tag = 363
            Type = "DATA"

        class EncodedUnderlyingSecurityDescLen:
            Tag = 364
            Type = "LENGTH"

        class EncodedUnderlyingSecurityDesc:
            Tag = 365
            Type = "DATA"

        class AllocPrice:
            Tag = 366
            Type = "PRICE"

        class QuoteSetValidUntilTime:
            Tag = 367
            Type = "UTCTIMESTAMP"

        class QuoteEntryRejectReason:
            Tag = 368
            Type = "INT"

        class LastMsgSeqNumProcessed:
            Tag = 369
            Type = "SEQNUM"

        class RefTagID:
            Tag = 371
            Type = "INT"

        class RefMsgType:
            Tag = 372
            Type = "STRING"

        class SessionRejectReason:
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

        class BidRequestTransType:
            Tag = 374
            Type = "CHAR"
            class Values:
                CANCEL = "C"
                NO = "N"

        class ContraBroker:
            Tag = 375
            Type = "STRING"

        class ComplianceID:
            Tag = 376
            Type = "STRING"

        class SolicitedFlag:
            Tag = 377
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class ExecRestatementReason:
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

        class BusinessRejectRefID:
            Tag = 379
            Type = "STRING"

        class BusinessRejectReason:
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

        class GrossTradeAmt:
            Tag = 381
            Type = "AMT"

        class NoContraBrokers:
            Tag = 382
            Type = "NUMINGROUP"

        class MaxMessageSize:
            Tag = 383
            Type = "LENGTH"

        class NoMsgTypes:
            Tag = 384
            Type = "NUMINGROUP"

        class MsgDirection:
            Tag = 385
            Type = "CHAR"
            class Values:
                RECEIVE = "R"
                SEND = "S"

        class NoTradingSessions:
            Tag = 386
            Type = "NUMINGROUP"

        class TotalVolumeTraded:
            Tag = 387
            Type = "QTY"

        class DiscretionInst:
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

        class DiscretionOffsetValue:
            Tag = 389
            Type = "FLOAT"

        class BidID:
            Tag = 390
            Type = "STRING"

        class ClientBidID:
            Tag = 391
            Type = "STRING"

        class ListName:
            Tag = 392
            Type = "STRING"

        class TotNoRelatedSym:
            Tag = 393
            Type = "INT"

        class BidType:
            Tag = 394
            Type = "INT"
            class Values:
                NON_DISCLOSED_STYLE = 1
                DISCLOSED_SYTLE = 2
                NO_BIDDING_PROCESS = 3

        class NumTickets:
            Tag = 395
            Type = "INT"

        class SideValue1:
            Tag = 396
            Type = "AMT"

        class SideValue2:
            Tag = 397
            Type = "AMT"

        class NoBidDescriptors:
            Tag = 398
            Type = "NUMINGROUP"

        class BidDescriptorType:
            Tag = 399
            Type = "INT"
            class Values:
                SECTOR = 1
                COUNTRY = 2
                INDEX = 3

        class BidDescriptor:
            Tag = 400
            Type = "STRING"

        class SideValueInd:
            Tag = 401
            Type = "INT"
            class Values:
                SIDE_VALUE_1 = 1
                SIDE_VALUE_2 = 2

        class LiquidityPctLow:
            Tag = 402
            Type = "PERCENTAGE"

        class LiquidityPctHigh:
            Tag = 403
            Type = "PERCENTAGE"

        class LiquidityValue:
            Tag = 404
            Type = "AMT"

        class EFPTrackingError:
            Tag = 405
            Type = "PERCENTAGE"

        class FairValue:
            Tag = 406
            Type = "AMT"

        class OutsideIndexPct:
            Tag = 407
            Type = "PERCENTAGE"

        class ValueOfFutures:
            Tag = 408
            Type = "AMT"

        class LiquidityIndType:
            Tag = 409
            Type = "INT"
            class Values:
                N5_DAY_MOVING_AVERAGE = 1
                N20_DAY_MOVING_AVERAGE = 2
                NORMAL_MARKET_SIZE = 3
                OTHER = 4

        class WtAverageLiquidity:
            Tag = 410
            Type = "PERCENTAGE"

        class ExchangeForPhysical:
            Tag = 411
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class OutMainCntryUIndex:
            Tag = 412
            Type = "AMT"

        class CrossPercent:
            Tag = 413
            Type = "PERCENTAGE"

        class ProgRptReqs:
            Tag = 414
            Type = "INT"
            class Values:
                BUY_SIDE_EXPLICITLY_REQUESTS_STATUS_USING_STATUE_REQUEST = 1
                SELL_SIDE_PERIODICALLY_SENDS_STATUS_USING_LIST_STATUS_PERIOD_OPTIONALLY_SPECIFIED_IN_PROGRESSPERIOD = 2
                REAL_TIME_EXECUTION_REPORTS = 3

        class ProgPeriodInterval:
            Tag = 415
            Type = "INT"

        class IncTaxInd:
            Tag = 416
            Type = "INT"
            class Values:
                NET = 1
                GROSS = 2

        class NumBidders:
            Tag = 417
            Type = "INT"

        class BidTradeType:
            Tag = 418
            Type = "CHAR"
            class Values:
                AGENCY = "A"
                VWAP_GUARANTEE = "G"
                GUARANTEED_CLOSE = "J"
                RISK_TRADE = "R"

        class BasisPxType:
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

        class NoBidComponents:
            Tag = 420
            Type = "NUMINGROUP"

        class Country:
            Tag = 421
            Type = "COUNTRY"

        class TotNoStrikes:
            Tag = 422
            Type = "INT"

        class PriceType:
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

        class DayOrderQty:
            Tag = 424
            Type = "QTY"

        class DayCumQty:
            Tag = 425
            Type = "QTY"

        class DayAvgPx:
            Tag = 426
            Type = "PRICE"

        class GTBookingInst:
            Tag = 427
            Type = "INT"
            class Values:
                BOOK_OUT_ALL_TRADES_ON_DAY_OF_EXECUTION = 0
                ACCUMULATE_EXECUTIONS_UNTIL_ORDER_IS_FILLED_OR_EXPIRES = 1
                ACCUMULATE_UNTIL_VERBALLY_NOTIFIED_OTHERWISE = 2

        class NoStrikes:
            Tag = 428
            Type = "NUMINGROUP"

        class ListStatusType:
            Tag = 429
            Type = "INT"
            class Values:
                ACK = 1
                RESPONSE = 2
                TIMED = 3
                EXEC_STARTED = 4
                ALL_DONE = 5
                ALERT = 6

        class NetGrossInd:
            Tag = 430
            Type = "INT"
            class Values:
                NET = 1
                GROSS = 2

        class ListOrderStatus:
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

        class ExpireDate:
            Tag = 432
            Type = "LOCALMKTDATE"

        class ListExecInstType:
            Tag = 433
            Type = "CHAR"
            class Values:
                IMMEDIATE = "1"
                WAIT_FOR_EXECUT_INSTRUCTION = "2"
                EXCHANGE_SWITCH_CIV_ORDER_3 = "3"
                EXCHANGE_SWITCH_CIV_ORDER_4 = "4"
                EXCHANGE_SWITCH_CIV_ORDER_5 = "5"

        class CxlRejResponseTo:
            Tag = 434
            Type = "CHAR"
            class Values:
                ORDER_CANCEL_REQUEST = "1"
                ORDER_CANCEL_REPLACE_REQUEST = "2"

        class UnderlyingCouponRate:
            Tag = 435
            Type = "PERCENTAGE"

        class UnderlyingContractMultiplier:
            Tag = 436
            Type = "FLOAT"

        class ContraTradeQty:
            Tag = 437
            Type = "QTY"

        class ContraTradeTime:
            Tag = 438
            Type = "UTCTIMESTAMP"

        class LiquidityNumSecurities:
            Tag = 441
            Type = "INT"

        class MultiLegReportingType:
            Tag = 442
            Type = "CHAR"
            class Values:
                SINGLE_SECURITY = "1"
                INDIVIDUAL_LEG_OF_A_MULTI_LEG_SECURITY = "2"
                MULTI_LEG_SECURITY = "3"

        class StrikeTime:
            Tag = 443
            Type = "UTCTIMESTAMP"

        class ListStatusText:
            Tag = 444
            Type = "STRING"

        class EncodedListStatusTextLen:
            Tag = 445
            Type = "LENGTH"

        class EncodedListStatusText:
            Tag = 446
            Type = "DATA"

        class PartyIDSource:
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

        class PartyID:
            Tag = 448
            Type = "STRING"

        class NetChgPrevDay:
            Tag = 451
            Type = "PRICEOFFSET"

        class PartyRole:
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

        class NoPartyIDs:
            Tag = 453
            Type = "NUMINGROUP"

        class NoSecurityAltID:
            Tag = 454
            Type = "NUMINGROUP"

        class SecurityAltID:
            Tag = 455
            Type = "STRING"

        class SecurityAltIDSource:
            Tag = 456
            Type = "STRING"

        class NoUnderlyingSecurityAltID:
            Tag = 457
            Type = "NUMINGROUP"

        class UnderlyingSecurityAltID:
            Tag = 458
            Type = "STRING"

        class UnderlyingSecurityAltIDSource:
            Tag = 459
            Type = "STRING"

        class Product:
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

        class CFICode:
            Tag = 461
            Type = "STRING"

        class UnderlyingProduct:
            Tag = 462
            Type = "INT"

        class UnderlyingCFICode:
            Tag = 463
            Type = "STRING"

        class TestMessageIndicator:
            Tag = 464
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class BookingRefID:
            Tag = 466
            Type = "STRING"

        class IndividualAllocID:
            Tag = 467
            Type = "STRING"

        class RoundingDirection:
            Tag = 468
            Type = "CHAR"
            class Values:
                ROUND_TO_NEAREST = "0"
                ROUND_DOWN = "1"
                ROUND_UP = "2"

        class RoundingModulus:
            Tag = 469
            Type = "FLOAT"

        class CountryOfIssue:
            Tag = 470
            Type = "COUNTRY"

        class StateOrProvinceOfIssue:
            Tag = 471
            Type = "STRING"

        class LocaleOfIssue:
            Tag = 472
            Type = "STRING"

        class NoRegistDtls:
            Tag = 473
            Type = "NUMINGROUP"

        class MailingDtls:
            Tag = 474
            Type = "STRING"

        class InvestorCountryOfResidence:
            Tag = 475
            Type = "COUNTRY"

        class PaymentRef:
            Tag = 476
            Type = "STRING"

        class DistribPaymentMethod:
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

        class CashDistribCurr:
            Tag = 478
            Type = "CURRENCY"

        class CommCurrency:
            Tag = 479
            Type = "CURRENCY"

        class CancellationRights:
            Tag = 480
            Type = "CHAR"
            class Values:
                YES = "Y"
                NO_N = "N"
                NO_M = "M"
                NO_O = "O"

        class MoneyLaunderingStatus:
            Tag = 481
            Type = "CHAR"
            class Values:
                PASSED = "Y"
                NOT_CHECKED = "N"
                EXEMPT_1 = "1"
                EXEMPT_2 = "2"
                EXEMPT_3 = "3"

        class MailingInst:
            Tag = 482
            Type = "STRING"

        class TransBkdTime:
            Tag = 483
            Type = "UTCTIMESTAMP"

        class ExecPriceType:
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

        class ExecPriceAdjustment:
            Tag = 485
            Type = "FLOAT"

        class DateOfBirth:
            Tag = 486
            Type = "LOCALMKTDATE"

        class TradeReportTransType:
            Tag = 487
            Type = "INT"
            class Values:
                NEW = 0
                CANCEL = 1
                REPLACE = 2
                RELEASE = 3
                REVERSE = 4
                CANCEL_DUE_TO_BACK_OUT_OF_TRADE = 5

        class CardHolderName:
            Tag = 488
            Type = "STRING"

        class CardNumber:
            Tag = 489
            Type = "STRING"

        class CardExpDate:
            Tag = 490
            Type = "LOCALMKTDATE"

        class CardIssNum:
            Tag = 491
            Type = "STRING"

        class PaymentMethod:
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

        class RegistAcctType:
            Tag = 493
            Type = "STRING"

        class Designation:
            Tag = 494
            Type = "STRING"

        class TaxAdvantageType:
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

        class RegistRejReasonText:
            Tag = 496
            Type = "STRING"

        class FundRenewWaiv:
            Tag = 497
            Type = "CHAR"
            class Values:
                NO = "N"
                YES = "Y"

        class CashDistribAgentName:
            Tag = 498
            Type = "STRING"

        class CashDistribAgentCode:
            Tag = 499
            Type = "STRING"

        class CashDistribAgentAcctNumber:
            Tag = 500
            Type = "STRING"

        class CashDistribPayRef:
            Tag = 501
            Type = "STRING"

        class CashDistribAgentAcctName:
            Tag = 502
            Type = "STRING"

        class CardStartDate:
            Tag = 503
            Type = "LOCALMKTDATE"

        class PaymentDate:
            Tag = 504
            Type = "LOCALMKTDATE"

        class PaymentRemitterID:
            Tag = 505
            Type = "STRING"

        class RegistStatus:
            Tag = 506
            Type = "CHAR"
            class Values:
                ACCEPTED = "A"
                REJECTED = "R"
                HELD = "H"
                REMINDER = "N"

        class RegistRejReasonCode:
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

        class RegistRefID:
            Tag = 508
            Type = "STRING"

        class RegistDtls:
            Tag = 509
            Type = "STRING"

        class NoDistribInsts:
            Tag = 510
            Type = "NUMINGROUP"

        class RegistEmail:
            Tag = 511
            Type = "STRING"

        class DistribPercentage:
            Tag = 512
            Type = "PERCENTAGE"

        class RegistID:
            Tag = 513
            Type = "STRING"

        class RegistTransType:
            Tag = 514
            Type = "CHAR"
            class Values:
                NEW = "0"
                CANCEL = "2"
                REPLACE = "1"

        class ExecValuationPoint:
            Tag = 515
            Type = "UTCTIMESTAMP"

        class OrderPercent:
            Tag = 516
            Type = "PERCENTAGE"

        class OwnershipType:
            Tag = 517
            Type = "CHAR"
            class Values:
                JOINT_INVESTORS = "J"
                TENANTS_IN_COMMON = "T"
                JOINT_TRUSTEES = "2"

        class NoContAmts:
            Tag = 518
            Type = "NUMINGROUP"

        class ContAmtType:
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

        class ContAmtValue:
            Tag = 520
            Type = "FLOAT"

        class ContAmtCurr:
            Tag = 521
            Type = "CURRENCY"

        class OwnerType:
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

        class PartySubID:
            Tag = 523
            Type = "STRING"

        class NestedPartyID:
            Tag = 524
            Type = "STRING"

        class NestedPartyIDSource:
            Tag = 525
            Type = "CHAR"

        class SecondaryClOrdID:
            Tag = 526
            Type = "STRING"

        class SecondaryExecID:
            Tag = 527
            Type = "STRING"

        class OrderCapacity:
            Tag = 528
            Type = "CHAR"
            class Values:
                AGENCY = "A"
                PROPRIETARY = "G"
                INDIVIDUAL = "I"
                PRINCIPAL = "P"
                RISKLESS_PRINCIPAL = "R"
                AGENT_FOR_OTHER_MEMBER = "W"

        class OrderRestrictions:
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

        class MassCancelRequestType:
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

        class MassCancelResponse:
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

        class MassCancelRejectReason:
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

        class TotalAffectedOrders:
            Tag = 533
            Type = "INT"

        class NoAffectedOrders:
            Tag = 534
            Type = "NUMINGROUP"

        class AffectedOrderID:
            Tag = 535
            Type = "STRING"

        class AffectedSecondaryOrderID:
            Tag = 536
            Type = "STRING"

        class QuoteType:
            Tag = 537
            Type = "INT"
            class Values:
                INDICATIVE = 0
                TRADEABLE = 1
                RESTRICTED_TRADEABLE = 2
                COUNTER = 3

        class NestedPartyRole:
            Tag = 538
            Type = "INT"

        class NoNestedPartyIDs:
            Tag = 539
            Type = "NUMINGROUP"

        class TotalAccruedInterestAmt:
            Tag = 540
            Type = "AMT"

        class MaturityDate:
            Tag = 541
            Type = "LOCALMKTDATE"

        class UnderlyingMaturityDate:
            Tag = 542
            Type = "LOCALMKTDATE"

        class InstrRegistry:
            Tag = 543
            Type = "STRING"

        class CashMargin:
            Tag = 544
            Type = "CHAR"
            class Values:
                CASH = "1"
                MARGIN_OPEN = "2"
                MARGIN_CLOSE = "3"

        class NestedPartySubID:
            Tag = 545
            Type = "STRING"

        class Scope:
            Tag = 546
            Type = "MULTIPLECHARVALUE"
            class Values:
                LOCAL_MARKET = "1"
                NATIONAL = "2"
                GLOBAL = "3"

        class MDImplicitDelete:
            Tag = 547
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class CrossID:
            Tag = 548
            Type = "STRING"

        class CrossType:
            Tag = 549
            Type = "INT"
            class Values:
                CROSS_AON = 1
                CROSS_IOC = 2
                CROSS_ONE_SIDE = 3
                CROSS_SAME_PRICE = 4

        class CrossPrioritization:
            Tag = 550
            Type = "INT"
            class Values:
                NONE = 0
                BUY_SIDE_IS_PRIORITIZED = 1
                SELL_SIDE_IS_PRIORITIZED = 2

        class OrigCrossID:
            Tag = 551
            Type = "STRING"

        class NoSides:
            Tag = 552
            Type = "NUMINGROUP"
            class Values:
                ONE_SIDE = 1
                BOTH_SIDES = 2

        class Username:
            Tag = 553
            Type = "STRING"

        class Password:
            Tag = 554
            Type = "STRING"

        class NoLegs:
            Tag = 555
            Type = "NUMINGROUP"

        class LegCurrency:
            Tag = 556
            Type = "CURRENCY"

        class TotNoSecurityTypes:
            Tag = 557
            Type = "INT"

        class NoSecurityTypes:
            Tag = 558
            Type = "NUMINGROUP"

        class SecurityListRequestType:
            Tag = 559
            Type = "INT"
            class Values:
                SYMBOL = 0
                SECURITYTYPE_AND_OR_CFICODE = 1
                PRODUCT = 2
                TRADINGSESSIONID = 3
                ALL_SECURITIES = 4
                MARKETID_OR_MARKETID_PLUS_MARKETSEGMENTID = 5

        class SecurityRequestResult:
            Tag = 560
            Type = "INT"
            class Values:
                VALID_REQUEST = 0
                INVALID_OR_UNSUPPORTED_REQUEST = 1
                NO_INSTRUMENTS_FOUND_THAT_MATCH_SELECTION_CRITERIA = 2
                NOT_AUTHORIZED_TO_RETRIEVE_INSTRUMENT_DATA = 3
                INSTRUMENT_DATA_TEMPORARILY_UNAVAILABLE = 4
                REQUEST_FOR_INSTRUMENT_DATA_NOT_SUPPORTED = 5

        class RoundLot:
            Tag = 561
            Type = "QTY"

        class MinTradeVol:
            Tag = 562
            Type = "QTY"

        class MultiLegRptTypeReq:
            Tag = 563
            Type = "INT"
            class Values:
                REPORT_BY_MULITLEG_SECURITY_ONLY = 0
                REPORT_BY_MULTILEG_SECURITY_AND_BY_INSTRUMENT_LEGS_BELONGING_TO_THE_MULTILEG_SECURITY = 1
                REPORT_BY_INSTRUMENT_LEGS_BELONGING_TO_THE_MULTILEG_SECURITY_ONLY = 2

        class LegPositionEffect:
            Tag = 564
            Type = "CHAR"

        class LegCoveredOrUncovered:
            Tag = 565
            Type = "INT"

        class LegPrice:
            Tag = 566
            Type = "PRICE"

        class TradSesStatusRejReason:
            Tag = 567
            Type = "INT"
            class Values:
                UNKNOWN_OR_INVALID_TRADINGSESSIONID = 1
                OTHER = 99

        class TradeRequestID:
            Tag = 568
            Type = "STRING"

        class TradeRequestType:
            Tag = 569
            Type = "INT"
            class Values:
                ALL_TRADES = 0
                MATCHED_TRADES_MATCHING_CRITERIA_PROVIDED_ON_REQUEST = 1
                UNMATCHED_TRADES_THAT_MATCH_CRITERIA = 2
                UNREPORTED_TRADES_THAT_MATCH_CRITERIA = 3
                ADVISORIES_THAT_MATCH_CRITERIA = 4

        class PreviouslyReported:
            Tag = 570
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class TradeReportID:
            Tag = 571
            Type = "STRING"

        class TradeReportRefID:
            Tag = 572
            Type = "STRING"

        class MatchStatus:
            Tag = 573
            Type = "CHAR"
            class Values:
                COMPARED_MATCHED_OR_AFFIRMED = "0"
                UNCOMPARED_UNMATCHED_OR_UNAFFIRMED = "1"
                ADVISORY_OR_ALERT = "2"

        class MatchType:
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

        class OddLot:
            Tag = 575
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class NoClearingInstructions:
            Tag = 576
            Type = "NUMINGROUP"

        class ClearingInstruction:
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

        class TradeInputSource:
            Tag = 578
            Type = "STRING"

        class TradeInputDevice:
            Tag = 579
            Type = "STRING"

        class NoDates:
            Tag = 580
            Type = "NUMINGROUP"

        class AccountType:
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

        class CustOrderCapacity:
            Tag = 582
            Type = "INT"
            class Values:
                MEMBER_TRADING_FOR_THEIR_OWN_ACCOUNT = 1
                CLEARING_FIRM_TRADING_FOR_ITS_PROPRIETARY_ACCOUNT = 2
                MEMBER_TRADING_FOR_ANOTHER_MEMBER = 3
                ALL_OTHER = 4

        class ClOrdLinkID:
            Tag = 583
            Type = "STRING"

        class MassStatusReqID:
            Tag = 584
            Type = "STRING"

        class MassStatusReqType:
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

        class OrigOrdModTime:
            Tag = 586
            Type = "UTCTIMESTAMP"

        class LegSettlType:
            Tag = 587
            Type = "CHAR"

        class LegSettlDate:
            Tag = 588
            Type = "LOCALMKTDATE"

        class DayBookingInst:
            Tag = 589
            Type = "CHAR"
            class Values:
                CAN_TRIGGER_BOOKING_WITHOUT_REFERENCE_TO_THE_ORDER_INITIATOR = "0"
                SPEAK_WITH_ORDER_INITIATOR_BEFORE_BOOKING = "1"
                ACCUMULATE = "2"

        class BookingUnit:
            Tag = 590
            Type = "CHAR"
            class Values:
                EACH_PARTIAL_EXECUTION_IS_A_BOOKABLE_UNIT = "0"
                AGGREGATE_PARTIAL_EXECUTIONS_ON_THIS_ORDER_AND_BOOK_ONE_TRADE_PER_ORDER = "1"
                AGGREGATE_EXECUTIONS_FOR_THIS_SYMBOL_SIDE_AND_SETTLEMENT_DATE = "2"

        class PreallocMethod:
            Tag = 591
            Type = "CHAR"
            class Values:
                PRO_RATA = "0"
                DO_NOT_PRO_RATA = "1"

        class UnderlyingCountryOfIssue:
            Tag = 592
            Type = "COUNTRY"

        class UnderlyingStateOrProvinceOfIssue:
            Tag = 593
            Type = "STRING"

        class UnderlyingLocaleOfIssue:
            Tag = 594
            Type = "STRING"

        class UnderlyingInstrRegistry:
            Tag = 595
            Type = "STRING"

        class LegCountryOfIssue:
            Tag = 596
            Type = "COUNTRY"

        class LegStateOrProvinceOfIssue:
            Tag = 597
            Type = "STRING"

        class LegLocaleOfIssue:
            Tag = 598
            Type = "STRING"

        class LegInstrRegistry:
            Tag = 599
            Type = "STRING"

        class LegSymbol:
            Tag = 600
            Type = "STRING"

        class LegSymbolSfx:
            Tag = 601
            Type = "STRING"

        class LegSecurityID:
            Tag = 602
            Type = "STRING"

        class LegSecurityIDSource:
            Tag = 603
            Type = "STRING"

        class NoLegSecurityAltID:
            Tag = 604
            Type = "NUMINGROUP"

        class LegSecurityAltID:
            Tag = 605
            Type = "STRING"

        class LegSecurityAltIDSource:
            Tag = 606
            Type = "STRING"

        class LegProduct:
            Tag = 607
            Type = "INT"

        class LegCFICode:
            Tag = 608
            Type = "STRING"

        class LegSecurityType:
            Tag = 609
            Type = "STRING"

        class LegMaturityMonthYear:
            Tag = 610
            Type = "MONTHYEAR"

        class LegMaturityDate:
            Tag = 611
            Type = "LOCALMKTDATE"

        class LegStrikePrice:
            Tag = 612
            Type = "PRICE"

        class LegOptAttribute:
            Tag = 613
            Type = "CHAR"

        class LegContractMultiplier:
            Tag = 614
            Type = "FLOAT"

        class LegCouponRate:
            Tag = 615
            Type = "PERCENTAGE"

        class LegSecurityExchange:
            Tag = 616
            Type = "EXCHANGE"

        class LegIssuer:
            Tag = 617
            Type = "STRING"

        class EncodedLegIssuerLen:
            Tag = 618
            Type = "LENGTH"

        class EncodedLegIssuer:
            Tag = 619
            Type = "DATA"

        class LegSecurityDesc:
            Tag = 620
            Type = "STRING"

        class EncodedLegSecurityDescLen:
            Tag = 621
            Type = "LENGTH"

        class EncodedLegSecurityDesc:
            Tag = 622
            Type = "DATA"

        class LegRatioQty:
            Tag = 623
            Type = "FLOAT"

        class LegSide:
            Tag = 624
            Type = "CHAR"

        class TradingSessionSubID:
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

        class AllocType:
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

        class NoHops:
            Tag = 627
            Type = "NUMINGROUP"

        class HopCompID:
            Tag = 628
            Type = "STRING"

        class HopSendingTime:
            Tag = 629
            Type = "UTCTIMESTAMP"

        class HopRefID:
            Tag = 630
            Type = "SEQNUM"

        class MidPx:
            Tag = 631
            Type = "PRICE"

        class BidYield:
            Tag = 632
            Type = "PERCENTAGE"

        class MidYield:
            Tag = 633
            Type = "PERCENTAGE"

        class OfferYield:
            Tag = 634
            Type = "PERCENTAGE"

        class ClearingFeeIndicator:
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

        class WorkingIndicator:
            Tag = 636
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class LegLastPx:
            Tag = 637
            Type = "PRICE"

        class PriorityIndicator:
            Tag = 638
            Type = "INT"
            class Values:
                PRIORITY_UNCHANGED = 0
                LOST_PRIORITY_AS_RESULT_OF_ORDER_CHANGE = 1

        class PriceImprovement:
            Tag = 639
            Type = "PRICEOFFSET"

        class Price2:
            Tag = 640
            Type = "PRICE"

        class LastForwardPoints2:
            Tag = 641
            Type = "PRICEOFFSET"

        class BidForwardPoints2:
            Tag = 642
            Type = "PRICEOFFSET"

        class OfferForwardPoints2:
            Tag = 643
            Type = "PRICEOFFSET"

        class RFQReqID:
            Tag = 644
            Type = "STRING"

        class MktBidPx:
            Tag = 645
            Type = "PRICE"

        class MktOfferPx:
            Tag = 646
            Type = "PRICE"

        class MinBidSize:
            Tag = 647
            Type = "QTY"

        class MinOfferSize:
            Tag = 648
            Type = "QTY"

        class QuoteStatusReqID:
            Tag = 649
            Type = "STRING"

        class LegalConfirm:
            Tag = 650
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class UnderlyingLastPx:
            Tag = 651
            Type = "PRICE"

        class UnderlyingLastQty:
            Tag = 652
            Type = "QTY"

        class LegRefID:
            Tag = 654
            Type = "STRING"

        class ContraLegRefID:
            Tag = 655
            Type = "STRING"

        class SettlCurrBidFxRate:
            Tag = 656
            Type = "FLOAT"

        class SettlCurrOfferFxRate:
            Tag = 657
            Type = "FLOAT"

        class QuoteRequestRejectReason:
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

        class SideComplianceID:
            Tag = 659
            Type = "STRING"

        class AcctIDSource:
            Tag = 660
            Type = "INT"
            class Values:
                BIC = 1
                SID_CODE = 2
                TFM = 3
                OMGEO = 4
                DTCC_CODE = 5
                OTHER = 99

        class AllocAcctIDSource:
            Tag = 661
            Type = "INT"

        class BenchmarkPrice:
            Tag = 662
            Type = "PRICE"

        class BenchmarkPriceType:
            Tag = 663
            Type = "INT"

        class ConfirmID:
            Tag = 664
            Type = "STRING"

        class ConfirmStatus:
            Tag = 665
            Type = "INT"
            class Values:
                RECEIVED = 1
                MISMATCHED_ACCOUNT = 2
                MISSING_SETTLEMENT_INSTRUCTIONS = 3
                CONFIRMED = 4
                REQUEST_REJECTED = 5

        class ConfirmTransType:
            Tag = 666
            Type = "INT"
            class Values:
                NEW = 0
                REPLACE = 1
                CANCEL = 2

        class ContractSettlMonth:
            Tag = 667
            Type = "MONTHYEAR"

        class DeliveryForm:
            Tag = 668
            Type = "INT"
            class Values:
                BOOK_ENTRY = 1
                BEARER = 2

        class LastParPx:
            Tag = 669
            Type = "PRICE"

        class NoLegAllocs:
            Tag = 670
            Type = "NUMINGROUP"

        class LegAllocAccount:
            Tag = 671
            Type = "STRING"

        class LegIndividualAllocID:
            Tag = 672
            Type = "STRING"

        class LegAllocQty:
            Tag = 673
            Type = "QTY"

        class LegAllocAcctIDSource:
            Tag = 674
            Type = "STRING"

        class LegSettlCurrency:
            Tag = 675
            Type = "CURRENCY"

        class LegBenchmarkCurveCurrency:
            Tag = 676
            Type = "CURRENCY"

        class LegBenchmarkCurveName:
            Tag = 677
            Type = "STRING"

        class LegBenchmarkCurvePoint:
            Tag = 678
            Type = "STRING"

        class LegBenchmarkPrice:
            Tag = 679
            Type = "PRICE"

        class LegBenchmarkPriceType:
            Tag = 680
            Type = "INT"

        class LegBidPx:
            Tag = 681
            Type = "PRICE"

        class LegIOIQty:
            Tag = 682
            Type = "STRING"

        class NoLegStipulations:
            Tag = 683
            Type = "NUMINGROUP"

        class LegOfferPx:
            Tag = 684
            Type = "PRICE"

        class LegOrderQty:
            Tag = 685
            Type = "QTY"

        class LegPriceType:
            Tag = 686
            Type = "INT"

        class LegQty:
            Tag = 687
            Type = "QTY"

        class LegStipulationType:
            Tag = 688
            Type = "STRING"

        class LegStipulationValue:
            Tag = 689
            Type = "STRING"

        class LegSwapType:
            Tag = 690
            Type = "INT"
            class Values:
                PAR_FOR_PAR = 1
                MODIFIED_DURATION = 2
                RISK = 4
                PROCEEDS = 5

        class Pool:
            Tag = 691
            Type = "STRING"

        class QuotePriceType:
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

        class QuoteRespID:
            Tag = 693
            Type = "STRING"

        class QuoteRespType:
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

        class QuoteQualifier:
            Tag = 695
            Type = "CHAR"

        class YieldRedemptionDate:
            Tag = 696
            Type = "LOCALMKTDATE"

        class YieldRedemptionPrice:
            Tag = 697
            Type = "PRICE"

        class YieldRedemptionPriceType:
            Tag = 698
            Type = "INT"

        class BenchmarkSecurityID:
            Tag = 699
            Type = "STRING"

        class ReversalIndicator:
            Tag = 700
            Type = "BOOLEAN"

        class YieldCalcDate:
            Tag = 701
            Type = "LOCALMKTDATE"

        class NoPositions:
            Tag = 702
            Type = "NUMINGROUP"

        class PosType:
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

        class LongQty:
            Tag = 704
            Type = "QTY"

        class ShortQty:
            Tag = 705
            Type = "QTY"

        class PosQtyStatus:
            Tag = 706
            Type = "INT"
            class Values:
                SUBMITTED = 0
                ACCEPTED = 1
                REJECTED = 2

        class PosAmtType:
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

        class PosAmt:
            Tag = 708
            Type = "AMT"

        class PosTransType:
            Tag = 709
            Type = "INT"
            class Values:
                EXERCISE = 1
                DO_NOT_EXERCISE = 2
                POSITION_ADJUSTMENT = 3
                POSITION_CHANGE_SUBMISSION_MARGIN_DISPOSITION = 4
                PLEDGE = 5
                LARGE_TRADER_SUBMISSION = 6

        class PosReqID:
            Tag = 710
            Type = "STRING"

        class NoUnderlyings:
            Tag = 711
            Type = "NUMINGROUP"

        class PosMaintAction:
            Tag = 712
            Type = "INT"
            class Values:
                NEW = 1
                REPLACE = 2
                CANCEL = 3
                REVERSE = 4

        class OrigPosReqRefID:
            Tag = 713
            Type = "STRING"

        class PosMaintRptRefID:
            Tag = 714
            Type = "STRING"

        class ClearingBusinessDate:
            Tag = 715
            Type = "LOCALMKTDATE"

        class SettlSessID:
            Tag = 716
            Type = "STRING"
            class Values:
                INTRADAY = "ITD"
                REGULAR_TRADING_HOURS = "RTH"
                ELECTRONIC_TRADING_HOURS = "ETH"
                END_OF_DAY = "EOD"

        class SettlSessSubID:
            Tag = 717
            Type = "STRING"

        class AdjustmentType:
            Tag = 718
            Type = "INT"
            class Values:
                PROCESS_REQUEST_AS_MARGIN_DISPOSITION = 0
                DELTA_PLUS = 1
                DELTA_MINUS = 2
                FINAL = 3

        class ContraryInstructionIndicator:
            Tag = 719
            Type = "BOOLEAN"

        class PriorSpreadIndicator:
            Tag = 720
            Type = "BOOLEAN"

        class PosMaintRptID:
            Tag = 721
            Type = "STRING"

        class PosMaintStatus:
            Tag = 722
            Type = "INT"
            class Values:
                ACCEPTED = 0
                ACCEPTED_WITH_WARNINGS = 1
                REJECTED = 2
                COMPLETED = 3
                COMPLETED_WITH_WARNINGS = 4

        class PosMaintResult:
            Tag = 723
            Type = "INT"
            class Values:
                SUCCESSFUL_COMPLETION = 0
                REJECTED = 1
                OTHER = 99

        class PosReqType:
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

        class ResponseTransportType:
            Tag = 725
            Type = "INT"
            class Values:
                INBAND = 0
                OUT_OF_BAND = 1

        class ResponseDestination:
            Tag = 726
            Type = "STRING"

        class TotalNumPosReports:
            Tag = 727
            Type = "INT"

        class PosReqResult:
            Tag = 728
            Type = "INT"
            class Values:
                VALID_REQUEST = 0
                INVALID_OR_UNSUPPORTED_REQUEST = 1
                NO_POSITIONS_FOUND_THAT_MATCH_CRITERIA = 2
                NOT_AUTHORIZED_TO_REQUEST_POSITIONS = 3
                REQUEST_FOR_POSITION_NOT_SUPPORTED = 4
                OTHER = 99

        class PosReqStatus:
            Tag = 729
            Type = "INT"
            class Values:
                COMPLETED = 0
                COMPLETED_WITH_WARNINGS = 1
                REJECTED = 2

        class SettlPrice:
            Tag = 730
            Type = "PRICE"

        class SettlPriceType:
            Tag = 731
            Type = "INT"
            class Values:
                FINAL = 1
                THEORETICAL = 2

        class UnderlyingSettlPrice:
            Tag = 732
            Type = "PRICE"

        class UnderlyingSettlPriceType:
            Tag = 733
            Type = "INT"

        class PriorSettlPrice:
            Tag = 734
            Type = "PRICE"

        class NoQuoteQualifiers:
            Tag = 735
            Type = "NUMINGROUP"

        class AllocSettlCurrency:
            Tag = 736
            Type = "CURRENCY"

        class AllocSettlCurrAmt:
            Tag = 737
            Type = "AMT"

        class InterestAtMaturity:
            Tag = 738
            Type = "AMT"

        class LegDatedDate:
            Tag = 739
            Type = "LOCALMKTDATE"

        class LegPool:
            Tag = 740
            Type = "STRING"

        class AllocInterestAtMaturity:
            Tag = 741
            Type = "AMT"

        class AllocAccruedInterestAmt:
            Tag = 742
            Type = "AMT"

        class DeliveryDate:
            Tag = 743
            Type = "LOCALMKTDATE"

        class AssignmentMethod:
            Tag = 744
            Type = "CHAR"
            class Values:
                PRO_RATA = "P"
                RANDOM = "R"

        class AssignmentUnit:
            Tag = 745
            Type = "QTY"

        class OpenInterest:
            Tag = 746
            Type = "AMT"

        class ExerciseMethod:
            Tag = 747
            Type = "CHAR"
            class Values:
                AUTOMATIC = "A"
                MANUAL = "M"

        class TotNumTradeReports:
            Tag = 748
            Type = "INT"

        class TradeRequestResult:
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

        class TradeRequestStatus:
            Tag = 750
            Type = "INT"
            class Values:
                ACCEPTED = 0
                COMPLETED = 1
                REJECTED = 2

        class TradeReportRejectReason:
            Tag = 751
            Type = "INT"
            class Values:
                SUCCESSFUL = 0
                INVALID_PARTY_ONFORMATION = 1
                UNKNOWN_INSTRUMENT = 2
                UNAUTHORIZED_TO_REPORT_TRADES = 3
                INVALID_TRADE_TYPE = 4
                OTHER = 99

        class SideMultiLegReportingType:
            Tag = 752
            Type = "INT"
            class Values:
                SINGLE_SECURITY = 1
                INDIVIDUAL_LEG_OF_A_MULTILEG_SECURITY = 2
                MULTILEG_SECURITY = 3

        class NoPosAmt:
            Tag = 753
            Type = "NUMINGROUP"

        class AutoAcceptIndicator:
            Tag = 754
            Type = "BOOLEAN"

        class AllocReportID:
            Tag = 755
            Type = "STRING"

        class NoNested2PartyIDs:
            Tag = 756
            Type = "NUMINGROUP"

        class Nested2PartyID:
            Tag = 757
            Type = "STRING"

        class Nested2PartyIDSource:
            Tag = 758
            Type = "CHAR"

        class Nested2PartyRole:
            Tag = 759
            Type = "INT"

        class Nested2PartySubID:
            Tag = 760
            Type = "STRING"

        class BenchmarkSecurityIDSource:
            Tag = 761
            Type = "STRING"

        class SecuritySubType:
            Tag = 762
            Type = "STRING"

        class UnderlyingSecuritySubType:
            Tag = 763
            Type = "STRING"

        class LegSecuritySubType:
            Tag = 764
            Type = "STRING"

        class AllowableOneSidednessPct:
            Tag = 765
            Type = "PERCENTAGE"

        class AllowableOneSidednessValue:
            Tag = 766
            Type = "AMT"

        class AllowableOneSidednessCurr:
            Tag = 767
            Type = "CURRENCY"

        class NoTrdRegTimestamps:
            Tag = 768
            Type = "NUMINGROUP"

        class TrdRegTimestamp:
            Tag = 769
            Type = "UTCTIMESTAMP"

        class TrdRegTimestampType:
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

        class TrdRegTimestampOrigin:
            Tag = 771
            Type = "STRING"

        class ConfirmRefID:
            Tag = 772
            Type = "STRING"

        class ConfirmType:
            Tag = 773
            Type = "INT"
            class Values:
                STATUS = 1
                CONFIRMATION = 2
                CONFIRMATION_REQUEST_REJECTED = 3

        class ConfirmRejReason:
            Tag = 774
            Type = "INT"
            class Values:
                MISMATCHED_ACCOUNT = 1
                MISSING_SETTLEMENT_INSTRUCTIONS = 2
                OTHER = 99

        class BookingType:
            Tag = 775
            Type = "INT"
            class Values:
                REGULAR_BOOKING = 0
                CFD = 1
                TOTAL_RETURN_SWAP = 2

        class IndividualAllocRejCode:
            Tag = 776
            Type = "INT"

        class SettlInstMsgID:
            Tag = 777
            Type = "STRING"

        class NoSettlInst:
            Tag = 778
            Type = "NUMINGROUP"

        class LastUpdateTime:
            Tag = 779
            Type = "UTCTIMESTAMP"

        class AllocSettlInstType:
            Tag = 780
            Type = "INT"
            class Values:
                USE_DEFAULT_INSTRUCTIONS = 0
                DERIVE_FROM_PARAMETERS_PROVIDED = 1
                FULL_DETAILS_PROVIDED = 2
                SSI_DB_IDS_PROVIDED = 3
                PHONE_FOR_INSTRUCTIONS = 4

        class NoSettlPartyIDs:
            Tag = 781
            Type = "NUMINGROUP"

        class SettlPartyID:
            Tag = 782
            Type = "STRING"

        class SettlPartyIDSource:
            Tag = 783
            Type = "CHAR"

        class SettlPartyRole:
            Tag = 784
            Type = "INT"

        class SettlPartySubID:
            Tag = 785
            Type = "STRING"

        class SettlPartySubIDType:
            Tag = 786
            Type = "INT"

        class DlvyInstType:
            Tag = 787
            Type = "CHAR"
            class Values:
                CASH = "C"
                SECURITIES = "S"

        class TerminationType:
            Tag = 788
            Type = "INT"
            class Values:
                OVERNIGHT = 1
                TERM = 2
                FLEXIBLE = 3
                OPEN = 4

        class NextExpectedMsgSeqNum:
            Tag = 789
            Type = "SEQNUM"

        class OrdStatusReqID:
            Tag = 790
            Type = "STRING"

        class SettlInstReqID:
            Tag = 791
            Type = "STRING"

        class SettlInstReqRejCode:
            Tag = 792
            Type = "INT"
            class Values:
                UNABLE_TO_PROCESS_REQUEST = 0
                UNKNOWN_ACCOUNT = 1
                NO_MATCHING_SETTLEMENT_INSTRUCTIONS_FOUND = 2
                OTHER = 99

        class SecondaryAllocID:
            Tag = 793
            Type = "STRING"

        class AllocReportType:
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

        class AllocReportRefID:
            Tag = 795
            Type = "STRING"

        class AllocCancReplaceReason:
            Tag = 796
            Type = "INT"
            class Values:
                ORIGINAL_DETAILS_INCOMPLETE_INCORRECT = 1
                CHANGE_IN_UNDERLYING_ORDER_DETAILS = 2
                OTHER = 99

        class CopyMsgIndicator:
            Tag = 797
            Type = "BOOLEAN"

        class AllocAccountType:
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

        class OrderAvgPx:
            Tag = 799
            Type = "PRICE"

        class OrderBookingQty:
            Tag = 800
            Type = "QTY"

        class NoSettlPartySubIDs:
            Tag = 801
            Type = "NUMINGROUP"

        class NoPartySubIDs:
            Tag = 802
            Type = "NUMINGROUP"

        class PartySubIDType:
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

        class NoNestedPartySubIDs:
            Tag = 804
            Type = "NUMINGROUP"

        class NestedPartySubIDType:
            Tag = 805
            Type = "INT"

        class NoNested2PartySubIDs:
            Tag = 806
            Type = "NUMINGROUP"

        class Nested2PartySubIDType:
            Tag = 807
            Type = "INT"

        class AllocIntermedReqType:
            Tag = 808
            Type = "INT"
            class Values:
                PENDING_ACCEPT = 1
                PENDING_RELEASE = 2
                PENDING_REVERSAL = 3
                ACCEPT = 4
                BLOCK_LEVEL_REJECT = 5
                ACCOUNT_LEVEL_REJECT = 6

        class NoUsernames:
            Tag = 809
            Type = "NUMINGROUP"

        class UnderlyingPx:
            Tag = 810
            Type = "PRICE"

        class PriceDelta:
            Tag = 811
            Type = "FLOAT"

        class ApplQueueMax:
            Tag = 812
            Type = "INT"

        class ApplQueueDepth:
            Tag = 813
            Type = "INT"

        class ApplQueueResolution:
            Tag = 814
            Type = "INT"
            class Values:
                NO_ACTION_TAKEN = 0
                QUEUE_FLUSHED = 1
                OVERLAY_LAST = 2
                END_SESSION = 3

        class ApplQueueAction:
            Tag = 815
            Type = "INT"
            class Values:
                NO_ACTION_TAKEN = 0
                QUEUE_FLUSHED = 1
                OVERLAY_LAST = 2
                END_SESSION = 3

        class NoAltMDSource:
            Tag = 816
            Type = "NUMINGROUP"

        class AltMDSourceID:
            Tag = 817
            Type = "STRING"

        class SecondaryTradeReportID:
            Tag = 818
            Type = "STRING"

        class AvgPxIndicator:
            Tag = 819
            Type = "INT"
            class Values:
                NO_AVERAGE_PRICING = 0
                TRADE_IS_PART_OF_AN_AVERAGE_PRICE_GROUP_IDENTIFIED_BY_THE_TRADELINKID = 1
                LAST_TRADE_IS_THE_AVERAGE_PRICE_GROUP_IDENTIFIED_BY_THE_TRADELINKID = 2

        class TradeLinkID:
            Tag = 820
            Type = "STRING"

        class OrderInputDevice:
            Tag = 821
            Type = "STRING"

        class UnderlyingTradingSessionID:
            Tag = 822
            Type = "STRING"

        class UnderlyingTradingSessionSubID:
            Tag = 823
            Type = "STRING"

        class TradeLegRefID:
            Tag = 824
            Type = "STRING"

        class ExchangeRule:
            Tag = 825
            Type = "STRING"

        class TradeAllocIndicator:
            Tag = 826
            Type = "INT"
            class Values:
                ALLOCATION_NOT_REQUIRED = 0
                ALLOCATION_REQUIRED = 1
                USE_ALLOCATION_PROVIDED_WITH_THE_TRADE = 2
                ALLOCATION_GIVE_UP_EXECUTOR = 3
                ALLOCATION_FROM_EXECUTOR = 4
                ALLOCATION_TO_CLAIM_ACCOUNT = 5

        class ExpirationCycle:
            Tag = 827
            Type = "INT"
            class Values:
                EXPIRE_ON_TRADING_SESSION_CLOSE = 0
                EXPIRE_ON_TRADING_SESSION_OPEN = 1
                TRADING_ELIGIBILITY_EXPIRATION_SPECIFIED_IN_THE_DATE_AND_TIME_FIELDS_EVENTDATE = 2

        class TrdType:
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

        class TrdSubType:
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

        class TransferReason:
            Tag = 830
            Type = "STRING"

        class TotNumAssignmentReports:
            Tag = 832
            Type = "INT"

        class AsgnRptID:
            Tag = 833
            Type = "STRING"

        class ThresholdAmount:
            Tag = 834
            Type = "PRICEOFFSET"

        class PegMoveType:
            Tag = 835
            Type = "INT"
            class Values:
                FLOATING = 0
                FIXED = 1

        class PegOffsetType:
            Tag = 836
            Type = "INT"
            class Values:
                PRICE = 0
                BASIS_POINTS = 1
                TICKS = 2
                PRICE_TIER = 3

        class PegLimitType:
            Tag = 837
            Type = "INT"
            class Values:
                OR_BETTER = 0
                STRICT = 1
                OR_WORSE = 2

        class PegRoundDirection:
            Tag = 838
            Type = "INT"
            class Values:
                MORE_AGGRESSIVE = 1
                MORE_PASSIVE = 2

        class PeggedPrice:
            Tag = 839
            Type = "PRICE"

        class PegScope:
            Tag = 840
            Type = "INT"
            class Values:
                LOCAL = 1
                NATIONAL = 2
                GLOBAL = 3
                NATIONAL_EXCLUDING_LOCAL = 4

        class DiscretionMoveType:
            Tag = 841
            Type = "INT"
            class Values:
                FLOATING = 0
                FIXED = 1

        class DiscretionOffsetType:
            Tag = 842
            Type = "INT"
            class Values:
                PRICE = 0
                BASIS_POINTS = 1
                TICKS = 2
                PRICE_TIER = 3

        class DiscretionLimitType:
            Tag = 843
            Type = "INT"
            class Values:
                OR_BETTER = 0
                STRICT = 1
                OR_WORSE = 2

        class DiscretionRoundDirection:
            Tag = 844
            Type = "INT"
            class Values:
                MORE_AGGRESSIVE = 1
                MORE_PASSIVE = 2

        class DiscretionPrice:
            Tag = 845
            Type = "PRICE"

        class DiscretionScope:
            Tag = 846
            Type = "INT"
            class Values:
                LOCAL = 1
                NATIONAL = 2
                GLOBAL = 3
                NATIONAL_EXCLUDING_LOCAL = 4

        class TargetStrategy:
            Tag = 847
            Type = "INT"
            class Values:
                VWAP = 1
                PARTICIPATE = 2
                MININIZE_MARKET_IMPACT = 3

        class TargetStrategyParameters:
            Tag = 848
            Type = "STRING"

        class ParticipationRate:
            Tag = 849
            Type = "PERCENTAGE"

        class TargetStrategyPerformance:
            Tag = 850
            Type = "FLOAT"

        class LastLiquidityInd:
            Tag = 851
            Type = "INT"
            class Values:
                ADDED_LIQUIDITY = 1
                REMOVED_LIQUIDITY = 2
                LIQUIDITY_ROUTED_OUT = 3
                AUCTION = 4

        class PublishTrdIndicator:
            Tag = 852
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class ShortSaleReason:
            Tag = 853
            Type = "INT"
            class Values:
                DEALER_SOLD_SHORT = 0
                DEALER_SOLD_SHORT_EXEMPT = 1
                SELLING_CUSTOMER_SOLD_SHORT = 2
                SELLING_CUSTOMER_SOLD_SHORT_EXEMPT = 3
                QUALIFIED_SERVICE_REPRESENTATIVE = 4
                QSR_OR_AGU_CONTRA_SIDE_SOLD_SHORT_EXEMPT = 5

        class QtyType:
            Tag = 854
            Type = "INT"
            class Values:
                UNITS = 0
                CONTRACTS = 1
                UNITS_OF_MEASURE_PER_TIME_UNIT = 2

        class SecondaryTrdType:
            Tag = 855
            Type = "INT"

        class TradeReportType:
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

        class AllocNoOrdersType:
            Tag = 857
            Type = "INT"
            class Values:
                NOT_SPECIFIED = 0
                EXPLICIT_LIST_PROVIDED = 1

        class SharedCommission:
            Tag = 858
            Type = "AMT"

        class ConfirmReqID:
            Tag = 859
            Type = "STRING"

        class AvgParPx:
            Tag = 860
            Type = "PRICE"

        class ReportedPx:
            Tag = 861
            Type = "PRICE"

        class NoCapacities:
            Tag = 862
            Type = "NUMINGROUP"

        class OrderCapacityQty:
            Tag = 863
            Type = "QTY"

        class NoEvents:
            Tag = 864
            Type = "NUMINGROUP"

        class EventType:
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

        class EventDate:
            Tag = 866
            Type = "LOCALMKTDATE"

        class EventPx:
            Tag = 867
            Type = "PRICE"

        class EventText:
            Tag = 868
            Type = "STRING"

        class PctAtRisk:
            Tag = 869
            Type = "PERCENTAGE"

        class NoInstrAttrib:
            Tag = 870
            Type = "NUMINGROUP"

        class InstrAttribType:
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

        class InstrAttribValue:
            Tag = 872
            Type = "STRING"

        class DatedDate:
            Tag = 873
            Type = "LOCALMKTDATE"

        class InterestAccrualDate:
            Tag = 874
            Type = "LOCALMKTDATE"

        class CPProgram:
            Tag = 875
            Type = "INT"
            class Values:
                N3 = 1
                N4 = 2
                OTHER = 99

        class CPRegType:
            Tag = 876
            Type = "STRING"

        class UnderlyingCPProgram:
            Tag = 877
            Type = "STRING"

        class UnderlyingCPRegType:
            Tag = 878
            Type = "STRING"

        class UnderlyingQty:
            Tag = 879
            Type = "QTY"

        class TrdMatchID:
            Tag = 880
            Type = "STRING"

        class SecondaryTradeReportRefID:
            Tag = 881
            Type = "STRING"

        class UnderlyingDirtyPrice:
            Tag = 882
            Type = "PRICE"

        class UnderlyingEndPrice:
            Tag = 883
            Type = "PRICE"

        class UnderlyingStartValue:
            Tag = 884
            Type = "AMT"

        class UnderlyingCurrentValue:
            Tag = 885
            Type = "AMT"

        class UnderlyingEndValue:
            Tag = 886
            Type = "AMT"

        class NoUnderlyingStips:
            Tag = 887
            Type = "NUMINGROUP"

        class UnderlyingStipType:
            Tag = 888
            Type = "STRING"

        class UnderlyingStipValue:
            Tag = 889
            Type = "STRING"

        class MaturityNetMoney:
            Tag = 890
            Type = "AMT"

        class MiscFeeBasis:
            Tag = 891
            Type = "INT"
            class Values:
                ABSOLUTE = 0
                PER_UNIT = 1
                PERCENTAGE = 2

        class TotNoAllocs:
            Tag = 892
            Type = "INT"

        class LastFragment:
            Tag = 893
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class CollReqID:
            Tag = 894
            Type = "STRING"

        class CollAsgnReason:
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

        class CollInquiryQualifier:
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

        class NoTrades:
            Tag = 897
            Type = "NUMINGROUP"

        class MarginRatio:
            Tag = 898
            Type = "PERCENTAGE"

        class MarginExcess:
            Tag = 899
            Type = "AMT"

        class TotalNetValue:
            Tag = 900
            Type = "AMT"

        class CashOutstanding:
            Tag = 901
            Type = "AMT"

        class CollAsgnID:
            Tag = 902
            Type = "STRING"

        class CollAsgnTransType:
            Tag = 903
            Type = "INT"
            class Values:
                NEW = 0
                REPLACE = 1
                CANCEL = 2
                RELEASE = 3
                REVERSE = 4

        class CollRespID:
            Tag = 904
            Type = "STRING"

        class CollAsgnRespType:
            Tag = 905
            Type = "INT"
            class Values:
                RECEIVED = 0
                ACCEPTED = 1
                DECLINED = 2
                REJECTED = 3

        class CollAsgnRejectReason:
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

        class CollAsgnRefID:
            Tag = 907
            Type = "STRING"

        class CollRptID:
            Tag = 908
            Type = "STRING"

        class CollInquiryID:
            Tag = 909
            Type = "STRING"

        class CollStatus:
            Tag = 910
            Type = "INT"
            class Values:
                UNASSIGNED = 0
                PARTIALLY_ASSIGNED = 1
                ASSIGNMENT_PROPOSED = 2
                ASSIGNED = 3
                CHALLENGED = 4

        class TotNumReports:
            Tag = 911
            Type = "INT"

        class LastRptRequested:
            Tag = 912
            Type = "BOOLEAN"
            class Values:
                NO = 0
                YES = 1

        class AgreementDesc:
            Tag = 913
            Type = "STRING"

        class AgreementID:
            Tag = 914
            Type = "STRING"

        class AgreementDate:
            Tag = 915
            Type = "LOCALMKTDATE"

        class StartDate:
            Tag = 916
            Type = "LOCALMKTDATE"

        class EndDate:
            Tag = 917
            Type = "LOCALMKTDATE"

        class AgreementCurrency:
            Tag = 918
            Type = "CURRENCY"

        class DeliveryType:
            Tag = 919
            Type = "INT"
            class Values:
                VERSUS_PAYMENT_DELIVER = 0
                FREE_DELIVER = 1
                TRI_PARTY = 2
                HOLD_IN_CUSTODY = 3

        class EndAccruedInterestAmt:
            Tag = 920
            Type = "AMT"

        class StartCash:
            Tag = 921
            Type = "AMT"

        class EndCash:
            Tag = 922
            Type = "AMT"

        class UserRequestID:
            Tag = 923
            Type = "STRING"

        class UserRequestType:
            Tag = 924
            Type = "INT"
            class Values:
                LOG_ON_USER = 1
                LOG_OFF_USER = 2
                CHANGE_PASSWORD_FOR_USER = 3
                REQUEST_INDIVIDUAL_USER_STATUS = 4

        class NewPassword:
            Tag = 925
            Type = "STRING"

        class UserStatus:
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

        class UserStatusText:
            Tag = 927
            Type = "STRING"

        class StatusValue:
            Tag = 928
            Type = "INT"
            class Values:
                CONNECTED = 1
                NOT_CONNECTED_2 = 2
                NOT_CONNECTED_3 = 3
                IN_PROCESS = 4

        class StatusText:
            Tag = 929
            Type = "STRING"

        class RefCompID:
            Tag = 930
            Type = "STRING"

        class RefSubID:
            Tag = 931
            Type = "STRING"

        class NetworkResponseID:
            Tag = 932
            Type = "STRING"

        class NetworkRequestID:
            Tag = 933
            Type = "STRING"

        class LastNetworkResponseID:
            Tag = 934
            Type = "STRING"

        class NetworkRequestType:
            Tag = 935
            Type = "INT"
            class Values:
                SNAPSHOT = 1
                SUBSCRIBE = 2
                STOP_SUBSCRIBING = 4
                LEVEL_OF_DETAIL_THEN_NOCOMPIDS_BECOMES_REQUIRED = 8

        class NoCompIDs:
            Tag = 936
            Type = "NUMINGROUP"

        class NetworkStatusResponseType:
            Tag = 937
            Type = "INT"
            class Values:
                FULL = 1
                INCREMENTAL_UPDATE = 2

        class NoCollInquiryQualifier:
            Tag = 938
            Type = "NUMINGROUP"

        class TrdRptStatus:
            Tag = 939
            Type = "INT"
            class Values:
                ACCEPTED = 0
                REJECTED = 1
                ACCEPTED_WITH_ERRORS = 3

        class AffirmStatus:
            Tag = 940
            Type = "INT"
            class Values:
                RECEIVED = 1
                CONFIRM_REJECTED_IE_NOT_AFFIRMED = 2
                AFFIRMED = 3

        class UnderlyingStrikeCurrency:
            Tag = 941
            Type = "CURRENCY"

        class LegStrikeCurrency:
            Tag = 942
            Type = "CURRENCY"

        class TimeBracket:
            Tag = 943
            Type = "STRING"

        class CollAction:
            Tag = 944
            Type = "INT"
            class Values:
                RETAIN = 0
                ADD = 1
                REMOVE = 2

        class CollInquiryStatus:
            Tag = 945
            Type = "INT"
            class Values:
                ACCEPTED = 0
                ACCEPTED_WITH_WARNINGS = 1
                COMPLETED = 2
                COMPLETED_WITH_WARNINGS = 3
                REJECTED = 4

        class CollInquiryResult:
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

        class StrikeCurrency:
            Tag = 947
            Type = "CURRENCY"

        class NoNested3PartyIDs:
            Tag = 948
            Type = "NUMINGROUP"

        class Nested3PartyID:
            Tag = 949
            Type = "STRING"

        class Nested3PartyIDSource:
            Tag = 950
            Type = "CHAR"

        class Nested3PartyRole:
            Tag = 951
            Type = "INT"

        class NoNested3PartySubIDs:
            Tag = 952
            Type = "NUMINGROUP"

        class Nested3PartySubID:
            Tag = 953
            Type = "STRING"

        class Nested3PartySubIDType:
            Tag = 954
            Type = "INT"

        class LegContractSettlMonth:
            Tag = 955
            Type = "MONTHYEAR"

        class LegInterestAccrualDate:
            Tag = 956
            Type = "LOCALMKTDATE"

        class NoStrategyParameters:
            Tag = 957
            Type = "NUMINGROUP"

        class StrategyParameterName:
            Tag = 958
            Type = "STRING"

        class StrategyParameterType:
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

        class StrategyParameterValue:
            Tag = 960
            Type = "STRING"

        class HostCrossID:
            Tag = 961
            Type = "STRING"

        class SideTimeInForce:
            Tag = 962
            Type = "UTCTIMESTAMP"

        class MDReportID:
            Tag = 963
            Type = "INT"

        class SecurityReportID:
            Tag = 964
            Type = "INT"

        class SecurityStatus:
            Tag = 965
            Type = "STRING"
            class Values:
                ACTIVE = "1"
                INACTIVE = "2"

        class SettleOnOpenFlag:
            Tag = 966
            Type = "STRING"

        class StrikeMultiplier:
            Tag = 967
            Type = "FLOAT"

        class StrikeValue:
            Tag = 968
            Type = "FLOAT"

        class MinPriceIncrement:
            Tag = 969
            Type = "FLOAT"

        class PositionLimit:
            Tag = 970
            Type = "INT"

        class NTPositionLimit:
            Tag = 971
            Type = "INT"

        class UnderlyingAllocationPercent:
            Tag = 972
            Type = "PERCENTAGE"

        class UnderlyingCashAmount:
            Tag = 973
            Type = "AMT"

        class UnderlyingCashType:
            Tag = 974
            Type = "STRING"
            class Values:
                FIXED = "FIXED"
                DIFF = "DIFF"

        class UnderlyingSettlementType:
            Tag = 975
            Type = "INT"
            class Values:
                T_PLUS_1 = 2
                T_PLUS_3 = 4
                T_PLUS_4 = 5

        class QuantityDate:
            Tag = 976
            Type = "LOCALMKTDATE"

        class ContIntRptID:
            Tag = 977
            Type = "STRING"

        class LateIndicator:
            Tag = 978
            Type = "BOOLEAN"

        class InputSource:
            Tag = 979
            Type = "STRING"

        class SecurityUpdateAction:
            Tag = 980
            Type = "CHAR"
            class Values:
                ADD = "A"
                DELETE = "D"
                MODIFY = "M"

        class NoExpiration:
            Tag = 981
            Type = "NUMINGROUP"

        class ExpirationQtyType:
            Tag = 982
            Type = "INT"
            class Values:
                AUTO_EXERCISE = 1
                NON_AUTO_EXERCISE = 2
                FINAL_WILL_BE_EXERCISED = 3
                CONTRARY_INTENTION = 4
                DIFFERENCE = 5

        class ExpQty:
            Tag = 983
            Type = "QTY"

        class NoUnderlyingAmounts:
            Tag = 984
            Type = "NUMINGROUP"

        class UnderlyingPayAmount:
            Tag = 985
            Type = "AMT"

        class UnderlyingCollectAmount:
            Tag = 986
            Type = "AMT"

        class UnderlyingSettlementDate:
            Tag = 987
            Type = "LOCALMKTDATE"

        class UnderlyingSettlementStatus:
            Tag = 988
            Type = "STRING"

        class SecondaryIndividualAllocID:
            Tag = 989
            Type = "STRING"

        class LegReportID:
            Tag = 990
            Type = "STRING"

        class RndPx:
            Tag = 991
            Type = "PRICE"

        class IndividualAllocType:
            Tag = 992
            Type = "INT"
            class Values:
                SUB_ALLOCATE = 1
                THIRD_PARTY_ALLOCATION = 2

        class AllocCustomerCapacity:
            Tag = 993
            Type = "STRING"

        class TierCode:
            Tag = 994
            Type = "STRING"

        class UnitOfMeasure:
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

        class TimeUnit:
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

        class UnderlyingUnitOfMeasure:
            Tag = 998
            Type = "STRING"

        class LegUnitOfMeasure:
            Tag = 999
            Type = "STRING"

        class UnderlyingTimeUnit:
            Tag = 1000
            Type = "STRING"

        class LegTimeUnit:
            Tag = 1001
            Type = "STRING"

        class AllocMethod:
            Tag = 1002
            Type = "INT"
            class Values:
                AUTOMATIC = 1
                GUARANTOR = 2
                MANUAL = 3

        class TradeID:
            Tag = 1003
            Type = "STRING"

        class SideTradeReportID:
            Tag = 1005
            Type = "STRING"

        class SideFillStationCd:
            Tag = 1006
            Type = "STRING"

        class SideReasonCd:
            Tag = 1007
            Type = "STRING"

        class SideTrdSubTyp:
            Tag = 1008
            Type = "INT"

        class SideLastQty:
            Tag = 1009
            Type = "INT"

        class MessageEventSource:
            Tag = 1011
            Type = "STRING"

        class SideTrdRegTimestamp:
            Tag = 1012
            Type = "UTCTIMESTAMP"

        class SideTrdRegTimestampType:
            Tag = 1013
            Type = "INT"

        class SideTrdRegTimestampSrc:
            Tag = 1014
            Type = "STRING"

        class AsOfIndicator:
            Tag = 1015
            Type = "CHAR"
            class Values:
                FALSE = "0"
                TRUE = "1"

        class NoSideTrdRegTS:
            Tag = 1016
            Type = "NUMINGROUP"

        class LegOptionRatio:
            Tag = 1017
            Type = "FLOAT"

        class NoInstrumentParties:
            Tag = 1018
            Type = "NUMINGROUP"

        class InstrumentPartyID:
            Tag = 1019
            Type = "STRING"

        class TradeVolume:
            Tag = 1020
            Type = "QTY"

        class MDBookType:
            Tag = 1021
            Type = "INT"
            class Values:
                TOP_OF_BOOK = 1
                PRICE_DEPTH = 2
                ORDER_DEPTH = 3

        class MDFeedType:
            Tag = 1022
            Type = "STRING"

        class MDPriceLevel:
            Tag = 1023
            Type = "INT"

        class MDOriginType:
            Tag = 1024
            Type = "INT"
            class Values:
                BOOK = 0
                OFF_BOOK = 1
                CROSS = 2

        class FirstPx:
            Tag = 1025
            Type = "PRICE"

        class MDEntrySpotRate:
            Tag = 1026
            Type = "FLOAT"

        class MDEntryForwardPoints:
            Tag = 1027
            Type = "PRICEOFFSET"

        class ManualOrderIndicator:
            Tag = 1028
            Type = "BOOLEAN"

        class CustDirectedOrder:
            Tag = 1029
            Type = "BOOLEAN"

        class ReceivedDeptID:
            Tag = 1030
            Type = "STRING"

        class CustOrderHandlingInst:
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

        class OrderHandlingInstSource:
            Tag = 1032
            Type = "INT"
            class Values:
                NASD_OATS = 1

        class DeskType:
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

        class DeskTypeSource:
            Tag = 1034
            Type = "INT"
            class Values:
                NASD_OATS = 1

        class DeskOrderHandlingInst:
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

        class ExecAckStatus:
            Tag = 1036
            Type = "CHAR"
            class Values:
                RECEIVED_NOT_YET_PROCESSED = "0"
                ACCEPTED = "1"
                DONT_KNOW = "2"

        class UnderlyingDeliveryAmount:
            Tag = 1037
            Type = "AMT"

        class UnderlyingCapValue:
            Tag = 1038
            Type = "AMT"

        class UnderlyingSettlMethod:
            Tag = 1039
            Type = "STRING"

        class SecondaryTradeID:
            Tag = 1040
            Type = "STRING"

        class FirmTradeID:
            Tag = 1041
            Type = "STRING"

        class SecondaryFirmTradeID:
            Tag = 1042
            Type = "STRING"

        class CollApplType:
            Tag = 1043
            Type = "INT"
            class Values:
                SPECIFIC_DEPOSIT = 0
                GENERAL = 1

        class UnderlyingAdjustedQuantity:
            Tag = 1044
            Type = "QTY"

        class UnderlyingFXRate:
            Tag = 1045
            Type = "FLOAT"

        class UnderlyingFXRateCalc:
            Tag = 1046
            Type = "CHAR"
            class Values:
                DIVIDE = "D"
                MULTIPLY = "M"

        class AllocPositionEffect:
            Tag = 1047
            Type = "CHAR"
            class Values:
                OPEN = "O"
                CLOSE = "C"
                ROLLED = "R"
                FIFO = "F"

        class DealingCapacity:
            Tag = 1048
            Type = "CHAR"
            class Values:
                AGENT = "A"
                PRINCIPAL = "P"
                RISKLESS_PRINCIPAL = "R"

        class InstrmtAssignmentMethod:
            Tag = 1049
            Type = "CHAR"
            class Values:
                PRO_RATA = "P"
                RANDOM = "R"

        class InstrumentPartyIDSource:
            Tag = 1050
            Type = "CHAR"

        class InstrumentPartyRole:
            Tag = 1051
            Type = "INT"

        class NoInstrumentPartySubIDs:
            Tag = 1052
            Type = "NUMINGROUP"

        class InstrumentPartySubID:
            Tag = 1053
            Type = "STRING"

        class InstrumentPartySubIDType:
            Tag = 1054
            Type = "INT"

        class PositionCurrency:
            Tag = 1055
            Type = "STRING"

        class CalculatedCcyLastQty:
            Tag = 1056
            Type = "QTY"

        class AggressorIndicator:
            Tag = 1057
            Type = "BOOLEAN"
            class Values:
                YES = 1
                NO = 0

        class NoUndlyInstrumentParties:
            Tag = 1058
            Type = "NUMINGROUP"

        class UnderlyingInstrumentPartyID:
            Tag = 1059
            Type = "STRING"

        class UnderlyingInstrumentPartyIDSource:
            Tag = 1060
            Type = "CHAR"

        class UnderlyingInstrumentPartyRole:
            Tag = 1061
            Type = "INT"

        class NoUndlyInstrumentPartySubIDs:
            Tag = 1062
            Type = "NUMINGROUP"

        class UnderlyingInstrumentPartySubID:
            Tag = 1063
            Type = "STRING"

        class UnderlyingInstrumentPartySubIDType:
            Tag = 1064
            Type = "INT"

        class BidSwapPoints:
            Tag = 1065
            Type = "PRICEOFFSET"

        class OfferSwapPoints:
            Tag = 1066
            Type = "PRICEOFFSET"

        class LegBidForwardPoints:
            Tag = 1067
            Type = "PRICEOFFSET"

        class LegOfferForwardPoints:
            Tag = 1068
            Type = "PRICEOFFSET"

        class SwapPoints:
            Tag = 1069
            Type = "PRICEOFFSET"

        class MDQuoteType:
            Tag = 1070
            Type = "INT"
            class Values:
                INDICATIVE = 0
                TRADEABLE = 1
                RESTRICTED_TRADEABLE = 2
                COUNTER = 3
                INDICATIVE_AND_TRADEABLE = 4

        class LastSwapPoints:
            Tag = 1071
            Type = "PRICEOFFSET"

        class SideGrossTradeAmt:
            Tag = 1072
            Type = "AMT"

        class LegLastForwardPoints:
            Tag = 1073
            Type = "PRICEOFFSET"

        class LegCalculatedCcyLastQty:
            Tag = 1074
            Type = "QTY"

        class LegGrossTradeAmt:
            Tag = 1075
            Type = "AMT"

        class MaturityTime:
            Tag = 1079
            Type = "TZTIMEONLY"

        class RefOrderID:
            Tag = 1080
            Type = "STRING"

        class RefOrderIDSource:
            Tag = 1081
            Type = "CHAR"
            class Values:
                SECONDARYORDERID = "0"
                ORDERID = "1"
                MDENTRYID = "2"
                QUOTEENTRYID = "3"
                ORIGINAL_ORDER_ID = "4"

        class SecondaryDisplayQty:
            Tag = 1082
            Type = "QTY"

        class DisplayWhen:
            Tag = 1083
            Type = "CHAR"
            class Values:
                IMMEDIATE = "1"
                EXHAUST = "2"

        class DisplayMethod:
            Tag = 1084
            Type = "CHAR"
            class Values:
                INITIAL = "1"
                NEW = "2"
                RANDOM = "3"
                UNDISCLOSED = "4"

        class DisplayLowQty:
            Tag = 1085
            Type = "QTY"

        class DisplayHighQty:
            Tag = 1086
            Type = "QTY"

        class DisplayMinIncr:
            Tag = 1087
            Type = "QTY"

        class RefreshQty:
            Tag = 1088
            Type = "QTY"

        class MatchIncrement:
            Tag = 1089
            Type = "QTY"

        class MaxPriceLevels:
            Tag = 1090
            Type = "INT"

        class PreTradeAnonymity:
            Tag = 1091
            Type = "BOOLEAN"

        class PriceProtectionScope:
            Tag = 1092
            Type = "CHAR"
            class Values:
                NONE = "0"
                LOCAL = "1"
                NATIONAL = "2"
                GLOBAL = "3"

        class LotType:
            Tag = 1093
            Type = "CHAR"
            class Values:
                ODD_LOT = "1"
                ROUND_LOT = "2"
                BLOCK_LOT = "3"
                ROUND_LOT_BASED_UPON_UNITOFMEASURE = "4"

        class PegPriceType:
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

        class PeggedRefPrice:
            Tag = 1095
            Type = "PRICE"

        class PegSecurityIDSource:
            Tag = 1096
            Type = "STRING"

        class PegSecurityID:
            Tag = 1097
            Type = "STRING"

        class PegSymbol:
            Tag = 1098
            Type = "STRING"

        class PegSecurityDesc:
            Tag = 1099
            Type = "STRING"

        class TriggerType:
            Tag = 1100
            Type = "CHAR"
            class Values:
                PARTIAL_EXECUTION = "1"
                SPECIFIED_TRADING_SESSION = "2"
                NEXT_AUCTION = "3"
                PRICE_MOVEMENT = "4"

        class TriggerAction:
            Tag = 1101
            Type = "CHAR"
            class Values:
                ACTIVATE = "1"
                MODIFY = "2"
                CANCEL = "3"

        class TriggerPrice:
            Tag = 1102
            Type = "PRICE"

        class TriggerSymbol:
            Tag = 1103
            Type = "STRING"

        class TriggerSecurityID:
            Tag = 1104
            Type = "STRING"

        class TriggerSecurityIDSource:
            Tag = 1105
            Type = "STRING"

        class TriggerSecurityDesc:
            Tag = 1106
            Type = "STRING"

        class TriggerPriceType:
            Tag = 1107
            Type = "CHAR"
            class Values:
                BEST_OFFER = "1"
                LAST_TRADE = "2"
                BEST_BID = "3"
                BEST_BID_OR_LAST_TRADE = "4"
                BEST_OFFER_OR_LAST_TRADE = "5"
                BEST_MID = "6"

        class TriggerPriceTypeScope:
            Tag = 1108
            Type = "CHAR"
            class Values:
                NONE = "0"
                LOCAL = "1"
                NATIONAL = "2"
                GLOBAL = "3"

        class TriggerPriceDirection:
            Tag = 1109
            Type = "CHAR"
            class Values:
                TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_UP_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE = "U"
                TRIGGER_IF_THE_PRICE_OF_THE_SPECIFIED_TYPE_GOES_DOWN_TO_OR_THROUGH_THE_SPECIFIED_TRIGGER_PRICE = "D"

        class TriggerNewPrice:
            Tag = 1110
            Type = "PRICE"

        class TriggerOrderType:
            Tag = 1111
            Type = "CHAR"
            class Values:
                MARKET = "1"
                LIMIT = "2"

        class TriggerNewQty:
            Tag = 1112
            Type = "QTY"

        class TriggerTradingSessionID:
            Tag = 1113
            Type = "STRING"

        class TriggerTradingSessionSubID:
            Tag = 1114
            Type = "STRING"

        class OrderCategory:
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

        class NoRootPartyIDs:
            Tag = 1116
            Type = "NUMINGROUP"

        class RootPartyID:
            Tag = 1117
            Type = "STRING"

        class RootPartyIDSource:
            Tag = 1118
            Type = "CHAR"

        class RootPartyRole:
            Tag = 1119
            Type = "INT"

        class NoRootPartySubIDs:
            Tag = 1120
            Type = "NUMINGROUP"

        class RootPartySubID:
            Tag = 1121
            Type = "STRING"

        class RootPartySubIDType:
            Tag = 1122
            Type = "INT"

        class TradeHandlingInstr:
            Tag = 1123
            Type = "CHAR"
            class Values:
                TRADE_CONFIRMATION = "0"
                TWO_PARTY_REPORT = "1"
                ONE_PARTY_REPORT_FOR_MATCHING = "2"
                ONE_PARTY_REPORT_FOR_PASS_THROUGH = "3"
                AUTOMATED_FLOOR_ORDER_ROUTING = "4"
                TWO_PARTY_REPORT_FOR_CLAIM = "5"

        class OrigTradeHandlingInstr:
            Tag = 1124
            Type = "CHAR"

        class OrigTradeDate:
            Tag = 1125
            Type = "LOCALMKTDATE"

        class OrigTradeID:
            Tag = 1126
            Type = "STRING"

        class OrigSecondaryTradeID:
            Tag = 1127
            Type = "STRING"

        class ApplVerID:
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

        class CstmApplVerID:
            Tag = 1129
            Type = "STRING"

        class RefApplVerID:
            Tag = 1130
            Type = "STRING"

        class RefCstmApplVerID:
            Tag = 1131
            Type = "STRING"

        class TZTransactTime:
            Tag = 1132
            Type = "TZTIMESTAMP"

        class ExDestinationIDSource:
            Tag = 1133
            Type = "CHAR"
            class Values:
                BIC = "B"
                GENERALLY_ACCEPTED_MARKET_PARTICIPANT_IDENTIFIER = "C"
                PROPRIETARY = "D"
                ISO_COUNTRY_CODE = "E"
                MIC = "G"

        class ReportedPxDiff:
            Tag = 1134
            Type = "BOOLEAN"

        class RptSys:
            Tag = 1135
            Type = "STRING"

        class AllocClearingFeeIndicator:
            Tag = 1136
            Type = "STRING"

        class DefaultApplVerID:
            Tag = 1137
            Type = "STRING"

        class DisplayQty:
            Tag = 1138
            Type = "QTY"

        class ExchangeSpecialInstructions:
            Tag = 1139
            Type = "STRING"

        class MaxTradeVol:
            Tag = 1140
            Type = "QTY"

        class NoMDFeedTypes:
            Tag = 1141
            Type = "NUMINGROUP"

        class MatchAlgorithm:
            Tag = 1142
            Type = "STRING"

        class MaxPriceVariation:
            Tag = 1143
            Type = "FLOAT"

        class ImpliedMarketIndicator:
            Tag = 1144
            Type = "INT"
            class Values:
                NOT_IMPLIED = 0
                IMPLIED_IN = 1
                IMPLIED_OUT = 2
                BOTH_IMPLIED_IN_AND_IMPLIED_OUT = 3

        class EventTime:
            Tag = 1145
            Type = "UTCTIMESTAMP"

        class MinPriceIncrementAmount:
            Tag = 1146
            Type = "AMT"

        class UnitOfMeasureQty:
            Tag = 1147
            Type = "QTY"

        class LowLimitPrice:
            Tag = 1148
            Type = "PRICE"

        class HighLimitPrice:
            Tag = 1149
            Type = "PRICE"

        class TradingReferencePrice:
            Tag = 1150
            Type = "PRICE"

        class SecurityGroup:
            Tag = 1151
            Type = "STRING"

        class LegNumber:
            Tag = 1152
            Type = "INT"

        class SettlementCycleNo:
            Tag = 1153
            Type = "INT"

        class SideCurrency:
            Tag = 1154
            Type = "CURRENCY"

        class SideSettlCurrency:
            Tag = 1155
            Type = "CURRENCY"

        class ApplExtID:
            Tag = 1156
            Type = "INT"

        class CcyAmt:
            Tag = 1157
            Type = "AMT"

        class NoSettlDetails:
            Tag = 1158
            Type = "NUMINGROUP"

        class SettlObligMode:
            Tag = 1159
            Type = "INT"
            class Values:
                PRELIMINARY = 1
                FINAL = 2

        class SettlObligMsgID:
            Tag = 1160
            Type = "STRING"

        class SettlObligID:
            Tag = 1161
            Type = "STRING"

        class SettlObligTransType:
            Tag = 1162
            Type = "CHAR"
            class Values:
                CANCEL = "C"
                NEW = "N"
                REPLACE = "R"
                RESTATE = "T"

        class SettlObligRefID:
            Tag = 1163
            Type = "STRING"

        class SettlObligSource:
            Tag = 1164
            Type = "CHAR"
            class Values:
                INSTRUCTIONS_OF_BROKER = "1"
                INSTRUCTIONS_FOR_INSTITUTION = "2"
                INVESTOR = "3"

        class NoSettlOblig:
            Tag = 1165
            Type = "NUMINGROUP"

        class QuoteMsgID:
            Tag = 1166
            Type = "STRING"

        class QuoteEntryStatus:
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

        class TotNoCxldQuotes:
            Tag = 1168
            Type = "INT"

        class TotNoAccQuotes:
            Tag = 1169
            Type = "INT"

        class TotNoRejQuotes:
            Tag = 1170
            Type = "INT"

        class PrivateQuote:
            Tag = 1171
            Type = "BOOLEAN"
            class Values:
                YES = 1
                NO = 0

        class RespondentType:
            Tag = 1172
            Type = "INT"
            class Values:
                ALL_MARKET_PARTICIPANTS = 1
                SPECIFIED_MARKET_PARTICIPANTS = 2
                ALL_MARKET_MAKERS = 3
                PRIMARY_MARKET_MAKER = 4

        class MDSubBookType:
            Tag = 1173
            Type = "INT"

        class SecurityTradingEvent:
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

        class NoStatsIndicators:
            Tag = 1175
            Type = "NUMINGROUP"

        class StatsType:
            Tag = 1176
            Type = "INT"
            class Values:
                EXCHANGE_LAST = 1
                HIGH = 2
                AVERAGE_PRICE = 3
                TURNOVER = 4

        class NoOfSecSizes:
            Tag = 1177
            Type = "NUMINGROUP"

        class MDSecSizeType:
            Tag = 1178
            Type = "INT"
            class Values:
                CUSTOMER = 1

        class MDSecSize:
            Tag = 1179
            Type = "QTY"

        class ApplID:
            Tag = 1180
            Type = "STRING"

        class ApplSeqNum:
            Tag = 1181
            Type = "SEQNUM"

        class ApplBegSeqNum:
            Tag = 1182
            Type = "SEQNUM"

        class ApplEndSeqNum:
            Tag = 1183
            Type = "SEQNUM"

        class SecurityXMLLen:
            Tag = 1184
            Type = "LENGTH"

        class SecurityXML:
            Tag = 1185
            Type = "XMLDATA"

        class SecurityXMLSchema:
            Tag = 1186
            Type = "STRING"

        class RefreshIndicator:
            Tag = 1187
            Type = "BOOLEAN"

        class Volatility:
            Tag = 1188
            Type = "FLOAT"

        class TimeToExpiration:
            Tag = 1189
            Type = "FLOAT"

        class RiskFreeRate:
            Tag = 1190
            Type = "FLOAT"

        class PriceUnitOfMeasure:
            Tag = 1191
            Type = "STRING"

        class PriceUnitOfMeasureQty:
            Tag = 1192
            Type = "QTY"

        class SettlMethod:
            Tag = 1193
            Type = "CHAR"
            class Values:
                CASH_SETTLEMENT_REQUIRED = "C"
                PHYSICAL_SETTLEMENT_REQUIRED = "P"

        class ExerciseStyle:
            Tag = 1194
            Type = "INT"
            class Values:
                EUROPEAN = 0
                AMERICAN = 1
                BERMUDA = 2

        class OptPayoutAmount:
            Tag = 1195
            Type = "AMT"

        class PriceQuoteMethod:
            Tag = 1196
            Type = "STRING"
            class Values:
                STANDARD_MONEY_PER_UNIT_OF_A_PHYSICAL = "STD"
                INDEX = "INX"
                INTEREST_RATE_INDEX = "INT"
                PERCENT_OF_PAR = "PCTPAR"

        class ValuationMethod:
            Tag = 1197
            Type = "STRING"
            class Values:
                PREMIUM_STYLE = "EQTY"
                FUTURES_STYLE_MARK_TO_MARKET = "FUT"
                FUTURES_STYLE_WITH_AN_ATTACHED_CASH_ADJUSTMENT = "FUTDA"
                CDS_STYLE_COLLATERALIZATION_OF_MARKET_TO_MARKET_AND_COUPON = "CDS"
                CDS_IN_DELIVERY = "CDSD"

        class ListMethod:
            Tag = 1198
            Type = "INT"
            class Values:
                PRE_LISTED_ONLY = 0
                USER_REQUESTED = 1

        class CapPrice:
            Tag = 1199
            Type = "PRICE"

        class FloorPrice:
            Tag = 1200
            Type = "PRICE"

        class NoStrikeRules:
            Tag = 1201
            Type = "NUMINGROUP"

        class StartStrikePxRange:
            Tag = 1202
            Type = "PRICE"

        class EndStrikePxRange:
            Tag = 1203
            Type = "PRICE"

        class StrikeIncrement:
            Tag = 1204
            Type = "FLOAT"

        class NoTickRules:
            Tag = 1205
            Type = "NUMINGROUP"

        class StartTickPriceRange:
            Tag = 1206
            Type = "PRICE"

        class EndTickPriceRange:
            Tag = 1207
            Type = "PRICE"

        class TickIncrement:
            Tag = 1208
            Type = "PRICE"

        class TickRuleType:
            Tag = 1209
            Type = "INT"
            class Values:
                REGULAR = 0
                VARIABLE = 1
                FIXED = 2
                TRADED_AS_A_SPREAD_LEG = 3
                SETTLED_AS_A_SPREAD_LEG = 4

        class NestedInstrAttribType:
            Tag = 1210
            Type = "INT"

        class NestedInstrAttribValue:
            Tag = 1211
            Type = "STRING"

        class LegMaturityTime:
            Tag = 1212
            Type = "TZTIMEONLY"

        class UnderlyingMaturityTime:
            Tag = 1213
            Type = "TZTIMEONLY"

        class DerivativeSymbol:
            Tag = 1214
            Type = "STRING"

        class DerivativeSymbolSfx:
            Tag = 1215
            Type = "STRING"

        class DerivativeSecurityID:
            Tag = 1216
            Type = "STRING"

        class DerivativeSecurityIDSource:
            Tag = 1217
            Type = "STRING"

        class NoDerivativeSecurityAltID:
            Tag = 1218
            Type = "NUMINGROUP"

        class DerivativeSecurityAltID:
            Tag = 1219
            Type = "STRING"

        class DerivativeSecurityAltIDSource:
            Tag = 1220
            Type = "STRING"

        class SecondaryLowLimitPrice:
            Tag = 1221
            Type = "PRICE"

        class MaturityRuleID:
            Tag = 1222
            Type = "STRING"

        class StrikeRuleID:
            Tag = 1223
            Type = "STRING"

        class LegUnitOfMeasureQty:
            Tag = 1224
            Type = "QTY"

        class DerivativeOptPayAmount:
            Tag = 1225
            Type = "AMT"

        class EndMaturityMonthYear:
            Tag = 1226
            Type = "MONTHYEAR"

        class ProductComplex:
            Tag = 1227
            Type = "STRING"

        class DerivativeProductComplex:
            Tag = 1228
            Type = "STRING"

        class MaturityMonthYearIncrement:
            Tag = 1229
            Type = "INT"

        class SecondaryHighLimitPrice:
            Tag = 1230
            Type = "PRICE"

        class MinLotSize:
            Tag = 1231
            Type = "QTY"

        class NoExecInstRules:
            Tag = 1232
            Type = "NUMINGROUP"

        class NoLotTypeRules:
            Tag = 1234
            Type = "NUMINGROUP"

        class NoMatchRules:
            Tag = 1235
            Type = "NUMINGROUP"

        class NoMaturityRules:
            Tag = 1236
            Type = "NUMINGROUP"

        class NoOrdTypeRules:
            Tag = 1237
            Type = "NUMINGROUP"

        class NoTimeInForceRules:
            Tag = 1239
            Type = "NUMINGROUP"

        class SecondaryTradingReferencePrice:
            Tag = 1240
            Type = "PRICE"

        class StartMaturityMonthYear:
            Tag = 1241
            Type = "MONTHYEAR"

        class FlexProductEligibilityIndicator:
            Tag = 1242
            Type = "BOOLEAN"

        class DerivFlexProductEligibilityIndicator:
            Tag = 1243
            Type = "BOOLEAN"

        class FlexibleIndicator:
            Tag = 1244
            Type = "BOOLEAN"

        class TradingCurrency:
            Tag = 1245
            Type = "CURRENCY"

        class DerivativeProduct:
            Tag = 1246
            Type = "INT"

        class DerivativeSecurityGroup:
            Tag = 1247
            Type = "STRING"

        class DerivativeCFICode:
            Tag = 1248
            Type = "STRING"

        class DerivativeSecurityType:
            Tag = 1249
            Type = "STRING"

        class DerivativeSecuritySubType:
            Tag = 1250
            Type = "STRING"

        class DerivativeMaturityMonthYear:
            Tag = 1251
            Type = "MONTHYEAR"

        class DerivativeMaturityDate:
            Tag = 1252
            Type = "LOCALMKTDATE"

        class DerivativeMaturityTime:
            Tag = 1253
            Type = "TZTIMEONLY"

        class DerivativeSettleOnOpenFlag:
            Tag = 1254
            Type = "STRING"

        class DerivativeInstrmtAssignmentMethod:
            Tag = 1255
            Type = "CHAR"

        class DerivativeSecurityStatus:
            Tag = 1256
            Type = "STRING"

        class DerivativeInstrRegistry:
            Tag = 1257
            Type = "STRING"

        class DerivativeCountryOfIssue:
            Tag = 1258
            Type = "COUNTRY"

        class DerivativeStateOrProvinceOfIssue:
            Tag = 1259
            Type = "STRING"

        class DerivativeLocaleOfIssue:
            Tag = 1260
            Type = "STRING"

        class DerivativeStrikePrice:
            Tag = 1261
            Type = "PRICE"

        class DerivativeStrikeCurrency:
            Tag = 1262
            Type = "CURRENCY"

        class DerivativeStrikeMultiplier:
            Tag = 1263
            Type = "FLOAT"

        class DerivativeStrikeValue:
            Tag = 1264
            Type = "FLOAT"

        class DerivativeOptAttribute:
            Tag = 1265
            Type = "CHAR"

        class DerivativeContractMultiplier:
            Tag = 1266
            Type = "FLOAT"

        class DerivativeMinPriceIncrement:
            Tag = 1267
            Type = "FLOAT"

        class DerivativeMinPriceIncrementAmount:
            Tag = 1268
            Type = "AMT"

        class DerivativeUnitOfMeasure:
            Tag = 1269
            Type = "STRING"

        class DerivativeUnitOfMeasureQty:
            Tag = 1270
            Type = "QTY"

        class DerivativeTimeUnit:
            Tag = 1271
            Type = "STRING"

        class DerivativeSecurityExchange:
            Tag = 1272
            Type = "EXCHANGE"

        class DerivativePositionLimit:
            Tag = 1273
            Type = "INT"

        class DerivativeNTPositionLimit:
            Tag = 1274
            Type = "INT"

        class DerivativeIssuer:
            Tag = 1275
            Type = "STRING"

        class DerivativeIssueDate:
            Tag = 1276
            Type = "LOCALMKTDATE"

        class DerivativeEncodedIssuerLen:
            Tag = 1277
            Type = "LENGTH"

        class DerivativeEncodedIssuer:
            Tag = 1278
            Type = "DATA"

        class DerivativeSecurityDesc:
            Tag = 1279
            Type = "STRING"

        class DerivativeEncodedSecurityDescLen:
            Tag = 1280
            Type = "LENGTH"

        class DerivativeEncodedSecurityDesc:
            Tag = 1281
            Type = "DATA"

        class DerivativeSecurityXMLLen:
            Tag = 1282
            Type = "LENGTH"

        class DerivativeSecurityXML:
            Tag = 1283
            Type = "DATA"

        class DerivativeSecurityXMLSchema:
            Tag = 1284
            Type = "STRING"

        class DerivativeContractSettlMonth:
            Tag = 1285
            Type = "MONTHYEAR"

        class NoDerivativeEvents:
            Tag = 1286
            Type = "NUMINGROUP"

        class DerivativeEventType:
            Tag = 1287
            Type = "INT"

        class DerivativeEventDate:
            Tag = 1288
            Type = "LOCALMKTDATE"

        class DerivativeEventTime:
            Tag = 1289
            Type = "UTCTIMESTAMP"

        class DerivativeEventPx:
            Tag = 1290
            Type = "PRICE"

        class DerivativeEventText:
            Tag = 1291
            Type = "STRING"

        class NoDerivativeInstrumentParties:
            Tag = 1292
            Type = "NUMINGROUP"

        class DerivativeInstrumentPartyID:
            Tag = 1293
            Type = "STRING"

        class DerivativeInstrumentPartyIDSource:
            Tag = 1294
            Type = "STRING"

        class DerivativeInstrumentPartyRole:
            Tag = 1295
            Type = "INT"

        class NoDerivativeInstrumentPartySubIDs:
            Tag = 1296
            Type = "NUMINGROUP"

        class DerivativeInstrumentPartySubID:
            Tag = 1297
            Type = "STRING"

        class DerivativeInstrumentPartySubIDType:
            Tag = 1298
            Type = "INT"

        class DerivativeExerciseStyle:
            Tag = 1299
            Type = "CHAR"

        class MarketSegmentID:
            Tag = 1300
            Type = "STRING"

        class MarketID:
            Tag = 1301
            Type = "EXCHANGE"

        class MaturityMonthYearIncrementUnits:
            Tag = 1302
            Type = "INT"
            class Values:
                MONTHS = 0
                DAYS = 1
                WEEKS = 2
                YEARS = 3

        class MaturityMonthYearFormat:
            Tag = 1303
            Type = "INT"
            class Values:
                YEARMONTH_ONLY = 0
                YEARMONTHDAY = 1
                YEARMONTHWEEK = 2

        class StrikeExerciseStyle:
            Tag = 1304
            Type = "INT"

        class SecondaryPriceLimitType:
            Tag = 1305
            Type = "INT"

        class PriceLimitType:
            Tag = 1306
            Type = "INT"
            class Values:
                PRICE = 0
                TICKS = 1
                PERCENTAGE = 2

        class ExecInstValue:
            Tag = 1308
            Type = "CHAR"

        class NoTradingSessionRules:
            Tag = 1309
            Type = "NUMINGROUP"

        class NoMarketSegments:
            Tag = 1310
            Type = "NUMINGROUP"

        class NoDerivativeInstrAttrib:
            Tag = 1311
            Type = "NUMINGROUP"

        class NoNestedInstrAttrib:
            Tag = 1312
            Type = "NUMINGROUP"

        class DerivativeInstrAttribType:
            Tag = 1313
            Type = "INT"

        class DerivativeInstrAttribValue:
            Tag = 1314
            Type = "STRING"

        class DerivativePriceUnitOfMeasure:
            Tag = 1315
            Type = "STRING"

        class DerivativePriceUnitOfMeasureQty:
            Tag = 1316
            Type = "QTY"

        class DerivativeSettlMethod:
            Tag = 1317
            Type = "CHAR"

        class DerivativePriceQuoteMethod:
            Tag = 1318
            Type = "STRING"

        class DerivativeValuationMethod:
            Tag = 1319
            Type = "STRING"

        class DerivativeListMethod:
            Tag = 1320
            Type = "INT"

        class DerivativeCapPrice:
            Tag = 1321
            Type = "PRICE"

        class DerivativeFloorPrice:
            Tag = 1322
            Type = "PRICE"

        class DerivativePutOrCall:
            Tag = 1323
            Type = "INT"

        class ListUpdateAction:
            Tag = 1324
            Type = "CHAR"

        class ParentMktSegmID:
            Tag = 1325
            Type = "STRING"

        class TradingSessionDesc:
            Tag = 1326
            Type = "STRING"

        class TradSesUpdateAction:
            Tag = 1327
            Type = "CHAR"

        class RejectText:
            Tag = 1328
            Type = "STRING"

        class FeeMultiplier:
            Tag = 1329
            Type = "FLOAT"

        class UnderlyingLegSymbol:
            Tag = 1330
            Type = "STRING"

        class UnderlyingLegSymbolSfx:
            Tag = 1331
            Type = "STRING"

        class UnderlyingLegSecurityID:
            Tag = 1332
            Type = "STRING"

        class UnderlyingLegSecurityIDSource:
            Tag = 1333
            Type = "STRING"

        class NoUnderlyingLegSecurityAltID:
            Tag = 1334
            Type = "NUMINGROUP"

        class UnderlyingLegSecurityAltID:
            Tag = 1335
            Type = "STRING"

        class UnderlyingLegSecurityAltIDSource:
            Tag = 1336
            Type = "STRING"

        class UnderlyingLegSecurityType:
            Tag = 1337
            Type = "STRING"

        class UnderlyingLegSecuritySubType:
            Tag = 1338
            Type = "STRING"

        class UnderlyingLegMaturityMonthYear:
            Tag = 1339
            Type = "MONTHYEAR"

        class UnderlyingLegStrikePrice:
            Tag = 1340
            Type = "PRICE"

        class UnderlyingLegSecurityExchange:
            Tag = 1341
            Type = "STRING"

        class NoOfLegUnderlyings:
            Tag = 1342
            Type = "NUMINGROUP"

        class UnderlyingLegPutOrCall:
            Tag = 1343
            Type = "INT"

        class UnderlyingLegCFICode:
            Tag = 1344
            Type = "STRING"

        class UnderlyingLegMaturityDate:
            Tag = 1345
            Type = "LOCALMKTDATE"

        class ApplReqID:
            Tag = 1346
            Type = "STRING"

        class ApplReqType:
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

        class ApplResponseType:
            Tag = 1348
            Type = "INT"
            class Values:
                REQUEST_SUCCESSFULLY_PROCESSED = 0
                APPLICATION_DOES_NOT_EXIST = 1
                MESSAGES_NOT_AVAILABLE = 2

        class ApplTotalMessageCount:
            Tag = 1349
            Type = "INT"

        class ApplLastSeqNum:
            Tag = 1350
            Type = "SEQNUM"

        class NoApplIDs:
            Tag = 1351
            Type = "NUMINGROUP"

        class ApplResendFlag:
            Tag = 1352
            Type = "BOOLEAN"

        class ApplResponseID:
            Tag = 1353
            Type = "STRING"

        class ApplResponseError:
            Tag = 1354
            Type = "INT"
            class Values:
                APPLICATION_DOES_NOT_EXIST = 0
                MESSAGES_REQUESTED_ARE_NOT_AVAILABLE = 1
                USER_NOT_AUTHORIZED_FOR_APPLICATION = 2

        class RefApplID:
            Tag = 1355
            Type = "STRING"

        class ApplReportID:
            Tag = 1356
            Type = "STRING"

        class RefApplLastSeqNum:
            Tag = 1357
            Type = "SEQNUM"

        class LegPutOrCall:
            Tag = 1358
            Type = "INT"

        class TotNoFills:
            Tag = 1361
            Type = "INT"

        class NoFills:
            Tag = 1362
            Type = "NUMINGROUP"

        class FillExecID:
            Tag = 1363
            Type = "STRING"

        class FillPx:
            Tag = 1364
            Type = "PRICE"

        class FillQty:
            Tag = 1365
            Type = "QTY"

        class LegAllocID:
            Tag = 1366
            Type = "STRING"

        class LegAllocSettlCurrency:
            Tag = 1367
            Type = "CURRENCY"

        class TradSesEvent:
            Tag = 1368
            Type = "INT"
            class Values:
                TRADING_RESUMES = 0
                CHANGE_OF_TRADING_SESSION = 1
                CHANGE_OF_TRADING_SUBSESSION = 2
                CHANGE_OF_TRADING_STATUS = 3

        class MassActionReportID:
            Tag = 1369
            Type = "STRING"

        class NoNotAffectedOrders:
            Tag = 1370
            Type = "NUMINGROUP"

        class NotAffectedOrderID:
            Tag = 1371
            Type = "STRING"

        class NotAffOrigClOrdID:
            Tag = 1372
            Type = "STRING"

        class MassActionType:
            Tag = 1373
            Type = "INT"
            class Values:
                SUSPEND_ORDERS = 1
                RELEASE_ORDERS_FROM_SUSPENSION = 2
                CANCEL_ORDERS = 3

        class MassActionScope:
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

        class MassActionResponse:
            Tag = 1375
            Type = "INT"
            class Values:
                REJECTED = 0
                ACCEPTED = 1

        class MassActionRejectReason:
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

        class MultilegModel:
            Tag = 1377
            Type = "INT"
            class Values:
                PREDEFINED_MULTILEG_SECURITY = 0
                USER_DEFINED_MULTLEG_SECURITY = 1
                USER_DEFINED_NON_SECURITIZED_MULTILEG = 2

        class MultilegPriceMethod:
            Tag = 1378
            Type = "INT"
            class Values:
                NET_PRICE = 0
                REVERSED_NET_PRICE = 1
                YIELD_DIFFERENCE = 2
                INDIVIDUAL = 3
                CONTRACT_WEIGHTED_AVERAGE_PRICE = 4
                MULTIPLIED_PRICE = 5

        class LegVolatility:
            Tag = 1379
            Type = "FLOAT"

        class DividendYield:
            Tag = 1380
            Type = "PERCENTAGE"

        class LegDividendYield:
            Tag = 1381
            Type = "PERCENTAGE"

        class CurrencyRatio:
            Tag = 1382
            Type = "FLOAT"

        class LegCurrencyRatio:
            Tag = 1383
            Type = "FLOAT"

        class LegExecInst:
            Tag = 1384
            Type = "MULTIPLECHARVALUE"

        class ContingencyType:
            Tag = 1385
            Type = "INT"
            class Values:
                ONE_CANCELS_THE_OTHER = 1
                ONE_TRIGGERS_THE_OTHER = 2
                ONE_UPDATES_THE_OTHER_3 = 3
                ONE_UPDATES_THE_OTHER_4 = 4

        class ListRejectReason:
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

        class NoTrdRepIndicators:
            Tag = 1387
            Type = "NUMINGROUP"

        class TrdRepPartyRole:
            Tag = 1388
            Type = "INT"

        class TrdRepIndicator:
            Tag = 1389
            Type = "BOOLEAN"

        class TradePublishIndicator:
            Tag = 1390
            Type = "INT"
            class Values:
                DO_NOT_PUBLISH_TRADE = 0
                PUBLISH_TRADE = 1
                DEFERRED_PUBLICATION = 2

        class UnderlyingLegOptAttribute:
            Tag = 1391
            Type = "CHAR"

        class UnderlyingLegSecurityDesc:
            Tag = 1392
            Type = "STRING"

        class MarketReqID:
            Tag = 1393
            Type = "STRING"

        class MarketReportID:
            Tag = 1394
            Type = "STRING"

        class MarketUpdateAction:
            Tag = 1395
            Type = "CHAR"
            class Values:
                ADD = "A"
                DELETE = "D"
                MODIFY = "M"

        class MarketSegmentDesc:
            Tag = 1396
            Type = "STRING"

        class EncodedMktSegmDescLen:
            Tag = 1397
            Type = "LENGTH"

        class EncodedMktSegmDesc:
            Tag = 1398
            Type = "DATA"

        class ApplNewSeqNum:
            Tag = 1399
            Type = "SEQNUM"

        class EncryptedPasswordMethod:
            Tag = 1400
            Type = "INT"

        class EncryptedPasswordLen:
            Tag = 1401
            Type = "LENGTH"

        class EncryptedPassword:
            Tag = 1402
            Type = "DATA"

        class EncryptedNewPasswordLen:
            Tag = 1403
            Type = "LENGTH"

        class EncryptedNewPassword:
            Tag = 1404
            Type = "DATA"

        class UnderlyingLegMaturityTime:
            Tag = 1405
            Type = "TZTIMEONLY"

        class RefApplExtID:
            Tag = 1406
            Type = "INT"

        class DefaultApplExtID:
            Tag = 1407
            Type = "INT"

        class DefaultCstmApplVerID:
            Tag = 1408
            Type = "STRING"

        class SessionStatus:
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

        class DefaultVerIndicator:
            Tag = 1410
            Type = "BOOLEAN"

        class Nested4PartySubIDType:
            Tag = 1411
            Type = "INT"

        class Nested4PartySubID:
            Tag = 1412
            Type = "STRING"

        class NoNested4PartySubIDs:
            Tag = 1413
            Type = "NUMINGROUP"

        class NoNested4PartyIDs:
            Tag = 1414
            Type = "NUMINGROUP"

        class Nested4PartyID:
            Tag = 1415
            Type = "STRING"

        class Nested4PartyIDSource:
            Tag = 1416
            Type = "CHAR"

        class Nested4PartyRole:
            Tag = 1417
            Type = "INT"

        class LegLastQty:
            Tag = 1418
            Type = "QTY"

        class UnderlyingExerciseStyle:
            Tag = 1419
            Type = "INT"

        class LegExerciseStyle:
            Tag = 1420
            Type = "INT"

        class LegPriceUnitOfMeasure:
            Tag = 1421
            Type = "STRING"

        class LegPriceUnitOfMeasureQty:
            Tag = 1422
            Type = "QTY"

        class UnderlyingUnitOfMeasureQty:
            Tag = 1423
            Type = "QTY"

        class UnderlyingPriceUnitOfMeasure:
            Tag = 1424
            Type = "STRING"

        class UnderlyingPriceUnitOfMeasureQty:
            Tag = 1425
            Type = "QTY"

        class ApplReportType:
            Tag = 1426
            Type = "INT"
            class Values:
                RESET_APPLSEQNUM_TO_NEW_VALUE_SPECIFIED_IN_APPLNEWSEQNUM = 0
                REPORTS_THAT_THE_LAST_MESSAGE_HAS_BEEN_SENT_FOR_THE_APPLIDS_REFER_TO_REFAPPLLASTSEQNUM = 1
                HEARTBEAT_MESSAGE_INDICATING_THAT_APPLICATION_IDENTIFIED_BY_REFAPPLID = 2
                APPLICATION_MESSAGE_RE_SEND_COMPLETED = 3

        class SideExecID:
            Tag = 1427
            Type = "STRING"

        class OrderDelay:
            Tag = 1428
            Type = "INT"

        class OrderDelayUnit:
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

        class VenueType:
            Tag = 1430
            Type = "CHAR"
            class Values:
                ELECTRONIC = "E"
                PIT = "P"
                EX_PIT = "X"

        class RefOrdIDReason:
            Tag = 1431
            Type = "INT"
            class Values:
                GTC_FROM_PREVIOUS_DAY = 0
                PARTIAL_FILL_REMAINING = 1
                ORDER_CHANGED = 2

        class OrigCustOrderCapacity:
            Tag = 1432
            Type = "INT"
            class Values:
                MEMBER_TRADING_FOR_THEIR_OWN_ACCOUNT = 1
                CLEARING_FIRM_TRADING_FOR_ITS_PROPRIETARY_ACCOUNT = 2
                MEMBER_TRADING_FOR_ANOTHER_MEMBER = 3
                ALL_OTHER = 4

        class RefApplReqID:
            Tag = 1433
            Type = "STRING"

        class ModelType:
            Tag = 1434
            Type = "INT"
            class Values:
                UTILITY_PROVIDED_STANDARD_MODEL = 0
                PROPRIETARY = 1

        class ContractMultiplierUnit:
            Tag = 1435
            Type = "INT"
            class Values:
                SHARES = 0
                HOURS = 1
                DAYS = 2

        class LegContractMultiplierUnit:
            Tag = 1436
            Type = "INT"

        class UnderlyingContractMultiplierUnit:
            Tag = 1437
            Type = "INT"

        class DerivativeContractMultiplierUnit:
            Tag = 1438
            Type = "INT"

        class FlowScheduleType:
            Tag = 1439
            Type = "INT"
            class Values:
                NERC_EASTERN_OFF_PEAK = 0
                NERC_WESTERN_OFF_PEAK = 1
                NERC_CALENDAR_ALL_DAYS_IN_MONTH = 2
                NERC_EASTERN_PEAK = 3
                NERC_WESTERN_PEAK = 4

        class LegFlowScheduleType:
            Tag = 1440
            Type = "INT"

        class UnderlyingFlowScheduleType:
            Tag = 1441
            Type = "INT"

        class DerivativeFlowScheduleType:
            Tag = 1442
            Type = "INT"

        class FillLiquidityInd:
            Tag = 1443
            Type = "INT"

        class SideLiquidityInd:
            Tag = 1444
            Type = "INT"

        class NoRateSources:
            Tag = 1445
            Type = "NUMINGROUP"

        class RateSource:
            Tag = 1446
            Type = "INT"
            class Values:
                BLOOMBERG = 0
                REUTERS = 1
                TELERATE = 2
                OTHER = 99

        class RateSourceType:
            Tag = 1447
            Type = "INT"
            class Values:
                PRIMARY = 0
                SECONDARY = 1

        class ReferencePage:
            Tag = 1448
            Type = "STRING"

        class RestructuringType:
            Tag = 1449
            Type = "STRING"
            class Values:
                FULL_RESTRUCTURING = "FR"
                MODIFIED_RESTRUCTURING = "MR"
                MODIFIED_MOD_RESTRUCTURING = "MM"
                NO_RESTRUCTURING_SPECIFIED = "XR"

        class Seniority:
            Tag = 1450
            Type = "STRING"
            class Values:
                SENIOR_SECURED = "SD"
                SENIOR = "SR"
                SUBORDINATED = "SB"

        class NotionalPercentageOutstanding:
            Tag = 1451
            Type = "PERCENTAGE"

        class OriginalNotionalPercentageOutstanding:
            Tag = 1452
            Type = "PERCENTAGE"

        class UnderlyingRestructuringType:
            Tag = 1453
            Type = "STRING"

        class UnderlyingSeniority:
            Tag = 1454
            Type = "STRING"

        class UnderlyingNotionalPercentageOutstanding:
            Tag = 1455
            Type = "PERCENTAGE"

        class UnderlyingOriginalNotionalPercentageOutstanding:
            Tag = 1456
            Type = "PERCENTAGE"

        class AttachmentPoint:
            Tag = 1457
            Type = "PERCENTAGE"

        class DetachmentPoint:
            Tag = 1458
            Type = "PERCENTAGE"

        class UnderlyingAttachmentPoint:
            Tag = 1459
            Type = "PERCENTAGE"

        class UnderlyingDetachmentPoint:
            Tag = 1460
            Type = "PERCENTAGE"

        class NoTargetPartyIDs:
            Tag = 1461
            Type = "NUMINGROUP"

        class TargetPartyID:
            Tag = 1462
            Type = "STRING"

        class TargetPartyIDSource:
            Tag = 1463
            Type = "CHAR"

        class TargetPartyRole:
            Tag = 1464
            Type = "INT"

        class SecurityListID:
            Tag = 1465
            Type = "STRING"

        class SecurityListRefID:
            Tag = 1466
            Type = "STRING"

        class SecurityListDesc:
            Tag = 1467
            Type = "STRING"

        class EncodedSecurityListDescLen:
            Tag = 1468
            Type = "LENGTH"

        class EncodedSecurityListDesc:
            Tag = 1469
            Type = "DATA"

        class SecurityListType:
            Tag = 1470
            Type = "INT"
            class Values:
                INDUSTRY_CLASSIFICATION = 1
                TRADING_LIST = 2
                MARKET = 3
                NEWSPAPER_LIST = 4

        class SecurityListTypeSource:
            Tag = 1471
            Type = "INT"
            class Values:
                ICB = 1
                NAICS = 2
                GICS = 3

        class NewsID:
            Tag = 1472
            Type = "STRING"

        class NewsCategory:
            Tag = 1473
            Type = "INT"
            class Values:
                COMPANY_NEWS = 0
                MARKETPLACE_NEWS = 1
                FINANCIAL_MARKET_NEWS = 2
                TECHNICAL_NEWS = 3
                OTHER_NEWS = 99

        class LanguageCode:
            Tag = 1474
            Type = "LANGUAGE"

        class NoNewsRefIDs:
            Tag = 1475
            Type = "NUMINGROUP"

        class NewsRefID:
            Tag = 1476
            Type = "STRING"

        class NewsRefType:
            Tag = 1477
            Type = "INT"
            class Values:
                REPLACEMENT = 0
                OTHER_LANGUAGE = 1
                COMPLIMENTARY = 2

        class StrikePriceDeterminationMethod:
            Tag = 1478
            Type = "INT"
            class Values:
                FIXED_STRIKE = 1
                STRIKE_SET_AT_EXPIRATION_TO_UNDERLYING_OR_OTHER_VALUE = 2
                STRIKE_SET_TO_AVERAGE_OF_UNDERLYING_SETTLEMENT_PRICE_ACROSS_THE_LIFE_OF_THE_OPTION = 3
                STRIKE_SET_TO_OPTIMAL_VALUE = 4

        class StrikePriceBoundaryMethod:
            Tag = 1479
            Type = "INT"
            class Values:
                LESS_THAN_UNDERLYING_PRICE_IS_IN_THE_MONEY = 1
                LESS_THAN_OR_EQUAL_TO_THE_UNDERLYING_PRICE_IS_IN_THE_MONEY = 2
                EQUAL_TO_THE_UNDERLYING_PRICE_IS_IN_THE_MONEY = 3
                GREATER_THAN_OR_EQUAL_TO_UNDERLYING_PRICE_IS_IN_THE_MONEY = 4
                GREATER_THAN_UNDERLYING_IS_IN_THE_MONEY = 5

        class StrikePriceBoundaryPrecision:
            Tag = 1480
            Type = "PERCENTAGE"

        class UnderlyingPriceDeterminationMethod:
            Tag = 1481
            Type = "INT"
            class Values:
                REGULAR = 1
                SPECIAL_REFERENCE = 2
                OPTIMAL_VALUE = 3
                AVERAGE_VALUE = 4

        class OptPayoutType:
            Tag = 1482
            Type = "INT"
            class Values:
                VANILLA = 1
                CAPPED = 2
                BINARY = 3

        class NoComplexEvents:
            Tag = 1483
            Type = "NUMINGROUP"

        class ComplexEventType:
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

        class ComplexOptPayoutAmount:
            Tag = 1485
            Type = "AMT"

        class ComplexEventPrice:
            Tag = 1486
            Type = "PRICE"

        class ComplexEventPriceBoundaryMethod:
            Tag = 1487
            Type = "INT"
            class Values:
                LESS_THAN_COMPLEXEVENTPRICE = 1
                LESS_THAN_OR_EQUAL_TO_COMPLEXEVENTPRICE = 2
                EQUAL_TO_COMPLEXEVENTPRICE = 3
                GREATER_THAN_OR_EQUAL_TO_COMPLEXEVENTPRICE = 4
                GREATER_THAN_COMPLEXEVENTPRICE = 5

        class ComplexEventPriceBoundaryPrecision:
            Tag = 1488
            Type = "PERCENTAGE"

        class ComplexEventPriceTimeType:
            Tag = 1489
            Type = "INT"
            class Values:
                EXPIRATION = 1
                IMMEDIATE = 2
                SPECIFIED_DATE_TIME = 3

        class ComplexEventCondition:
            Tag = 1490
            Type = "INT"
            class Values:
                AND = 1
                OR = 2

        class NoComplexEventDates:
            Tag = 1491
            Type = "NUMINGROUP"

        class ComplexEventStartDate:
            Tag = 1492
            Type = "UTCTIMESTAMP"

        class ComplexEventEndDate:
            Tag = 1493
            Type = "UTCTIMESTAMP"

        class NoComplexEventTimes:
            Tag = 1494
            Type = "NUMINGROUP"

        class ComplexEventStartTime:
            Tag = 1495
            Type = "UTCTIMEONLY"

        class ComplexEventEndTime:
            Tag = 1496
            Type = "UTCTIMEONLY"

        class StreamAsgnReqID:
            Tag = 1497
            Type = "STRING"

        class StreamAsgnReqType:
            Tag = 1498
            Type = "INT"
            class Values:
                STREAM_ASSIGNMENT_FOR_NEW_CUSTOMER = 1
                STREAM_ASSIGNMENT_FOR_EXISTING_CUSTOMER = 2

        class NoAsgnReqs:
            Tag = 1499
            Type = "NUMINGROUP"

        class MDStreamID:
            Tag = 1500
            Type = "STRING"

        class StreamAsgnRptID:
            Tag = 1501
            Type = "STRING"

        class StreamAsgnRejReason:
            Tag = 1502
            Type = "INT"
            class Values:
                UNKNOWN_CLIENT = 0
                EXCEEDS_MAXIMUM_SIZE = 1
                UNKNOWN_OR_INVALID_CURRENCY_PAIR = 2
                NO_AVAILABLE_STREAM = 3
                OTHER = 99

        class StreamAsgnAckType:
            Tag = 1503
            Type = "INT"
            class Values:
                ASSIGNMENT_ACCEPTED = 0
                ASSIGNMENT_REJECTED = 1

        class RelSymTransactTime:
            Tag = 1504
            Type = "UTCTIMESTAMP"

        class StreamAsgnType:
            Tag = 1617
            Type = "INT"
            class Values:
                ASSIGNMENT = 1
                REJECTED = 2
                TERMINATE_UNASSIGN = 3

