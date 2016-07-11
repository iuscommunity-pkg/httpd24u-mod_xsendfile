# IUS spec file for httpd24u-mod_xsendfile forked from Fedora:

%global httpd httpd24u
%global module mod_xsendfile

Summary:	Apache module to send files efficiently
Name:		%{httpd}-%{module}
Version:	0.12
Release:	1.ius%{?dist}
Group:		System Environment/Daemons
License:	ASL 2.0
URL:		https://tn123.org/%{module}/
Source0:	https://tn123.org/%{module}/%{module}-%{version}.tar.bz2
Source1:	10-xsendfile.conf
BuildRequires:	%{httpd}-devel
Requires:       %{httpd}, httpd-mmn = %{_httpd_mmn}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Conflicts:      %{module}

%description
%{module} is a small Apache2 module that processes X-SENDFILE headers
registered by the original output handler.

If it encounters the presence of such header it will discard all output and
send the file specified by that header instead using Apache internals
including all optimizations like caching-headers and sendfile or mmap if
configured.

It is useful for processing script-output of e.g. php, perl or any cgi.


%prep
%setup -q -n %{module}-%{version}


%build
%{_httpd_apxs} -c %{module}.c


%install
rm -rf $%{buildroot}
mkdir -p %{buildroot}/%{_httpd_moddir}
%{_httpd_apxs} -i -S LIBEXECDIR=%{buildroot}/%{_httpd_moddir} -n %{module} %{module}.la
mkdir -p %{buildroot}/%{_httpd_modconfdir}
cp -p %SOURCE1 %{buildroot}/%{_httpd_modconfdir}


%clean
rm -rf %{buildroot}


%files
%doc docs/*
%config(noreplace) %{_httpd_modconfdir}/10-xsendfile.conf
%{_httpd_moddir}/%{module}.so


%changelog
* Mon Jul 11 2016 Ben Harper <ben.harper@rackspace.com> - 0.12.-1.ius
- Port from Fedora to IUS

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 27 2012 Orion Poplawski <orion@cora.nwra.com> 0.12-5
- Rebuild for httpd 2.4, update for new module guidelines

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Apr 25 2011 Orion Poplawski <orion@cora.nwra.com> 0.12-3
- Fix license tag

* Wed Dec 1 2010 Orion Poplawski <orion@cora.nwra.com> 0.12-2
- Upstream fixed tar ball packaging

* Mon Oct 25 2010 Orion Poplawski <orion@cora.nwra.com> 0.12-1
- Initial package
