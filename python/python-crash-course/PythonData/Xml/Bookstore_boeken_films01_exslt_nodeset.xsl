<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
xmlns:exslt="http://exslt.org/common"
extension-element-prefixes="exslt"
>
<xsl:output method="xml" indent="yes" encoding="UTF-8" />
<!-- voor exslt:node-set(..)
extension-element-prefixes="exslt"
-->

<xsl:variable name="films">
	<!-- wordt in xsl 1.0 result tree fragment ipv nodeset =>Java xalan _ Python lxml
	 xpath alleen mogelijk met exslt:node-set(..); Java xalan daarnaast std fn nodeset() -->
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
		<xsl:copy-of select="$films" />								goed, toont alle films
		<xsl:copy-of select="$films/film[2]" />						error, xpath
		<xsl:apply-templates select="$films" />					error, geen node-set
		<xsl:apply-templates select="$films/film" />				error, xpath

		vlg wel in Java xalan (kan zonder ns decl), niet in Python lxml:
		<xsl:apply-templates select="nodeset($films)/film[lengte > 110]" />

		vlg gelijk in xalan en lxml:
		<xsl:copy-of select="exslt:node-set($films)/film[2]" />		goed
		<xsl:apply-templates select="exslt:node-set($films)" />		error, recursie
		<xsl:apply-templates select="exslt:node-set($films)/film" />	goed
		<xsl:apply-templates select="exslt:node-set($films)/film[lengte >= 110]" />
		<xsl:apply-templates select="exslt:node-set($films)/film[lengte &gt; 110]" />
		<xsl:apply-templates select="exslt:node-set($films)/film[lengte > 110]" />
		vlg error in lxml: entity ge not defined
		<xsl:apply-templates select="exslt:node-set($films)/film[lengte &ge; 110]" />		error
		-->
		
		<xsl:apply-templates select="exslt:node-set($films)/film[lengte &lt; 110]" />
		
	</films>
</xsl:template>

<xsl:template match="film">
	<xsl:copy-of select="." />
</xsl:template>

</xsl:stylesheet>
