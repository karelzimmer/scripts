<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="text" encoding="UTF-8" />

<xsl:template match="/adressen">
	<xsl:text>persoon: id, naam, tel
</xsl:text>
	<!--
	<xsl:apply-templates select="persoon"/>
	<xsl:apply-templates select="//persoon"/>
	<xsl:apply-templates select="persoon[naam='Jan Jansen']"/>
	-->
	<xsl:apply-templates select="//persoon"/>
</xsl:template>

<xsl:template match="persoon">
	<xsl:value-of select="@id"/>,"<xsl:value-of select="naam|anaam"/>","<xsl:value-of select="tel"/>"
</xsl:template>

</xsl:stylesheet>
