%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Recordset
Summary:	DBIx-Recordset perl module
Summary(pl):	Modu³ perla DBIx-Recordset
Name:		perl-DBIx-Recordset
Version:	0.24
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
DBIx::Recordset is a perl module for abstraction and simplification of
database access.

The goal is to make standard database access (select/insert/update/delete)
easier to handle and independend of the underlying DBMS. Special attention
is made on web applications to make it possible to handle the state-less
access and to process the posted data of formfields, but DBIx::Recordset
is not limited to web applications.

%description -l pl
DBIx::Recordset jest modu³em perla, umo¿liwiaj±cym ³atwy dostêp do baz
danych na wy¿szym, ni¿ oferowany przez modu³ DBI poziomie abstrakcji.

Celem jest uproszczenie typowych (odczyt/zapis/nadpisanie/usuniêcie)
operacji na bazie danych, oraz uniezale¿nienie ich od stosowanego DBMS.
Szczególn± uwagê po¶wiêcono umo¿liwieniu aplikacjom internetowym
obs³ugi bezstanowego dostêpu i przetwarzania danych z formularzy, ale
DBIx::Recordset nie jest ograniczony do WWW.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
# Strip out broken-by-design test preparation code; tests requires
# configured RDBMS anyway.  I have tested it locally, it works; it's
# noarch, so tests are needless.
/usr/bin/perl -ni -e 'print unless 11...197' Makefile.PL

%build
%{__perl} Makefile.PL < /dev/null
%{__make}
#%%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f eg/README README.eg

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO README.eg
%{perl_sitelib}/DBIx/*.pm
%{perl_sitelib}/DBIx/Intrors.pod
%dir %{perl_sitelib}/DBIx/Recordset
%{perl_sitelib}/DBIx/Recordset/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
