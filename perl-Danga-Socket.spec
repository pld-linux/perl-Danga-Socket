#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Danga
%define	pnam	Socket
Summary:	Danga::Socket - Event loop and event-driven async socket base class
Summary(pl.UTF-8):	Danga::Socket - pętla zdarzeń i klasa podstawowa gniazd asynchronicznych
Name:		perl-Danga-Socket
Version:	1.61
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Danga/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dc8f481b35172a090b977f3dea7fa24a
URL:		http://search.cpan.org/dist/Danga-Socket/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Sys-Syscall
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an abstract base class for objects backed by a socket which
provides the basic framework for event-driven asynchronous IO,
designed to be fast. Danga::Socket is both a base class for objects,
and an event loop.

%description -l pl.UTF-8
Ten moduł jest abstrakcyjną klasą bazową dla obiektów opartych na
gniazdach. Udostępnia podstawowy szkielet asynchronicznego we/wy
sterowanego zdarzeniami, zaprojektowany z myślą o szybkości.
Danga::Socket jest zarówno klasą bazową dla obiektów, jak i pętlą
zdarzeń.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%dir %{perl_vendorlib}/Danga
%{perl_vendorlib}/Danga/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
