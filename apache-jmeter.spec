%define oname jmeter
%define jdk %{_prefix}/lib/jvm/java-openjdk

Summary:	JMeter for testing Web Applications
Name:		apache-%{oname}
Version:	3.0
Release:	3
License:	ASL2.0
Group:		Development/Other
Url:		http://jmeter.apache.org/
Source:		%{name}-%{version}_src.tgz
BuildRequires:	ant
BuildRequires:	java-devel
Requires:	java >= 1.6
BuildArch:	noarch

%description
Apache JMeter may be used to test performance both
on static and dynamic resources (Webservices (SOAP/REST),
Web dynamic languages - PHP, Java, ASP.NET, Files, etc. -,
Java Objects, Data Bases and Queries, FTP Servers and more).
It can be used to simulate a heavy load on a server,
group of servers, network or object to test its strength
or to analyze overall performance under different load types.
You can use it to make a graphical analysis of performance
or to test your server/script/object behavior under
heavy concurrent load.

%files
%doc README LICENSE
%{_bindir}/%{oname}
%{_datadir}/%{oname}/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
ant download_jars
JAVA_HOME=%{jdk} ant

%install
#ant install
mkdir -p %{buildroot}%{_datadir}/%{oname}/lib
mkdir -p %{buildroot}%{_datadir}/%{oname}/bin
mkdir -p %{buildroot}%{_datadir}/%{oname}/bin/examples
mkdir -p %{buildroot}%{_datadir}/%{oname}/bin/templates
mkdir -p %{buildroot}%{_datadir}/%{oname}/bin/testfiles

cp -r lib/* %{buildroot}%{_datadir}/%{oname}/lib

install -Dm0755 bin/%{oname}		%{buildroot}%{_datadir}/%{oname}/bin/
install -Dm0755 bin/*server		%{buildroot}%{_datadir}/%{oname}/bin/
install -Dm0755 bin/*.sh		%{buildroot}%{_datadir}/%{oname}/bin/
install -Dm0644 bin/*.properties	%{buildroot}%{_datadir}/%{oname}/bin/
install -Dm0644 bin/*.conf		%{buildroot}%{_datadir}/%{oname}/bin/
install -Dm0644 bin/ApacheJMeter.jar	%{buildroot}%{_datadir}/%{oname}/bin/
install -Dm0644 bin/*.xml		%{buildroot}%{_datadir}/%{oname}/bin/
install -Dm0644 bin/*.parameters	%{buildroot}%{_datadir}/%{oname}/bin/
install -Dm0644 bin/*.bshrc		%{buildroot}%{_datadir}/%{oname}/bin/

cp -r bin/examples/*			%{buildroot}%{_datadir}/%{oname}/bin/examples/
cp -r bin/templates/*			%{buildroot}%{_datadir}/%{oname}/bin/templates/
cp -r bin/testfiles/*			%{buildroot}%{_datadir}/%{oname}/bin/testfiles/

mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf ../..%{_datadir}/%{oname}/bin/%{oname} %{oname}
popd
