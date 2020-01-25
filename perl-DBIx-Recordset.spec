#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	DBIx
%define		pnam	Recordset
Summary:	DBIx::Recordset - abstraction and simplification of database access
Summary(pl.UTF-8):	DBIx::Recordset - abstrakcja i uproszczenie dostępu do bazy danych
Name:		perl-DBIx-Recordset
Version:	0.26
Release:	2
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fe008ad93b76ac0dea487f0c014842ee
URL:		http://search.cpan.org/dist/DBIx-Recordset/
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
underlying DBMS. Special attention is made on web applications to make
it possible to handle the state-less access and to process the posted
data of formfields, but DBIx::Recordset is not limited to web
applications.

%description -l pl.UTF-8
DBIx::Recordset jest modułem Perla, umożliwiającym łatwy dostęp do baz
danych na wyższym, niż oferowany przez moduł DBI poziomie abstrakcji.

Celem jest uproszczenie typowych (odczyt/zapis/nadpisanie/usunięcie)
operacji na bazie danych, oraz uniezależnienie ich od stosowanego
DBMS. Szczególną uwagę poświęcono umożliwieniu aplikacjom internetowym
obsługi bezstanowego dostępu i przetwarzania danych z formularzy, ale
DBIx::Recordset nie jest ograniczony do WWW.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"%{pdir}::%{pnam}")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f eg/README README.eg

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
