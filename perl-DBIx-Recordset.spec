#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Recordset
Summary:	DBIx::Recordset - abstraction and simplification of database access
Summary(pl):	DBIx::Recordset - abstrakcja i uproszczenie dost�pu do bazy danych
Name:		perl-DBIx-Recordset
Version:	0.24
Release:	3
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	76835b342ac63d731a4eb9529613ee99
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::Recordset is a perl module for abstraction and simplification of
database access.

The goal is to make standard database access
(select/insert/update/delete) easier to handle and independend of the
underlying DBMS.  Special attention is made on web applications to
make it possible to handle the state-less access and to process the
posted data of formfields, but DBIx::Recordset is not limited to web
applications.

%description -l pl
DBIx::Recordset jest modu�em perla, umo�liwiaj�cym �atwy dost�p do baz
danych na wy�szym, ni� oferowany przez modu� DBI poziomie abstrakcji.

Celem jest uproszczenie typowych (odczyt/zapis/nadpisanie/usuni�cie)
operacji na bazie danych, oraz uniezale�nienie ich od stosowanego
DBMS. Szczeg�ln� uwag� po�wi�cono umo�liwieniu aplikacjom internetowym
obs�ugi bezstanowego dost�pu i przetwarzania danych z formularzy, ale
DBIx::Recordset nie jest ograniczony do WWW.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
# Strip out broken-by-design test preparation code; tests requires
# configured RDBMS anyway.  I have tested it locally, it works; it's
# noarch, so tests are needless.
/usr/bin/perl -ni -e 'print unless 11...197' Makefile.PL

%build
%{__perl} Makefile.PL < /dev/null \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f eg/README README.eg

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO README.eg
%{perl_vendorlib}/DBIx/*.pm
%dir %{perl_vendorlib}/DBIx/Recordset
%{perl_vendorlib}/DBIx/Recordset/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
