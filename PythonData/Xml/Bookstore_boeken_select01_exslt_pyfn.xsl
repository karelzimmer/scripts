<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
  xmlns:math="http://exslt.org/math" xmlns:date="http://exslt.org/dates-and-times"
  xmlns:re="http://exslt.org/regular-expressions"
  xmlns:py="urn:ecr:python-functions"
  extension-element-prefixes="math date re py"
>
<xsl:output method="xml" indent="yes" encoding="UTF-8" />
<!-- Voor xslt2.0 fn's moet je bij xsl-stylesheet version="2.0" zetten.
     Python lxml werkt met 1.0 + exslt extensies, incl re
     (Java xalan geen re)
     De extra namespaces kun je op beide vlg manieren onderdrukken:
	 exclude-result-prefixes="math"
	 extension-element-prefixes="math"
-->

<xsl:template match="/bookstore">
	<resultaat>
		<!--
		<xsl:apply-templates />
		<xsl:apply-templates select="book"/>
		<xsl:apply-templates select="book/title"/>
		<xsl:apply-templates select="book/title[@remark]"/>
		<xsl:apply-templates select="book[author/firstname='Kurt' and author/lastname='Cagle']/title"/>
		<xsl:apply-templates select="book/author[contains(firstname,' ')]"/>
		<xsl:apply-templates select="book/author[lastname[contains(.,'ix')]]"/>
		<xsl:apply-templates select="book/author[contains(lastname,'ix')]"/>
		<xsl:apply-templates select="book[author[contains(lastname,'ix')]]"/>
		<xsl:apply-templates select="book[contains(author/lastname,'ix')]/title"/> werkt niet, contains() wil string, geen node-set
		<xsl:apply-templates select="book[price > 30]"/>
		<xsl:apply-templates select="book[price &gt; 30]"/>
		<xsl:apply-templates select="sum(dvd/length)"/>

		<xsl:value-of select="sum(dvd/length)" />
		
		vlg bij exslt:
		<xsl:apply-templates select="book[author[re:test(lastname,'\w*ix')]]"/>
		<xsl:apply-templates select="book[author[re:test(firstname,'\w*\s\w*') or re:test(lastname,'\w*\s\w*')]]"/>

		<xsl:value-of select="math:min(dvd/length)" />
		<xsl:value-of select="math:max(dvd/length)" />
		<xsl:value-of select="math:avg(dvd/length)" />				error, exslt kent geen avg

		<xsl:value-of select="date:date-time()" />						wordt: 2018-12-15T19:18:19+01:00
			bij alle vlg mag je ook datumstr meegeven in xs:dateTime fmt
		<xsl:value-of select="date:date()" />							wordt: 2018-12-15+01:00
		<xsl:value-of select="date:day-in-month()" />-<xsl:value-of select="date:month-in-year()" />-<xsl:value-of select="date:year()" />

		vlg Python extension function
		<xsl:value-of select="py:upper(book[1]/@genre)" />
		<xsl:value-of select="py:upper(book[1]/title)" />

		<xsl:value-of select="book[3]/price * book[3]/stock" />
		<xsl:value-of select="number(book[3]/price) * number(book[3]/stock)" />

		-->

		<xsl:value-of select="py:upper(book[1]/@genre)" />
		
	</resultaat>
</xsl:template>

<xsl:template match="*">
	<xsl:copy-of select="." />
</xsl:template>

</xsl:stylesheet>
