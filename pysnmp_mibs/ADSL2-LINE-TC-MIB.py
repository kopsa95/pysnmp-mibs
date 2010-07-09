# PySNMP SMI module. Autogenerated from smidump -f python ADSL2-LINE-TC-MIB
# by libsmi2pysnmp-0.0.9-alpha at Fri Jul  9 17:12:36 2010,
# Python version sys.version_info(major=2, minor=7, micro=0, releaselevel='final', serial=0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, transmission, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "transmission")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class Adsl2ChAtmStatus(Bits):
    namedValues = namedval.NamedValues(("noDefect", 0), ("noCellDelineation", 1), ("lossOfCellDelineation", 2), )
    pass

class Adsl2ChPtmStatus(Bits):
    namedValues = namedval.NamedValues(("noDefect", 0), ("outOfSync", 1), )
    pass

class Adsl2ConfPmsForce(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,2,0,)
    namedValues = namedval.NamedValues(("l3toL0", 0), ("l0toL2", 2), ("l0orL2toL3", 3), )
    pass

class Adsl2Direction(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(1,2,)
    namedValues = namedval.NamedValues(("upstream", 1), ("downstream", 2), )
    pass

class Adsl2InitResult(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(5,1,3,4,2,0,)
    namedValues = namedval.NamedValues(("noFail", 0), ("configError", 1), ("configNotFeasible", 2), ("commFail", 3), ("noPeerAtu", 4), ("otherCause", 5), )
    pass

class Adsl2LConfProfPmMode(Bits):
    namedValues = namedval.NamedValues(("allowTransitionsToIdle", 0), ("allowTransitionsToLowPower", 1), )
    pass

class Adsl2LastTransmittedState(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(14,118,131,105,117,124,127,11,104,108,16,102,123,113,29,2,24,8,4,15,17,122,13,27,30,19,22,125,130,5,106,110,119,107,121,101,103,18,6,115,100,1,7,3,120,9,129,126,112,26,21,116,128,10,114,0,32,111,25,23,28,109,20,31,12,)
    namedValues = namedval.NamedValues(("atucG9941", 0), ("atucQuiet1", 1), ("atucMsgfmt", 10), ("aturG9941", 100), ("aturQuiet1", 101), ("aturComb1", 102), ("aturQuiet2", 103), ("aturComb2", 104), ("aturIcomb1", 105), ("aturLineprob", 106), ("aturQuiet3", 107), ("aturComb3", 108), ("aturIcomb2", 109), ("atucMsgpcb", 11), ("aturMsgfmt", 110), ("aturMsgpcb", 111), ("aturReverb1", 112), ("aturQuiet4", 113), ("aturReverb2", 114), ("aturQuiet5", 115), ("aturReverb3", 116), ("aturEct", 117), ("aturReverb4", 118), ("aturSegue1", 119), ("atucQuiet4", 12), ("aturReverb5", 120), ("aturSegue2", 121), ("aturMsg1", 122), ("aturMedley", 123), ("aturExchmarker", 124), ("aturMsg2", 125), ("aturReverb6", 126), ("aturSegue3", 127), ("aturParams", 128), ("aturReverb7", 129), ("atucReverb1", 13), ("aturSegue4", 130), ("aturShowtime", 131), ("atucTref1", 14), ("atucReverb2", 15), ("atucEct", 16), ("atucReverb3", 17), ("atucTref2", 18), ("atucReverb4", 19), ("atucComb1", 2), ("atucSegue1", 20), ("atucMsg1", 21), ("atucReverb5", 22), ("atucSegue2", 23), ("atucMedley", 24), ("atucExchmarker", 25), ("atucMsg2", 26), ("atucReverb6", 27), ("atucSegue3", 28), ("atucParams", 29), ("atucQuiet2", 3), ("atucReverb7", 30), ("atucSegue4", 31), ("atucShowtime", 32), ("atucComb2", 4), ("atucIcomb1", 5), ("atucLineprob", 6), ("atucQuiet3", 7), ("atucComb3", 8), ("atucIComb2", 9), )
    pass

class Adsl2LdsfResult(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(9,11,10,4,6,1,2,7,8,5,3,)
    namedValues = namedval.NamedValues(("none", 1), ("tableFull", 10), ("noResources", 11), ("success", 2), ("inProgress", 3), ("unsupported", 4), ("cannotRun", 5), ("aborted", 6), ("failed", 7), ("illegalMode", 8), ("adminUp", 9), )
    pass

class Adsl2LineLdsf(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(0,1,)
    namedValues = namedval.NamedValues(("inhibit", 0), ("force", 1), )
    pass

class Adsl2LineStatus(Bits):
    namedValues = namedval.NamedValues(("noDefect", 0), ("lossOfFrame", 1), ("lossOfSignal", 2), ("lossOfPower", 3), ("initFailure", 4), )
    pass

class Adsl2MaxBer(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(1,2,3,)
    namedValues = namedval.NamedValues(("eminus3", 1), ("eminus5", 2), ("eminus7", 3), )
    pass

class Adsl2OperationModes(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(30,8,23,20,40,18,26,25,37,36,38,1,28,2,19,10,14,9,11,24,32,15,31,29,21,22,27,33,39,41,)
    namedValues = namedval.NamedValues(("defMode", 1), ("g9923IsdnNonOverlapped", 10), ("g9923isdnOverlapped", 11), ("g9924potsNonOverlapped", 14), ("g9924potsOverlapped", 15), ("g9923AnnexIAllDigNonOverlapped", 18), ("g9923AnnexIAllDigOverlapped", 19), ("adsl", 2), ("g9923AnnexJAllDigNonOverlapped", 20), ("g9923AnnexJAllDigOverlapped", 21), ("g9924AnnexIAllDigNonOverlapped", 22), ("g9924AnnexIAllDigOverlapped", 23), ("g9923AnnexLMode1NonOverlapped", 24), ("g9923AnnexLMode2NonOverlapped", 25), ("g9923AnnexLMode3Overlapped", 26), ("g9923AnnexLMode4Overlapped", 27), ("g9923AnnexMPotsNonOverlapped", 28), ("g9923AnnexMPotsOverlapped", 29), ("g9925PotsNonOverlapped", 30), ("g9925PotsOverlapped", 31), ("g9925IsdnNonOverlapped", 32), ("g9925isdnOverlapped", 33), ("g9925AnnexIAllDigNonOverlapped", 36), ("g9925AnnexIAllDigOverlapped", 37), ("g9925AnnexJAllDigNonOverlapped", 38), ("g9925AnnexJAllDigOverlapped", 39), ("g9925AnnexMPotsNonOverlapped", 40), ("g9925AnnexMPotsOverlapped", 41), ("g9923PotsNonOverlapped", 8), ("g9923PotsOverlapped", 9), )
    pass

class Adsl2PowerMngState(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(3,4,1,2,)
    namedValues = namedval.NamedValues(("l0", 1), ("l1", 2), ("l2", 3), ("l3", 4), )
    pass

class Adsl2PsdMaskDs(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,96)
    pass

class Adsl2PsdMaskUs(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,12)
    pass

class Adsl2RaMode(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(1,3,2,)
    namedValues = namedval.NamedValues(("manual", 1), ("raInit", 2), ("dynamicRa", 3), )
    pass

class Adsl2RfiDs(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,64)
    pass

class Adsl2ScMaskDs(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,64)
    pass

class Adsl2ScMaskUs(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,8)
    pass

class Adsl2SymbolProtection(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(16,5,8,17,7,1,9,10,6,15,11,4,3,2,18,14,12,13,)
    namedValues = namedval.NamedValues(("noProtection", 1), ("eightSymbols", 10), ("nineSymbols", 11), ("tenSymbols", 12), ("elevenSymbols", 13), ("twelveSymbols", 14), ("thirteeSymbols", 15), ("fourteenSymbols", 16), ("fifteenSymbols", 17), ("sixteenSymbols", 18), ("halfSymbol", 2), ("singleSymbol", 3), ("twoSymbols", 4), ("threeSymbols", 5), ("fourSymbols", 6), ("fiveSymbols", 7), ("sixSymbols", 8), ("sevenSymbols", 9), )
    pass

class Adsl2TransmissionModeType(Bits):
    namedValues = namedval.NamedValues(("ansit1413", 0), ("etsi", 1), ("g9922tcmIsdnNonOverlapped", 10), ("g9922tcmIsdnOverlapped", 11), ("g9921tcmIsdnSymmetric", 12), ("reserved1", 13), ("reserved2", 14), ("reserved3", 15), ("reserved4", 16), ("reserved5", 17), ("g9923PotsNonOverlapped", 18), ("g9923PotsOverlapped", 19), ("g9921PotsNonOverlapped", 2), ("g9923IsdnNonOverlapped", 20), ("g9923isdnOverlapped", 21), ("reserved6", 22), ("reserved7", 23), ("g9924potsNonOverlapped", 24), ("g9924potsOverlapped", 25), ("reserved8", 26), ("reserved9", 27), ("g9923AnnexIAllDigNonOverlapped", 28), ("g9923AnnexIAllDigOverlapped", 29), ("g9921PotsOverlapped", 3), ("g9923AnnexJAllDigNonOverlapped", 30), ("g9923AnnexJAllDigOverlapped", 31), ("g9924AnnexIAllDigNonOverlapped", 32), ("g9924AnnexIAllDigOverlapped", 33), ("g9923AnnexLMode1NonOverlapped", 34), ("g9923AnnexLMode2NonOverlapped", 35), ("g9923AnnexLMode3Overlapped", 36), ("g9923AnnexLMode4Overlapped", 37), ("g9923AnnexMPotsNonOverlapped", 38), ("g9923AnnexMPotsOverlapped", 39), ("g9921IsdnNonOverlapped", 4), ("g9925PotsNonOverlapped", 40), ("g9925PotsOverlapped", 41), ("g9925IsdnNonOverlapped", 42), ("g9925isdnOverlapped", 43), ("reserved10", 44), ("reserved11", 45), ("g9925AnnexIAllDigNonOverlapped", 46), ("g9925AnnexIAllDigOverlapped", 47), ("g9925AnnexJAllDigNonOverlapped", 48), ("g9925AnnexJAllDigOverlapped", 49), ("g9921isdnOverlapped", 5), ("g9925AnnexMPotsNonOverlapped", 50), ("g9925AnnexMPotsOverlapped", 51), ("reserved12", 52), ("reserved13", 53), ("reserved14", 54), ("reserved15", 55), ("g9921tcmIsdnNonOverlapped", 6), ("g9921tcmIsdnOverlapped", 7), ("g9922potsNonOverlapped", 8), ("g9922potsOverlapped", 9), )
    pass

class Adsl2Tssi(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,96)
    pass

class Adsl2Unit(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(1,2,)
    namedValues = namedval.NamedValues(("atuc", 1), ("atur", 2), )
    pass


# Objects

adsl2TCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 238, 2)).setRevisions(("2006-10-04 00:00",))
if mibBuilder.loadTexts: adsl2TCMIB.setOrganization("ADSLMIB Working Group")
if mibBuilder.loadTexts: adsl2TCMIB.setContactInfo("WG-email:  adslmib@ietf.org\nInfo:      https://www1.ietf.org/mailman/listinfo/adslmib\n\n          Chair:     Mike Sneed\n                     Sand Channel Systems\n          Postal:    P.O. Box 37324\n                     Raleigh NC 27627-732\n          Email:     sneedmike@hotmail.com\n          Phone:     +1 206 600 7022\n\n          Co-Chair & Co-editor:\n                     Menachem Dodge\n                     ECI Telecom Ltd.\n          Postal:    30 Hasivim St.\n                     Petach Tikva 49517,\n                     Israel.\n          Email:     mbdodge@ieee.org\n          Phone:     +972 3 926 8421\n\n\n\n\n\n\n          Co-editor: Moti Morgenstern\n                     ECI Telecom Ltd.\n          Postal:    30 Hasivim St.\n                     Petach Tikva 49517,\n                     Israel.\n          Email:     moti.morgenstern@ecitele.com\n          Phone:     +972 3 926 6258\n\n          Co-editor: Scott Baillie\n                     NEC Australia\n          Postal:    649-655 Springvale Road,\n                     Mulgrave, Victoria 3170,\n                     Australia.\n          Email:     scott.baillie@nec.com.au\n          Phone:     +61 3 9264 3986\n\n          Co-editor: Umberto Bonollo\n                     NEC Australia\n          Postal:    649-655 Springvale Road,\n                     Mulgrave, Victoria 3170,\n                     Australia.\n          Email:     umberto.bonollo@nec.com.au\n          Phone:     +61 3 9264 3385\n         ")
if mibBuilder.loadTexts: adsl2TCMIB.setDescription("This MIB Module provides Textual Conventions to be\nused by the ADSL2-LINE-MIB module for the purpose of\nmanaging ADSL, ADSL2, and ADSL2+ lines.\n\nCopyright (C) The Internet Society (2006).  This version of\nthis MIB module is part of RFC 4706: see the RFC itself for\nfull legal notices.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("ADSL2-LINE-TC-MIB", PYSNMP_MODULE_ID=adsl2TCMIB)

# Types
mibBuilder.exportSymbols("ADSL2-LINE-TC-MIB", Adsl2ChAtmStatus=Adsl2ChAtmStatus, Adsl2ChPtmStatus=Adsl2ChPtmStatus, Adsl2ConfPmsForce=Adsl2ConfPmsForce, Adsl2Direction=Adsl2Direction, Adsl2InitResult=Adsl2InitResult, Adsl2LConfProfPmMode=Adsl2LConfProfPmMode, Adsl2LastTransmittedState=Adsl2LastTransmittedState, Adsl2LdsfResult=Adsl2LdsfResult, Adsl2LineLdsf=Adsl2LineLdsf, Adsl2LineStatus=Adsl2LineStatus, Adsl2MaxBer=Adsl2MaxBer, Adsl2OperationModes=Adsl2OperationModes, Adsl2PowerMngState=Adsl2PowerMngState, Adsl2PsdMaskDs=Adsl2PsdMaskDs, Adsl2PsdMaskUs=Adsl2PsdMaskUs, Adsl2RaMode=Adsl2RaMode, Adsl2RfiDs=Adsl2RfiDs, Adsl2ScMaskDs=Adsl2ScMaskDs, Adsl2ScMaskUs=Adsl2ScMaskUs, Adsl2SymbolProtection=Adsl2SymbolProtection, Adsl2TransmissionModeType=Adsl2TransmissionModeType, Adsl2Tssi=Adsl2Tssi, Adsl2Unit=Adsl2Unit)

# Objects
mibBuilder.exportSymbols("ADSL2-LINE-TC-MIB", adsl2TCMIB=adsl2TCMIB)

