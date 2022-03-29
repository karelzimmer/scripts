<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="xml" indent="yes" encoding="UTF-8" />
<!--  method = xml | html | text -->

<!-- Student: zet hieronder de benodigde templates -->

<xsl:variable name="anaam">Dix</xsl:variable>
<!--<xsl:variable name="anaam" select="'Dix'"  />-->		<!-- let op: 'Dix' moet tussen quotes, anders denkt hij dat Dix een node is -->

<xsl:template match="/bookstore">
	<resultaat>
		<var-anaam><xsl:value-of select="$anaam" /></var-anaam>
		<xsl:if test="not($anaam)" >
			<xsl:apply-templates select="book" />
		</xsl:if>
		<xsl:apply-templates select="book[author/lastname=$anaam]"/>
	</resultaat>
</xsl:template>

<xsl:template match="book">
	<xsl:copy-of select="." />
</xsl:template>

</xsl:stylesheet>
