Summary: OLE-Storage_Lite Perl module
Name: perl-OLE-Storage_Lite
Version: 0.16
Release: 1
Packager: mailscanner@ecs.soton.ac.uk
License: GPL or Artistic
Group: Development/Libraries
URL: http://search.cpan.org/dist/OLE-Storage_Lite/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
#BuildRequires: perl >= 0:5.00503
Source0: OLE-Storage_Lite-0.16.tar.gz

%description
OLE-Storage_Lite Perl module

%description
OLE-Storage_Lite Perl module
%prep
%setup -q -n OLE-Storage_Lite-%{version} 1

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL PREFIX=$RPM_BUILD_ROOT/usr 
make
make test

%clean
rm -rf $RPM_BUILD_ROOT
%install

rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
make install

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find $RPM_BUILD_ROOT/usr -type f -print | \
	sed "s@^$RPM_BUILD_ROOT@@g" | \
	grep -v perllocal.pod | \
	grep -v "\.packlist" > OLE-Storage_Lite-%{version}-filelist
if [ "$(cat OLE-Storage_Lite-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%files -f OLE-Storage_Lite-%{version}-filelist
%defattr(-,root,root)

%changelog
* Tue May 23 2006 Julian Field <mailscanner@ecs.soton.ac.uk>
- Specfile autogenerated
