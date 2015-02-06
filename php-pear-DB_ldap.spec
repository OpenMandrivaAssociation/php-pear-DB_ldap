%define		_class		DB
%define		_subclass	ldap
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.2.1
Release:	4
Summary:	DB interface to LDAP server
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/DB_ldap/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
The PEAR::DB_ldap class provides a DB compliant interface to LDAP
servers.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/data

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Sun Dec 18 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-1mdv2012.0
+ Revision: 743484
- 1.2.1

* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-7
+ Revision: 741847
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-6
+ Revision: 679291
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-5mdv2011.0
+ Revision: 613632
- the mass rebuild of 2010.1 packages

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.0-4mdv2010.1
+ Revision: 479290
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.2.0-3mdv2010.0
+ Revision: 440974
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2mdv2009.1
+ Revision: 321961
- rebuild

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.0-1mdv2009.0
+ Revision: 278912
- update to new version 1.2.0

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-7mdv2009.0
+ Revision: 236828
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Nov 12 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-6mdv2007.0
+ Revision: 83324
- rebuild

* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-5mdv2007.0
+ Revision: 81549
- Import php-pear-DB_ldap

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-5mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-1mdk
- 1.1.1

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-1mdk
- initial Mandriva package (PLD import)

