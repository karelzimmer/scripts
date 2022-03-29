<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
xmlns:exslt="http://exslt.org/common"
extension-element-prefixes="exslt"
>
<xsl:output method="xml" indent="yes" encoding="UTF-8" />
<!-- voor exslt:node-set(..) -->

<xsl:variable name="films">
	<!-- dit is een result tree fragment, geen nodeset =>geen xpath mogelijk in xsl 1.0, tenzij je exslt:node-set() gebr -->
	<xsl:for-each select="/bookstore/dvd">
		<film>
			<titel><xsl:value-of select="title" /></titel>
			<lengte><xsl:value-of select="length" /></lengte>
		</film>
	</xsl:for-each>
</xsl:variable>


<xsl:template match="/">
	<films>
		<!--
		<xsl:copy-of select="$films" />																goed, toont alle films
		<xsl:copy-of select="$films/film[2]" />														error, xpath
		<xsl:apply-templates select="$films" />														error, geen node-set
		<xsl:apply-templates select="$films/film" />												error, xpath

		<xsl:copy-of select="exslt:node-set($films)/film[2]" />								goed
		<xsl:apply-templates select="exslt:node-set($films)" />								error, recursie
		<xsl:apply-templates select="exslt:node-set($films)/film" />						goed 
		<xsl:apply-templates select="exslt:node-set($films)/film[lengte>=110]" />
		-->
		<xsl:apply-templates select="exslt:node-set($films)/film" />
		
	</films>
</xsl:template>

<xsl:template match="film">
	<xsl:copy-of select="." />
</xsl:template>

</xsl:stylesheet>
