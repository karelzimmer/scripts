<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="xml" indent="yes" encoding="UTF-8" />
<!--  method = xml | html | text -->

<!-- Student: zet hieronder de benodigde templates -->

<xsl:template match="/bookstore">
	<boeken>
		<xsl:apply-templates select="book" />
	</boeken>
</xsl:template>

<xsl:template match="book">
	<boek>
		<titel><xsl:value-of select="title" /></titel>
		<prijs><xsl:value-of select="price" /></prijs>
	</boek>
</xsl:template>

<!--
<xsl:template match="* | text()">
</xsl:template>
-->

</xsl:stylesheet>
