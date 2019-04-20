#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Math-Spline
Version  : 0.02
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Math-Spline-0.02.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Math-Spline-0.02.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmath-spline-perl/libmath-spline-perl_0.02-2.debian.tar.xz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Math-Spline-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Math::Derivative)

%description
Perl Module Math::Spline - 0.02
This program is free software; you can redistribute it and/or
modify it under the same terms as Perl itself.

%package dev
Summary: dev components for the perl-Math-Spline package.
Group: Development
Provides: perl-Math-Spline-devel = %{version}-%{release}

%description dev
dev components for the perl-Math-Spline package.


%package license
Summary: license components for the perl-Math-Spline package.
Group: Default

%description license
license components for the perl-Math-Spline package.


%prep
%setup -q -n Math-Spline-0.02
cd ..
%setup -q -T -D -n Math-Spline-0.02 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Math-Spline-0.02/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Math-Spline
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Math-Spline/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.2/Math/Spline.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Math::Spline.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Math-Spline/deblicense_copyright
