/*
	xml
	2 sax-parsers:
	SAX1 (oud):			org.xml.sax.HandlerBase					geen namespaces
	SAX2 (nw):			org.xml.sax.helpers.DefaultHandler		wel namespaces

http://www.edankert.com/apis/jaxp.sax-parser-factory.schema-validation.html

http://www.saxproject.org/
features:
http://www.saxproject.org/apidoc/org/xml/sax/package-summary.html#package_description

sax:
Possible values for 'org.xml.sax.driver' Property
Xerces2 (SUN JDK 5.0 distribution):
com.sun.org.apache.xerces.internal.parsers.SAXParser

xslt:
Possible values for 'javax.xml.transform.TransformerFactory' Property
Xalan J (SUN JDK 5.0 distribution):
com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl

*/

import java.text.MessageFormat;
import java.io.*;
import javax.xml.XMLConstants;
import javax.xml.parsers.*;		//SAXParserFactory, SAXParser, ParserConfigurationException, DocumentBuilderFactory, DocumentBuilder
import javax.xml.validation.*;	//SchemaFactory, Schema
import org.xml.sax.*;			//XMLReader, HandlerBase (sax1), InputSource, SAXException, Attributes
import org.xml.sax.helpers.*;	//DefaultHandler (sax2), XMLReaderFactory
import org.w3c.dom.*;			//Document, NodeList, Node, Element, DOMException
import javax.xml.xpath.*;		//XPathFactory, XPath, XPathExpressionException, XPathConstants
import javax.xml.transform.*;	//Source, Result (interfaces), TransformerFactory, Transformer
import javax.xml.transform.stream.*;	//StreamSource, StreamResult, XMLInputFactory
//import javax.xml.transform.dom.*;
//import javax.xml.transform.sax.*;
import javax.xml.stream.*;


import tools.Prompt;

public class TestXml
{
	private static final String ccBookstore = "Bookstore.xml";
	private static final String ccBookstoreXsd = "Bookstore.xsd";
	private static final String ccBookstoreXsl = "Bookstore.xsl";
	private static final String ccAdressen = "Adressen.xml";
	private static final String ccAdressenXsl = "Adressen.xsl";
	
	public static void main(String args[])
	{
		xsltBookstore();
		//xsltAdressen();				//met param
		//xsltAdobeIcml();				//adobe indesign convertor xslt van html naar adobe icml formaat
				
		//Prompt.ready();
	}

	
	private static void xsltBookstore()
	{
		// LET OP: xmlns weghalen in Bookstore.xml
		TransformerFactory fact;
		Transformer xf;
		Source xml, xsl;
		Result out;
		StringWriter sw = null;
		String curdir = null;
		
		xml = new StreamSource(ccBookstore);
		xsl = new StreamSource(ccBookstoreXsl);
		
		//sw = new StringWriter();
		//out = new StreamResult(sw);
		// of:
		curdir = System.getProperty("user.dir") + "\\";		//nodig voor IEXPLORE.EXE
		out = new StreamResult("bookstore.html");		//fname|File|OutputStream|Writer

		try {
			fact = TransformerFactory.newInstance();			//TransformerConfigurationException
			xf = fact.newTransformer(xsl);
			//xf.setParameter("debug", "true()");			//voor <xsl:param name="debug" />
			// com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl
			// com.sun.org.apache.xalan.internal.xsltc.trax.TransformerImpl
			xf.transform(xml, out);
		}
		catch ( TransformerConfigurationException ex) {
			System.out.println(ex); 
		}
		catch ( TransformerException ex) {
			System.out.println(ex); 
		}
		
		if ( sw != null )
			System.out.println(sw.toString());
		else if ( curdir != null ) {
			if ( Prompt.askChar("html tonen in IE? (Y/N) ") == 'Y' ) {
				try {
					Runtime.getRuntime().exec(new String[]{
						"C:\\Program Files\\Internet Explorer\\IEXPLORE.EXE", curdir + "bookstore.html"});
				} catch ( IOException ex ) {
					System.out.println(ex.getMessage());
				}
			}
		}
	}

	private static void xsltAdressen()
	{
		TransformerFactory fact;
		Transformer xf;
		Source xml, xsl;
		Result out;
		StringWriter sw = null;
		
		xml = new StreamSource(ccAdressen);
		xsl = new StreamSource(ccAdressenXsl);
		
		sw = new StringWriter();
		out = new StreamResult(sw);

		try {
			fact = TransformerFactory.newInstance();			//TransformerConfigurationException
			xf = fact.newTransformer(xsl);
			xf.setParameter("zkid", "12");		// 3, 12
			xf.transform(xml, out);
		}
		catch ( TransformerConfigurationException ex) {
			System.out.println(ex); 
		}
		catch ( TransformerException ex) {
			System.out.println(ex); 
		}
		
		if ( sw != null )
			System.out.println(sw.toString());
	}

	private static void xsltAdobeIcml()
	{
		TransformerFactory fact;
		Transformer xf;
		Source xml, xsl;
		Result out;
		StringWriter sw = null;
		
		xml = new StreamSource("story.html");
		xsl = new StreamSource("icml.xsl");
		
		sw = new StringWriter();
		//out = new StreamResult(sw);
		out = new StreamResult("story.icml");		//fname|File|OutputStream|Writer

		try {
			fact = TransformerFactory.newInstance();			//TransformerConfigurationException
			xf = fact.newTransformer(xsl);
			xf.setParameter("table-width", "500");
			xf.transform(xml, out);
		}
		catch ( TransformerConfigurationException ex) {
			System.out.println(ex); 
		}
		catch ( TransformerException ex) {
			System.out.println(ex); 
		}
		
		if ( sw != null )
			System.out.println(sw.toString());
	}
} //class TestXml




/*
XMLReader features:
Turn on Namespaces aware processing.
http://xml.org/sax/features/namespaces

Report original namespace prefixes.
http://xml.org/sax/features/namespace-prefixes

Use String.intern() for all names.
http://xml.org/sax/features/string-interning

Report validation errors.
http://xml.org/sax/features/validation

Include external entities.
http://xml.org/sax/features/external-general-entities

Include external parameter entities.
http://xml.org/sax/features/external-parameter-entities

The XML Parser supports XML 1.0 and 1.1.
http://xml.org/sax/features/xml-1.1

Report unicode normalization errors.
http://xml.org/sax/features/unicode-normalization-checking

Report xmlns uris for xmlns attributes.
http://xml.org/sax/features/xmlns-uris

XMLReader properties:
Returns the current string that is being processed by the XML Reader
http://xml.org/sax/properties/xml-string

Returns the current visited DOMNode if SAX is used as a DOM Iterator.
http://xml.org/sax/properties/dom-node

Description of the XML version.
http://xml.org/sax/properties/document-xml-version

http://xml.org/sax/properties/declaration-handler
http://xml.org/sax/properties/lexical-handler

*/
