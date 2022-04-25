<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="html" indent="yes" encoding="UTF-8" />
<!--  method = xml | html | text -->

<xsl:template match="/bookstore">
	<html>
	<head>
	<title>Boeken</title>
	</head>
	<body>
	<H3>Overzicht boeken</H3>
	<table width="70%" border="1" bgcolor="lightblue" style="font: x-small Arial, sans-serif;">
		<tr><td>title</td><td>price</td><td>stock</td><td>price * stock</td></tr>
		<xsl:apply-templates select="book" />
		<!--<xsl:apply-templates select="book[price > 50]" />-->
		<!--<xsl:apply-templates select="book[price &gt; 50]" />-->
		<!--<xsl:apply-templates select="book[price < 40]" />	deze geeft XmlException-->
		<!--<xsl:apply-templates select="book[price &lt; 50]" />-->
	</table>
	</body>
	</html>
</xsl:template>

<xsl:template match="book">
	<tr><td><xsl:value-of select="title"/></td><td><xsl:value-of select="price"/></td><td><xsl:value-of select="stock"/></td><td><xsl:value-of select="price * stock"/></td></tr>
</xsl:template>

</xsl:stylesheet>
