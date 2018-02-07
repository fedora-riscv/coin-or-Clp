%global		module		Clp

Name:		coin-or-%{module}
Group:		Applications/Engineering
Summary:	Coin-or linear programming
Version:	1.16.10
Release:	6%{?dist}
License:	EPL
URL:		http://projects.coin-or.org/%{module}
Source0:	http://www.coin-or.org/download/pkgsource/%{module}/%{module}-%{version}.tgz
BuildRequires:	atlas-devel
BuildRequires:	blas-devel
BuildRequires:	bzip2-devel
BuildRequires:	coin-or-CoinUtils-devel
BuildRequires:	coin-or-Osi-devel
BuildRequires:	doxygen
BuildRequires:	glpk-devel
BuildRequires:	graphviz
BuildRequires:	lapack-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires: 	zlib-devel

# Install documentation in standard rpm directory
Patch0:		%{name}-docdir.patch

%description
Clp (Coin-or linear programming) is an open-source linear programming
solver written in C++. It is primarily meant to be used as a callable
library, but a basic, stand-alone executable version is also available.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	coin-or-CoinUtils-devel
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation files for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
This package contains the documentation for %{name}.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%configure
# Kill rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags} all doxydoc

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
cp -a doxydoc/html %{buildroot}%{_docdir}/%{name}

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make test

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/AUTHORS
%doc %{_docdir}/%{name}/clp_addlibs.txt
%doc %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README
%{_bindir}/clp
%{_libdir}/*.so.*

%files		devel
%{_includedir}/coin/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files		doc
%doc %{_docdir}/%{name}/html

%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Mar 11 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.10-1
- Update to latest upstream release (#1308278)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 11 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.9-1
- Update to latest upstream release (#1270497)

* Fri Sep 25 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.8-1
- Update to latest upstream release (#1257923)
- Remove no longer needed patch to prevent coin-or-OS crash in %%check

* Mon Jun 22 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.6-5
- Correct crash on coin-or-OS check

* Sat Jun 20 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.6-4
- Bump release.

* Sat Jun 20 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.6-3
- Full rebuild or coin-or stack.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.6-1
- Update to latest upstream release (#1201068)

* Sat Feb 21 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.3-2
- Rebuild to ensure using latest C++ abi changes.

* Mon Feb  9 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.3-1
- Update to latest upstream release (#1190729).

* Sat Feb 07 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.16.1-1
- Update to latest upstream release (#1159475).

* Sun Aug 31 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.15.10-2
- Rebuild to ensure packages are built in proper order.

* Sat Aug 30 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.15.10-1
- Update to latest upstream release (#1133195#c2).

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 16 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.15.7-1
- Update to latest upstream release (#1089923).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov  4 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.15.3-3
- Correct source url path (#894587#c7).
- Add coin-or-CoinUtils-devel requires to the devel package (#894587#c7).

* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.15.3-2
- Use proper _smp_flags macro (#894586#c6).

* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.15.3-1
- Update to latest upstream release.

* Mon Jan 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.14.8-1
- Update to latest upstream release.

* Sat Jan 12 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.14.7-3
- Rename repackaged tarball.

* Sun Nov 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.14.7-2
- Rename package to coin-or-Clp.
- Do not package Thirdy party data or data without clean license.

* Thu Sep 27 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.14.7-1
- Initial coinor-Clp spec.
