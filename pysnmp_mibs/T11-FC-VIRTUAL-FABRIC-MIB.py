# PySNMP SMI module. Autogenerated from smidump -f python T11-FC-VIRTUAL-FABRIC-MIB
# by libsmi2pysnmp-0.1.1 at Sun Nov  6 01:16:18 2011,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( FcNameIdOrZero, fcmInstanceIndex, fcmPortEntry, fcmSwitchEntry, ) = mibBuilder.importSymbols("FC-MGMT-MIB", "FcNameIdOrZero", "fcmInstanceIndex", "fcmPortEntry", "fcmSwitchEntry")
( InterfaceIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2")
( RowStatus, StorageType, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType")
( T11FabricIndex, ) = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")

# Objects

t11FcVirtualFabricMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 147)).setRevisions(("2006-11-10 00:00",))
if mibBuilder.loadTexts: t11FcVirtualFabricMIB.setOrganization("IETF IMSS (Internet and Management Support\nfor Storage) Working Group")
if mibBuilder.loadTexts: t11FcVirtualFabricMIB.setContactInfo("\nScott Kipp\nMcDATA Corporation\nTel: +1 720 558-3452\nE-mail: scott.kipp@mcdata.com\nPostal: 4 McDATA Parkway\nBroomfield, CO USA 80021\n\nG D Ramkumar\nSnapTell, Inc.\nTel: +1 650-326-7627\nE-mail: gramkumar@stanfordalumni.org\nPostal: 2741 Middlefield Rd, Suite 200\nPalo Alto, CA USA 94306\n\nKeith McCloghrie\nCisco Systems, Inc.\nTel: +1 408 526-5260\nE-mail: kzm@cisco.com\nPostal: 170 West Tasman Drive\nSan Jose, CA USA 95134")
if mibBuilder.loadTexts: t11FcVirtualFabricMIB.setDescription("This module defines management information specific to\nFibre Channel Virtual Fabrics.  A Virtual Fabric is a\n\n\n\nFabric composed of partitions of switches, links and\nN_Ports with a single Fabric management domain, Fabric\nServices and independence from other Virtual Fabrics.\n\nCopyright (C) The IETF Trust (2006).  This version of\nthis MIB module is part of RFC 4747; see the RFC itself for\nfull legal notices.")
t11vfObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 147, 1))
t11vfCoreSwitchTable = MibTable((1, 3, 6, 1, 2, 1, 147, 1, 1))
if mibBuilder.loadTexts: t11vfCoreSwitchTable.setDescription("A table of core switches supported by the current\nmanagement entity.")
t11vfCoreSwitchEntry = MibTableRow((1, 3, 6, 1, 2, 1, 147, 1, 1, 1)).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "T11-FC-VIRTUAL-FABRIC-MIB", "t11vfCoreSwitchSwitchName"))
if mibBuilder.loadTexts: t11vfCoreSwitchEntry.setDescription("Each entry represents one core switch.")
t11vfCoreSwitchSwitchName = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 1, 1, 1), FcNameIdOrZero().subtype(subtypeSpec=constraint.ConstraintsUnion(constraint.ValueSizeConstraint(8,8),constraint.ValueSizeConstraint(16,16),))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: t11vfCoreSwitchSwitchName.setDescription("The Core Switch_Name (WWN) of this Core Switch.")
t11vfCoreSwitchMaxSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11vfCoreSwitchMaxSupported.setDescription("In switches that do not support Virtual Fabrics,\nthis object has the value of 1.  If Virtual Fabrics\nare supported, this object is the maximum number of\nVirtual Fabrics supported by the Core Switch.  For\nthe purpose of this count, the Control VF_ID is\nignored.")
t11vfCoreSwitchStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 1, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11vfCoreSwitchStorageType.setDescription("The storage type for this conceptual row.\nConceptual rows having the value 'permanent' need not\nallow write-access to any columnar objects in the row.")
t11vfVirtualSwitchTable = MibTable((1, 3, 6, 1, 2, 1, 147, 1, 2))
if mibBuilder.loadTexts: t11vfVirtualSwitchTable.setDescription("A table of Virtual Switches.  When one Core Switch\nprovides switching functions for multiple Virtual Fabrics,\nthat Core Switch is modeled as containing multiple\nVirtual Switches, one for each Virtual Fabric.  This table\ncontains one row for every Virtual Switch on every Core\nSwitch.  This table augments the basic switch information in\nthe fcmSwitchTable Table in the FC-MGMT-MIB.")
t11vfVirtualSwitchEntry = MibTableRow((1, 3, 6, 1, 2, 1, 147, 1, 2, 1))
if mibBuilder.loadTexts: t11vfVirtualSwitchEntry.setDescription("An entry of the Virtual Switch table.  Each row is for a\nVirtual Switch.\n\nThis table augments the fcmSwitchTable, i.e., every entry\nin this table has a one-to-one correspondence with an\nentry in the fcmSwitchTable.  At the time when the\nfcmSwitchTable was defined, it applied to physical\nswitches.  With the definition and usage of virtual\nswitches, fcmSwitchTable now applies to virtual switches\nas well as physical switches, and (in contrast to physical\nswitches) it is appropriate to provide the capability for\nvirtual switches to be created via remote management\napplications, e.g., via SNMP.\n\nSo, this entry contains a RowStatus object (to allow the\ncreation of a virtual switch), as well as a StorageType\nobject.  Obviously, if a row is created/deleted in this\ntable, the corresponding row in the fcmSwitchTable will\nbe created/deleted.")
t11vfVirtualSwitchVfId = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 2, 1, 1), T11FabricIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11vfVirtualSwitchVfId.setDescription("The VF_ID of the Virtual Fabric for which this virtual\nswitch performs its switching function.  The Control\nVF_ID is implicitly enabled and is not set.\nCommunication with the Control VF_ID is required.")
t11vfVirtualSwitchCoreSwitchName = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 2, 1, 2), FcNameIdOrZero().subtype(subtypeSpec=constraint.ConstraintsUnion(constraint.ValueSizeConstraint(8,8),constraint.ValueSizeConstraint(16,16),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11vfVirtualSwitchCoreSwitchName.setDescription("The Core Switch_Name (WWN) of the Core Switch that\ncontains this Virtual Switch.")
t11vfVirtualSwitchRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11vfVirtualSwitchRowStatus.setDescription("The status of this row.")
t11vfVirtualSwitchStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 2, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11vfVirtualSwitchStorageType.setDescription("The storage type for this conceptual row.\nConceptual rows having the value 'permanent' need not\nallow write-access to any columnar objects in the row.")
t11vfPortTable = MibTable((1, 3, 6, 1, 2, 1, 147, 1, 3))
if mibBuilder.loadTexts: t11vfPortTable.setDescription("A table of Port attributes related to Virtual Fabrics.")
t11vfPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 147, 1, 3, 1))
if mibBuilder.loadTexts: t11vfPortEntry.setDescription("Each entry represents a physical Port on a switch.\nSwitches that support Virtual Fabrics would add\n\n\n\nthese four additional columns to the fcmPortEntry\nrow.")
t11vfPortVfId = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 3, 1, 1), T11FabricIndex().clone('1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11vfPortVfId.setDescription("The Port VF_ID assigned to this Port.  The Port VF_ID is the\ndefault Virtual Fabric that is assigned to untagged frames\narriving at this Port.  The Control VF_ID is implicitly\nenabled and is not set.  Communication with the Control\nVF_ID is required.")
t11vfPortTaggingAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 3, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,3,)).subtype(namedValues=namedval.NamedValues(("off", 1), ("on", 2), ("auto", 3), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11vfPortTaggingAdminStatus.setDescription("This object is used to configure the administrative status\nof Virtual Fabric tagging on this Port.\n\nSET operation   Description\n--------------  -------------------------------------------\noff(1)          To disable Virtual Fabric tagging on this\n                Port.\n\non(2)           To enable Virtual Fabric tagging on this\n\n\n\n                Port if the attached Port doesn't\n                prohibit it.\n\nauto(3)         To enable Virtual Fabric tagging if the\n                peer requests it.")
t11vfPortTaggingOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 3, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("off", 1), ("on", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11vfPortTaggingOperStatus.setDescription("This object is used to report the operational status of\nVirtual Fabric tagging on this Port.\n\nSET operation   Description\n--------------  -------------------------------------------\noff(1)          Virtual Fabric tagging is disabled on this\n                Port.\n\non(2)           Virtual Fabric tagging is enabled on this\n                Port.")
t11vfPortStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 3, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11vfPortStorageType.setDescription("The storage type for this conceptual row, and for the\ncorresponding row in the augmented fcmPortTable.\n\nConceptual rows having the value 'permanent' need not\nallow write-access to any columnar objects in the row.")
t11vfLocallyEnabledTable = MibTable((1, 3, 6, 1, 2, 1, 147, 1, 4))
if mibBuilder.loadTexts: t11vfLocallyEnabledTable.setDescription("A table for assigning and reporting operational status of\nlocally-enabled Virtual Fabric IDs to Ports.  The set of\nVirtual Fabrics operational on the Port is the bit-wise\n'AND' of the set of locally-enabled VF_IDs of this Port\nand the locally-enabled VF_IDs of the attached Port.")
t11vfLocallyEnabledEntry = MibTableRow((1, 3, 6, 1, 2, 1, 147, 1, 4, 1)).setIndexNames((0, "T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledPortIfIndex"), (0, "T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledVfId"))
if mibBuilder.loadTexts: t11vfLocallyEnabledEntry.setDescription("An entry for each locally-enabled VF_ID on\neach Port.")
t11vfLocallyEnabledPortIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 1), InterfaceIndex()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: t11vfLocallyEnabledPortIfIndex.setDescription("The value of the ifIndex that identifies the Port.")
t11vfLocallyEnabledVfId = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 2), T11FabricIndex()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: t11vfLocallyEnabledVfId.setDescription("A locally-enabled VF_ID on this Port.")
t11vfLocallyEnabledOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 3), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(2,1,)).subtype(namedValues=namedval.NamedValues(("off", 1), ("on", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11vfLocallyEnabledOperStatus.setDescription("This object is used to report the operational status of\nVirtual Fabric tagging on this Port.\n\nSET operation   Description\n--------------  -------------------------------------------\noff(1)          Virtual Fabric tagging is disabled on this\n                Port.\n\non(2)           Virtual Fabric tagging is enabled on this\n                Port.")
t11vfLocallyEnabledRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11vfLocallyEnabledRowStatus.setDescription("The status of this conceptual row.\n\nWhen a row in this table is in 'active(1)' state,\nno object in that row can be modified except\nt11vfLocallyEnabledRowStatus and\nt11vfLocallyEnabledStorageType.")
t11vfLocallyEnabledStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11vfLocallyEnabledStorageType.setDescription("The storage type for this conceptual row.\nConceptual rows having the value 'permanent' need not\nallow write-access to any columnar objects in the row.")
t11vfConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 147, 2))
t11vfMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 147, 2, 1))
t11vfMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 147, 2, 2))

# Augmentions
fcmPortEntry, = mibBuilder.importSymbols("FC-MGMT-MIB", "fcmPortEntry")
fcmPortEntry.registerAugmentions(("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortEntry"))
t11vfPortEntry.setIndexNames(*fcmPortEntry.getIndexNames())
fcmSwitchEntry, = mibBuilder.importSymbols("FC-MGMT-MIB", "fcmSwitchEntry")
fcmSwitchEntry.registerAugmentions(("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchEntry"))
t11vfVirtualSwitchEntry.setIndexNames(*fcmSwitchEntry.getIndexNames())

# Groups

t11vfGeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 147, 2, 2, 1)).setObjects(("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortStorageType"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledRowStatus"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfCoreSwitchMaxSupported"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchRowStatus"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortVfId"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfCoreSwitchStorageType"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortTaggingAdminStatus"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledOperStatus"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchCoreSwitchName"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledStorageType"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortTaggingOperStatus"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchVfId"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchStorageType"), )
if mibBuilder.loadTexts: t11vfGeneralGroup.setDescription("A collection of objects for monitoring and\nconfiguring Virtual Fabrics in a Fibre Channel switch.")

# Compliances

t11vfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 147, 2, 1, 1)).setObjects(("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfGeneralGroup"), )
if mibBuilder.loadTexts: t11vfMIBCompliance.setDescription("Describes the requirements for compliance to the\nFibre Channel Virtual Fabric MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("T11-FC-VIRTUAL-FABRIC-MIB", PYSNMP_MODULE_ID=t11FcVirtualFabricMIB)

# Objects
mibBuilder.exportSymbols("T11-FC-VIRTUAL-FABRIC-MIB", t11FcVirtualFabricMIB=t11FcVirtualFabricMIB, t11vfObjects=t11vfObjects, t11vfCoreSwitchTable=t11vfCoreSwitchTable, t11vfCoreSwitchEntry=t11vfCoreSwitchEntry, t11vfCoreSwitchSwitchName=t11vfCoreSwitchSwitchName, t11vfCoreSwitchMaxSupported=t11vfCoreSwitchMaxSupported, t11vfCoreSwitchStorageType=t11vfCoreSwitchStorageType, t11vfVirtualSwitchTable=t11vfVirtualSwitchTable, t11vfVirtualSwitchEntry=t11vfVirtualSwitchEntry, t11vfVirtualSwitchVfId=t11vfVirtualSwitchVfId, t11vfVirtualSwitchCoreSwitchName=t11vfVirtualSwitchCoreSwitchName, t11vfVirtualSwitchRowStatus=t11vfVirtualSwitchRowStatus, t11vfVirtualSwitchStorageType=t11vfVirtualSwitchStorageType, t11vfPortTable=t11vfPortTable, t11vfPortEntry=t11vfPortEntry, t11vfPortVfId=t11vfPortVfId, t11vfPortTaggingAdminStatus=t11vfPortTaggingAdminStatus, t11vfPortTaggingOperStatus=t11vfPortTaggingOperStatus, t11vfPortStorageType=t11vfPortStorageType, t11vfLocallyEnabledTable=t11vfLocallyEnabledTable, t11vfLocallyEnabledEntry=t11vfLocallyEnabledEntry, t11vfLocallyEnabledPortIfIndex=t11vfLocallyEnabledPortIfIndex, t11vfLocallyEnabledVfId=t11vfLocallyEnabledVfId, t11vfLocallyEnabledOperStatus=t11vfLocallyEnabledOperStatus, t11vfLocallyEnabledRowStatus=t11vfLocallyEnabledRowStatus, t11vfLocallyEnabledStorageType=t11vfLocallyEnabledStorageType, t11vfConformance=t11vfConformance, t11vfMIBCompliances=t11vfMIBCompliances, t11vfMIBGroups=t11vfMIBGroups)

# Groups
mibBuilder.exportSymbols("T11-FC-VIRTUAL-FABRIC-MIB", t11vfGeneralGroup=t11vfGeneralGroup)

# Compliances
mibBuilder.exportSymbols("T11-FC-VIRTUAL-FABRIC-MIB", t11vfMIBCompliance=t11vfMIBCompliance)
