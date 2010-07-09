# PySNMP SMI module. Autogenerated from smidump -f python SIP-UA-MIB
# by libsmi2pysnmp-0.0.9-alpha at Fri Jul  9 17:12:46 2010,
# Python version sys.version_info(major=2, minor=7, micro=0, releaselevel='final', serial=0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( InetAddress, InetAddressType, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
( applIndex, ) = mibBuilder.importSymbols("NETWORK-SERVICES-MIB", "applIndex")
( SipTCEntityRole, ) = mibBuilder.importSymbols("SIP-TC-MIB", "SipTCEntityRole")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2")

# Objects

sipUAMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 150)).setRevisions(("2007-04-20 00:00",))
if mibBuilder.loadTexts: sipUAMIB.setOrganization("IETF Session Initiation Protocol Working Group")
if mibBuilder.loadTexts: sipUAMIB.setContactInfo("SIP WG email: sip@ietf.org\n\nCo-editor  Kevin Lingle\n\n\n\n           Cisco Systems, Inc.\npostal:    7025 Kit Creek Road\n           P.O. Box 14987\n           Research Triangle Park, NC 27709\n           USA\nemail:     klingle@cisco.com\nphone:     +1 919 476 2029\n\nCo-editor  Joon Maeng\nemail:     jmaeng@austin.rr.com\n\nCo-editor  Jean-Francois Mule\n           CableLabs\npostal:    858 Coal Creek Circle\n           Louisville, CO 80027\n           USA\nemail:     jf.mule@cablelabs.com\nphone:     +1 303 661 9100\n\nCo-editor  Dave Walker\nemail:     drwalker@rogers.com")
if mibBuilder.loadTexts: sipUAMIB.setDescription("Session Initiation Protocol (SIP) User Agent (UA) MIB module.\n\nSIP is an application-layer signaling protocol for creating,\nmodifying, and terminating multimedia sessions with one or more\nparticipants.  These sessions include Internet multimedia\nconferences and Internet telephone calls.  SIP is defined in\nRFC 3261 (June 2002).\n\nA User Agent is an application that contains both a User Agent\nClient (UAC) and a User Agent Server (UAS).  A UAC is an\napplication that initiates a SIP request.  A UAS is an\napplication that contacts the user when a SIP request is\nreceived and that returns a response on behalf of the user.\nThe response accepts, rejects, or redirects the request.\n\nCopyright (C) The IETF Trust (2007).  This version of\nthis MIB module is part of RFC 4780; see the RFC itself for\nfull legal notices.")
sipUAMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 150, 1))
sipUACfgServer = MibIdentifier((1, 3, 6, 1, 2, 1, 150, 1, 1))
sipUACfgServerTable = MibTable((1, 3, 6, 1, 2, 1, 150, 1, 1, 1))
if mibBuilder.loadTexts: sipUACfgServerTable.setDescription("This table contains SIP server configuration objects applicable\nto each SIP user agent in this system.")
sipUACfgServerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 150, 1, 1, 1, 1)).setIndexNames((0, "NETWORK-SERVICES-MIB", "applIndex"), (0, "SIP-UA-MIB", "sipUACfgServerIndex"))
if mibBuilder.loadTexts: sipUACfgServerEntry.setDescription("A row of server configuration.\n\nEach row represents those objects for a particular SIP user\nagent present in this system.  applIndex is used to uniquely\nidentify these instances of SIP user agents and correlate\nthem through the common framework of the NETWORK-SERVICES-MIB\n(RFC 2788).  The same value of applIndex used in the\ncorresponding SIP-COMMON-MIB is used here.")
sipUACfgServerIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 150, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 4294967295L))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: sipUACfgServerIndex.setDescription("A unique identifier of a server address when multiple addresses\n\n\nare configured by the SIP entity.  If one address isn't\nreachable, then another can be tried.")
sipUACfgServerAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 150, 1, 1, 1, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipUACfgServerAddressType.setDescription("This object reflects the type of address contained in the\nassociated instance of sipUACfgServerAddress.")
sipUACfgServerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 150, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipUACfgServerAddress.setDescription("This object reflects the address of a SIP server this user\nagent will use to proxy/redirect calls.  The type of this\naddress is determined by the value of the\nsipUACfgServerAddressType object.")
sipUACfgServerRole = MibTableColumn((1, 3, 6, 1, 2, 1, 150, 1, 1, 1, 1, 4), SipTCEntityRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sipUACfgServerRole.setDescription("This object reflects the function of the SIP server this user\nagent should communicate with: registrar, proxy (outbound\nproxy), etc.")
sipUAMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 150, 2))
sipUAMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 150, 2, 1))
sipUAMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 150, 2, 2))

# Augmentions

# Groups

sipUAConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 150, 2, 2, 1)).setObjects(("SIP-UA-MIB", "sipUACfgServerAddressType"), ("SIP-UA-MIB", "sipUACfgServerAddress"), ("SIP-UA-MIB", "sipUACfgServerRole"), )

# Exports

# Module identity
mibBuilder.exportSymbols("SIP-UA-MIB", PYSNMP_MODULE_ID=sipUAMIB)

# Objects
mibBuilder.exportSymbols("SIP-UA-MIB", sipUAMIB=sipUAMIB, sipUAMIBObjects=sipUAMIBObjects, sipUACfgServer=sipUACfgServer, sipUACfgServerTable=sipUACfgServerTable, sipUACfgServerEntry=sipUACfgServerEntry, sipUACfgServerIndex=sipUACfgServerIndex, sipUACfgServerAddressType=sipUACfgServerAddressType, sipUACfgServerAddress=sipUACfgServerAddress, sipUACfgServerRole=sipUACfgServerRole, sipUAMIBConformance=sipUAMIBConformance, sipUAMIBCompliances=sipUAMIBCompliances, sipUAMIBGroups=sipUAMIBGroups)

# Groups
mibBuilder.exportSymbols("SIP-UA-MIB", sipUAConfigGroup=sipUAConfigGroup)
