# PySNMP SMI module. Autogenerated from smidump -f python TIME-AGGREGATE-MIB
# by libsmi2pysnmp-0.0.9-alpha at Fri Jul  9 17:12:47 2010,
# Python version sys.version_info(major=2, minor=7, micro=0, releaselevel='final', serial=0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( OwnerString, ) = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Opaque, TimeTicks, experimental, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Opaque", "TimeTicks", "experimental")
( RowStatus, StorageType, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "TextualConvention")

# Types

class CompressedTimeAggrMOValue(Opaque):
    subtypeSpec = Opaque.subtypeSpec+constraint.ValueSizeConstraint(0,1024)
    pass

class TAggrMOErrorStatus(Opaque):
    subtypeSpec = Opaque.subtypeSpec+constraint.ValueSizeConstraint(0,1024)
    pass

class TimeAggrMOValue(Opaque):
    subtypeSpec = Opaque.subtypeSpec+constraint.ValueSizeConstraint(0,1024)
    pass


# Objects

tAggrMIB = ModuleIdentity((1, 3, 6, 1, 3, 124)).setRevisions(("2006-04-27 00:00",))
if mibBuilder.loadTexts: tAggrMIB.setOrganization("Cyber Solutions Inc. NetMan Working Group")
if mibBuilder.loadTexts: tAggrMIB.setContactInfo("                      Glenn Mansfield Keeni\nPostal: Cyber Solutions Inc.\n        6-6-3, Minami Yoshinari\n        Aoba-ku, Sendai, Japan 989-3204.\n   Tel: +81-22-303-4012\n   Fax: +81-22-303-4015\nE-mail: glenn@cysols.com\n\nSupport Group E-mail: mibsupport@cysols.com")
if mibBuilder.loadTexts: tAggrMIB.setDescription("The MIB for servicing Time-Based aggregate\nobjects.\n\nCopyright (C) The Internet Society (2006).  This\nversion of this MIB module is part of RFC 4498;\nsee the RFC itself for full legal notices.")
tAggrCtlTable = MibTable((1, 3, 6, 1, 3, 124, 1))
if mibBuilder.loadTexts: tAggrCtlTable.setDescription("The Time-Based aggregation control table.  It controls\nthe aggregation of the samples of MO instances.  There\nwill be a row for each TAgMO.")
tAggrCtlEntry = MibTableRow((1, 3, 6, 1, 3, 124, 1, 1)).setIndexNames((0, "TIME-AGGREGATE-MIB", "tAggrCtlEntryID"))
if mibBuilder.loadTexts: tAggrCtlEntry.setDescription("A row of the control table that defines one Time-Based\naggregate MO (TAgMO).")
tAggrCtlEntryID = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: tAggrCtlEntryID.setDescription("A locally unique, administratively assigned name\nfor this aggregated MO.  It is used as an index to\nuniquely identify this row in the table.")
tAggrCtlMOInstance = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlMOInstance.setDescription("The sampled values of this MO instance will be\naggregated by the TAgMO.")
tAggrCtlAgMODescr = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlAgMODescr.setDescription("A textual description of the aggregate object.")
tAggrCtlInterval = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlInterval.setDescription("The interval, in microseconds, at which the MO instance\npointed at by tAggrInstance will be sampled for\nTime-Based aggregation.")
tAggrCtlSamples = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlSamples.setDescription("The number of times at which the MO instance referred\nto by tAggrInstance will be sampled for Time-Based\naggregation.")
tAggrCtlCompressionAlgorithm = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 6), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(1,2,)).subtype(namedValues=namedval.NamedValues(("none", 1), ("deflate", 2), )).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlCompressionAlgorithm.setDescription("The compression algorithm that will be used by\nthe agent to compress the value of the TAgMO.\nThe deflate algorithm and corresponding data format\nspecification is described in RFC 1951.  It is\ncompatible with the widely used gzip utility.")
tAggrCtlEntryOwner = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 7), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlEntryOwner.setDescription("A textual description of the entity that created\nthis entry.")
tAggrCtlEntryStorageType = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 8), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlEntryStorageType.setDescription("This object defines whether the parameters defined in\nthis row are kept in volatile storage and lost upon\nreboot or backed up by non-volatile (permanent)\nstorage.\nConceptual rows having the value 'permanent' need not\nallow write-access to any columnar objects in the row.")
tAggrCtlEntryStatus = MibTableColumn((1, 3, 6, 1, 3, 124, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tAggrCtlEntryStatus.setDescription("The row status variable, used according to row\ninstallation and removal conventions.\nObjects in a row can be modified only when the value of\nthis object in the corresponding conceptual row is not\n'active'.\nThus, to modify one or more of the objects in this\nconceptual row,\n  a. change the row status to 'notInService',\n  b. change the values of the row, and\n  c. change the row status to 'active'.\nThe tAggrCtlEntryStatus may be changed to 'active' iff\nall the MOs in the conceptual row have been assigned\nvalid values.")
tAggrDataTable = MibTable((1, 3, 6, 1, 3, 124, 2))
if mibBuilder.loadTexts: tAggrDataTable.setDescription("This is the data table.  Each row of this table contains\ninformation about a TAgMO indexed by tAggrCtlEntryID.\ntAggrCtlEntryID is the key to the table.  It is used to\nidentify instances of the TAgMO that are present in the\ntable.")
tAggrDataEntry = MibTableRow((1, 3, 6, 1, 3, 124, 2, 1)).setIndexNames((0, "TIME-AGGREGATE-MIB", "tAggrCtlEntryID"))
if mibBuilder.loadTexts: tAggrDataEntry.setDescription("Entry containing information pertaining\nto a TAgMO.")
tAggrDataRecord = MibTableColumn((1, 3, 6, 1, 3, 124, 2, 1, 1), TimeAggrMOValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tAggrDataRecord.setDescription("The snapshot value of the TAgMO.")
tAggrDataRecordCompressed = MibTableColumn((1, 3, 6, 1, 3, 124, 2, 1, 2), CompressedTimeAggrMOValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tAggrDataRecordCompressed.setDescription("The compressed value of the TAgMO.\nThe compression algorithm will depend on the\ntAggrCtlCompressionAlgorithm given in the corresponding\ntAggrCtlEntry.  If the value of the corresponding\ntAggrCtlCompressionAlgorithm is (1) 'none', then the\n\n\n\nvalue of all instances of this object will be a string\nof zero length.\nNote that the access privileges to this object will be\ngoverned by the access privileges of the corresponding MO\ninstance.  Thus, an entity attempting to access an\ninstance of this MO MUST have access rights to the\ninstance object pointed at by tAggrCtlMOInstance and this\nMO instance.")
tAggrDataErrorRecord = MibTableColumn((1, 3, 6, 1, 3, 124, 2, 1, 3), TAggrMOErrorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tAggrDataErrorRecord.setDescription("The error status corresponding to the MO instance\nsamples aggregated in tAggrDataRecord (and\ntAggrDataRecordCompressed).")
tAggrConformance = MibIdentifier((1, 3, 6, 1, 3, 124, 3))
tAggrGroups = MibIdentifier((1, 3, 6, 1, 3, 124, 3, 1))
tAggrCompliances = MibIdentifier((1, 3, 6, 1, 3, 124, 3, 2))

# Augmentions

# Groups

tAggrMibBasicGroup = ObjectGroup((1, 3, 6, 1, 3, 124, 3, 1, 1)).setObjects(("TIME-AGGREGATE-MIB", "tAggrCtlMOInstance"), ("TIME-AGGREGATE-MIB", "tAggrCtlEntryStatus"), ("TIME-AGGREGATE-MIB", "tAggrDataErrorRecord"), ("TIME-AGGREGATE-MIB", "tAggrCtlEntryStorageType"), ("TIME-AGGREGATE-MIB", "tAggrDataRecordCompressed"), ("TIME-AGGREGATE-MIB", "tAggrCtlAgMODescr"), ("TIME-AGGREGATE-MIB", "tAggrCtlInterval"), ("TIME-AGGREGATE-MIB", "tAggrCtlCompressionAlgorithm"), ("TIME-AGGREGATE-MIB", "tAggrDataRecord"), ("TIME-AGGREGATE-MIB", "tAggrCtlSamples"), ("TIME-AGGREGATE-MIB", "tAggrCtlEntryOwner"), )

# Exports

# Module identity
mibBuilder.exportSymbols("TIME-AGGREGATE-MIB", PYSNMP_MODULE_ID=tAggrMIB)

# Types
mibBuilder.exportSymbols("TIME-AGGREGATE-MIB", CompressedTimeAggrMOValue=CompressedTimeAggrMOValue, TAggrMOErrorStatus=TAggrMOErrorStatus, TimeAggrMOValue=TimeAggrMOValue)

# Objects
mibBuilder.exportSymbols("TIME-AGGREGATE-MIB", tAggrMIB=tAggrMIB, tAggrCtlTable=tAggrCtlTable, tAggrCtlEntry=tAggrCtlEntry, tAggrCtlEntryID=tAggrCtlEntryID, tAggrCtlMOInstance=tAggrCtlMOInstance, tAggrCtlAgMODescr=tAggrCtlAgMODescr, tAggrCtlInterval=tAggrCtlInterval, tAggrCtlSamples=tAggrCtlSamples, tAggrCtlCompressionAlgorithm=tAggrCtlCompressionAlgorithm, tAggrCtlEntryOwner=tAggrCtlEntryOwner, tAggrCtlEntryStorageType=tAggrCtlEntryStorageType, tAggrCtlEntryStatus=tAggrCtlEntryStatus, tAggrDataTable=tAggrDataTable, tAggrDataEntry=tAggrDataEntry, tAggrDataRecord=tAggrDataRecord, tAggrDataRecordCompressed=tAggrDataRecordCompressed, tAggrDataErrorRecord=tAggrDataErrorRecord, tAggrConformance=tAggrConformance, tAggrGroups=tAggrGroups, tAggrCompliances=tAggrCompliances)

# Groups
mibBuilder.exportSymbols("TIME-AGGREGATE-MIB", tAggrMibBasicGroup=tAggrMibBasicGroup)
