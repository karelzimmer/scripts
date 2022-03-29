# contact zoeken met sql express en Northwind db

r"""
(de r voor raw; anders errors verkeerd einde string enz.)

sqlexpress 2008R2 64-bit geinstalleerd
sql server configuration manager (vlg 2 niet nodig voor pypyodbc):
  service: sql server browser ->automatic, start (stond disabled)
  node: sql server network configuration\Protocols for SQLEXPRESS ->TCP/IP enabled (stond disabled)
sql express management studio geinstalleerd
dir: db Northwind en pubs naar C:\SqlDatabases gekopieerd
verkenner, security: Users alle rechten op deze dir geven, ander error bij attach 
mgmt studio: Northwind en pubs ge-attached

python: library pypyodbc opgehaald met pip
  ncoi: pip staat in:

C:\>cd C:\Users\Cursist\AppData\Local\Programs\Python\Python35-32\Scripts
pip install pypyodbc
  haalt data uit PyPI (=Python Package Index, https://pypi.python.org/pypi)
  imports komen in:

  C:\Users\Cursist\AppData\Local\Programs\Python\Python35-32\Lib\site-packages
(kan je ook met de hand daarheen kopieren)

mdb: kan hij autom lezen; 32bit driver al geinstalleerd in Windows
accdb: 64bit driver wsch al geinstalleerd; zie Adm Tools, Data Sources ->tab Drivers
32bit odbc driver ophalen bij:
https://www.microsoft.com/en-US/download/details.aspx?id=13255
Microsoft Access Database Engine 2010 Redistributable
->bij klik op knop Download kun je de 32bit en 64bit versie beide aanvinken
AccessDatabaseEngine.exe
AccessDatabaseEngine_X64.exe
* installeren als Administrator

connect(connectString='', autocommit=False, ansi=False,
    timeout=0, unicode_results=True, readonly=False)
"""

import pypyodbc as db

#{SQL Server Native Client 10.0}; Integrated Security=SSPI
#cnString = r'Driver={SQL Server};Server=localhost\SQLEXPRESS;Database=Northwind;uid=sa;pwd=Pa$$w0rd'
#cnString = r'Driver={SQL Server};Server=.\SQLEXPRESS;Database=Northwind;Trusted_Connection=yes'
cnString = r'Driver={SQL Server};Server=.\SQLEXPRESS;Database=pubs;Trusted_Connection=yes'

# NWIND.MDB, BIBLIO.MDB
#cnString = r'Driver={Microsoft Access Driver (*.mdb)}' \
#    r';DBQ=C:\Sql2005DataBases\nwind.mdb'
#cnString = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}' \
#    r';DBQ=C:\Sql2005DataBases\Raaket.accdb'        #uit oefeningen Computrain

sqlShippers = "select * from Shippers"
sqlProducts = "select ProductID, ProductName, CategoryID, UnitPrice, UnitsInStock from Products"

#con = db.connect(cnString)
#cur = con.cursor()
#cur.execute(sqlShippers)

def readnull():
    cn = db.connect(cnString)
    cursor = cn.cursor()
    cursor.execute("select 3, null, null")
    
    row = cursor.fetchone()
    print(row)
    cursor.close()
    cn.close()          #sluit NIET autom cursor


def tblinfo():
    cn = db.connect(cnString)
    cursor = cn.cursor()
    # .tables(table,catalog,schema,tableType); TABLE|VIEW|SYSTEM TABLE (of kl lett)
    c = cursor.tables(tableType='table')
    for t in c:
        print(t)
    cursor.close()
    cn.close()

    
def readpubs():
    cn = db.connect(cnString)
    cursor = cn.cursor()
    cursor.execute('select * from authors')
    for row in cursor:
        print(row)
    cursor.close()
    cn.close()          #sluit NIET autom cursor
    

def readRaaket():              #accdb
    cn = db.connect(cnString)
    cursor = cn.cursor()
    tbl = 'tblContributie'          #tblContributie, tblLeden
    cols = [tup[3] for tup in cursor.columns(tbl)]
    print("Velden: ", cols)
    print()

    cursor.execute('select * from ' + tbl)
    #cursor.execute("select * from tblLeden where Achternaam like 'B%'")
    for row in cursor:
        print(row[0], row[1], row[2], row[3])
    cursor.close()
    cn.close()          #sluit NIET autom cursor

    
def readShippers0():
    cn = db.connect(cnString)
    cursor = cn.cursor()

    print("Velden: ShipperID, CompanyName, Phone")
    cursor.execute(sqlShippers)
    
    row = cursor.fetchone()
    while row:
        print("%2s  %-24s  %s" % (row[0], row[1], row[2]))
        # vlg geeft allemaal None of niks
        #print("%2s  %-24s  %s" % (row.get('ShipperID'), row.get('CompanyName'), row.get('Phone')))
        #print("%2s  %-24s  %s" % (row['ShipperID'], row['CompanyName'], row['Phone']))
        #print("%2s  %-24s  %s" % (row.ShipperID, row.CompanyName, row.Phone))
        row = cursor.fetchone()
    print('\nAantal rijen: ', cursor.rowcount)

    cursor.close()
    cn.close()          #sluit NIET autom cursor
    print('cursor.closed: ',cursor.closed)
    print('connected: ', cn.connected)

def readShippers1():
    cn = db.connect(cnString)
    cursor = cn.cursor()

    # vlg wordt aparte query ->draaien voor cursor.execute(sqlShippers)
    # vlg geeft list met tupels, iedere tupel bevat naam + metadata over een veld
    # vlg toont van iedere tupel alleen het 4e item; daarin zit de veldnaam
    # (netjes met de juiste hfdletters)
    # cur.columns(table,catalog,schema,column)
    cols = [tup[3] for tup in cursor.columns('shippers')]
    print("Velden: ", cols)

    cursor.execute(sqlShippers)     #retval: zelfde cursor=obj
    # vlg beschikbaar na cursor.execute(), volgorde anders, kl lett
    # [('shipperid', <class 'int'>, 11, 10, 10, 0, False), ('companyname', <class 'str'>, 40, 40, 40, 0, False), ('phone', <class 'str'>, 24, 24, 24, 0, True)]
    #cols = [tup[0] for tup in cursor.description]
    #print("Velden: ", cols)

    #for p,q,r in cursor.fetchall():     #geeft list met tuples, op client
    #for p,q,r in cursor:               #cursor is zelf al een iterator, efficienter
    #    print("%2s  %-24s  %s" % (p, q, r))
    for row in cursor:
        print(row)
    print('\nAantal rijen: ', cursor.rowcount)        # -1
    cursor.close()
    cn.close()

def readShippersRegion():
    cn = db.connect(cnString)
    cursor = cn.cursor()
    cursor.execute(sqlShippers + '; select * from region;')
    print('\n  Shippers:')
    for row in cursor:
        print(row)
    if cursor.nextset():
        print('\n  Region:')
        for row in cursor:
            print(row)
        
    cursor.close()
    cn.close()

def readTable(sql, sqlext=''):
    cn = db.connect(cnString)
    cursor = cn.cursor()
    cursor.execute(sql + ' ' + sqlext)
    cols = [tup[0] for tup in cursor.description]
    print("Velden: ", cols)
    for row in cursor:
        print(row)
    cursor.close()
    cn.close()


def execprocCustOrderHist():
    cn = db.connect(cnString)
    cursor = cn.cursor()
    # vlg in pypyodbc 'Still not fully implemented'
    #cursor.callproc('CustOrderHist', ['ALFKI'])     #fout
    # vlg kan geen output params verwerken!
    cursor.execute("exec CustOrderHist 'ALFKI'")           #goed
    for row in cursor:
        print(row)
    cursor.close()
    cn.close()

def execproczkEmployee(empid):
    #output params ophalen via extra sql vars, die ik in 1 select zet
    cn = db.connect(cnString)
    cursor = cn.cursor()
    cursor.execute("""
declare @empid int
declare @naam varchar(32)
declare @tel varchar(24)
declare @retval int
set @empid = ?

exec @retval = dbo.zkEmployee @empid, @naam output, @tel output

select @empid as 'EmployeeID'
, @naam as 'Name'
, @tel as 'Phone'
, @retval as 'retval'
""", empid)           #goed
    #retval geeft len(@naam), gaf err in sp bij @naam=null ->sp gewijzigd
    # in len(isnull(@naam, ''))
    print(cursor.fetchone())
    cursor.close()
    cn.close()


def insertShippersParam(values):   #values als list of tuple [CompanyName,Phone]
    cn = db.connect(cnString)       #, autocommit=True
    cursor = cn.cursor()
    cursor.execute("insert into Shippers(CompanyName, Phone) values(?,?)", values)
    cnt = cursor.rowcount
    cn.commit()         #default cn.autocommit = False
    cursor.close()
    cn.close()          #close() doet geen autocommit
    return cnt

def updateShippersParam(values):   #values als list [CompanyName,Phone,ShipperID]
    cn = db.connect(cnString)
    cursor = cn.cursor()
    try:
        cursor.execute("update Shippers set CompanyName=?, Phone=? where ShipperID=?", values)
        #cursor.execute("update Shippers set CompanyName=null, Phone=123 where ShipperID=31")
        cnt = cursor.rowcount
        cn.commit()         #default cn.autocommit = False
    except db.IntegrityError as ex:
        cn.rollback()
        print('Integr error: ', ex)
        cnt = 0
    except db.ProgrammingError as ex:       #als je foute tblnaam gebruikt
        cn.rollback()
        print(ex)
        cnt = 0
    except db.DataError as ex:       #als je fout gegevenstype gebruikt
        cn.rollback()
        print(ex)
        cnt = 0
    cursor.close()
    cn.close()
    return cnt

def deleteShippersParam(values):   #values als list met 1 [ShipperID]
    cn = db.connect(cnString)
    cursor = cn.cursor()
    try:
        cursor.execute("delete from Shippers where ShipperID = ?", values)
        cnt = cursor.rowcount
        cn.commit()
    except (db.IntegrityError, db.ProgrammingError, db.DataError) as ex:
        cn.rollback()
        print(ex)
        cnt = 0
    cursor.close()
    cn.close()
    return cnt

def deleteShippersParamMany(values):   #values als list met tupels [ShipperID's]
    cn = db.connect(cnString)
    cursor = cn.cursor()
    try:
        # vlg voert stmt meermaals uit
        c = cursor.executemany("delete from Shippers where ShipperID = ?", values)
        print(c)
        cnt = cursor.rowcount       #wordt -1, helaas
        cn.commit()
    except (db.IntegrityError, db.ProgrammingError) as ex:
        cn.rollback()
        print(ex)
        cnt = 0
    cursor.close()
    cn.close()
    return cnt


#--------- hoofdprogramma:

#readnull()
#tblinfo()

readpubs()
#readRaaket()

#readShippers0()
#readShippers1()
#readShippersRegion()

#readTable(sqlShippers)
#readTable(sqlShippers, "where shipperid > 50")
#readTable(sqlProducts)
#readTable(sqlProducts, "where productid <= 10"
#     " order by unitprice desc")
#readTable(sqlProducts, "where productname like 'Louis%'")
#readTable("select CustomerID, CompanyName, ContactName, Region, Country"
#          " from Customers", "where Region is not null")

#execprocCustOrderHist()
#execproczkEmployee([9])         # 9 emps

#print("%d records toegevoegd" % insertShippersParam(['Bes', '031-1116723']))

#print("%d records gewijzigd" % updateShippersParam(('Boes', '032-3336723', 38)))
# None wordt binnen sql automatisch null
#print("%d records gewijzigd" % updateShippersParam((None, '032-3336723', 33)))

#print("%d records gewist" % deleteShippersParam(['allemaal']))
#print("%d records gewist" % deleteShippersParam([40]))
#print("%d records gewist" % deleteShippersParamMany([(33,), (34,)]))


"""
cursor.execute("BEGIN TRANSACTION")
cursor.execute("INSERT SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) OUTPUT INSERTED.ProductID VALUES ('SQL Server Express New', 'SQLEXPRESS New', 0, 0, CURRENT_TIMESTAMP)")  
conn.rollback()  
conn.close()


print(list(cursor.statistics('shippers'))  #('shippers','northwind')
cursor.primaryKeys('shippers')    #iterable
cursor.foreignKeys('customers')   #idem,vanuit 1-kant naar veel-kant
cursor.tables()     # iterable, alle tbl + vw

cursor.arraysize    # 1, std voor fetchmany()
cursor.connection   # ->cn obj

"""

