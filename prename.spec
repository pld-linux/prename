Summary:	Perl script to rename multiple files
Name:		prename
Version:	1.9
Release:	1
License:	GPL+ or Artistic
Group:		Applications/System
URL:		https://metacpan.org/release/rename
Source0:	https://cpan.metacpan.org/authors/id/P/PE/PEDERST/rename-%{version}.tar.gz
# Source0-md5:	16df2adde955a6867701564e3d7c6a52
# This patch renames the executable from rename to prename
Patch0:		%{name}-1.9-namechange.patch
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Prename renames the file names supplied according to the rule
specified as the first argument. The argument is a Perl expression
which is expected to modify the $_ string for at least some of the
file names specified.

%prep
%setup -q -n rename-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	PREFIX=%{_prefix} \
	INSTALLSITEMAN1DIR=%{_mandir}/man1 \
	NO_PACKLIST=1
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
