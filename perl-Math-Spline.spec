#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Math-Spline
Version  : 0.02
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Math-Spline-0.02.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Math-Spline-0.02.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmath-spline-perl/libmath-spline-perl_0.02-2.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Math-Spline-license = %{version}-%{release}
Requires: perl-Math-Spline-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Math::Derivative)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Perl Module Math::Spline - 0.02
This program is free software; you can redistribute it and/or
modify it under the same terms as Perl itself.

%package dev
Summary: dev components for the perl-Math-Spline package.
Group: Development
Provides: perl-Math-Spline-devel = %{version}-%{release}
Requires: perl-Math-Spline = %{version}-%{release}

%description dev
dev components for the perl-Math-Spline package.


%package license
Summary: license components for the perl-Math-Spline package.
Group: Default

%description license
license components for the perl-Math-Spline package.


%package perl
Summary: perl components for the perl-Math-Spline package.
Group: Default
Requires: perl-Math-Spline = %{version}-%{release}

%description perl
perl components for the perl-Math-Spline package.


%prep
%setup -q -n Math-Spline-0.02
cd %{_builddir}
tar xf %{_sourcedir}/libmath-spline-perl_0.02-2.debian.tar.xz
cd %{_builddir}/Math-Spline-0.02
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Math-Spline-0.02/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Math-Spline
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Math-Spline/ad09dfd1729df50a9786d6c95d43a409f7022f21 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Math::Spline.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Math-Spline/ad09dfd1729df50a9786d6c95d43a409f7022f21

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
