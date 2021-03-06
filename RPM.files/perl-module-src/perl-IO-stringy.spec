Summary: IO-stringy Perl module
Name: perl-IO-stringy
Version: 2.110
Release: 2
Packager: mailscanner@ecs.soton.ac.uk
License: GPL or Artistic
Group: Development/Libraries
URL: http://search.cpan.org/dist/IO-stringy/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
#BuildRequires: perl >= 0:5.00503
Source0: IO-stringy-2.110.tar.gz

%description
IO-stringy Perl module

%description
IO-stringy Perl module
%prep
%setup -q -n IO-stringy-%{version} 1

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
make
make test

%clean
rm -rf $RPM_BUILD_ROOT
%install

rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
make install DESTDIR=$RPM_BUILD_ROOT

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find $RPM_BUILD_ROOT/usr -type f -print | \
	sed "s@^$RPM_BUILD_ROOT@@g" | \
	grep -v perllocal.pod | \
	grep -v "\.packlist" > IO-stringy-%{version}-filelist
if [ "$(cat IO-stringy-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%files -f IO-stringy-%{version}-filelist
%defattr(-,root,root)

%changelog
* Sun Oct 06 2002 Julian Field <mailscanner@ecs.soton.ac.uk>
- Specfile autogenerated

