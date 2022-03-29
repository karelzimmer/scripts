<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" indent="yes" encoding="UTF-8" />

<!--<xsl:variable name="zkid" select="3"/>-->
<!--<xsl:variable name="zkid">4</xsl:variable>-->
	<!-- vlg is globale param met evt default waarde, kan van buiten gevuld worden -->
<xsl:param name="zkid">3</xsl:param>

<xsl:template match="/adressen">
	<table width="50%" border="1" bgcolor="aquamarine" style="font:small Arial,sans-serif;">
		<tr><th colspan="3">Mijn adressenlijst</th></tr>
		<!--<xsl:apply-templates select="persoon|klant/persoon" />-->
		<!--<xsl:apply-templates select="persoon" />-->
		<!--<xsl:apply-templates select="persoon[naam=$zkid]" />-->
	<!-- hieronder choose gebruikt ipv if, want if kent geen else -->
		<xsl:choose>
			<xsl:when test="number($zkid)">
				<xsl:apply-templates select="//persoon[@id=$zkid]" />
			</xsl:when>
			<xsl:otherwise>
				<xsl:apply-templates select="//persoon" />
			</xsl:otherwise>
		</xsl:choose>
	</table>
</xsl:template>

<xsl:template match="persoon">
<!-- Python doet vlg ook met > teken -->
	<tr><td><xsl:value-of select="@id"/></td><td><xsl:if test="string-length(vnaam) &gt; 0"><xsl:value-of select="concat(vnaam,' ')" /></xsl:if>
	<xsl:value-of select="naam|anaam"/></td><td><xsl:value-of select="tel"/></td></tr>
</xsl:template>

</xsl:stylesheet>
